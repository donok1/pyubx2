'''
UBX Message Protocol Class

Created on 26 Sep 2020

@author: semuadmin
'''

import struct

import pyubx2.exceptions as ube
import pyubx2.ubxtypes as ubt

INPUT = 0
OUTPUT = 1


class UBXMessage():
    '''
    UBX Message Class.
    '''

    def __init__(self, ubx_class, ubx_id, payload=b'', inout=INPUT):
        '''
        Constructor.

        Accepts message class/id in bytes or ASCII format.
        '''

        self._header = ubt.UBX_HDR
        if isinstance(ubx_class, str) and isinstance(ubx_id, str):  # e.g. 'CFG, CFG-PRT'
            (self._ubx_class, self._ubx_id) = self.ubx_str2bytes(ubx_class, ubx_id)
        else:  # e.g. b'\x06', b'\x01'
            self._ubx_class = ubx_class
            self._ubx_id = ubx_id
        if isinstance(payload, str):
            payload = bytes(payload, 'utf-8')
        self._length = self.len2bytes(len(payload))
        self._checksum = self.calc_checksum(self._ubx_class + self._ubx_id +
                                            self._length + payload)
        self._inout = inout

        if payload:
            self.payload = payload

    def __str__(self) -> str:
        '''
        String representation.
        '''

        return repr(self)

    def __repr__(self) -> str:
        '''
        Human readable representation.
        '''

        clsid = None

        umsg_name = self.identity
        rep = f"<UBX({umsg_name}, "
        for i, att in enumerate(self.__dict__):
            if att[0] != '_':  # only show public attributes
                val = self.__dict__[att]
                # if the attributes include a UBX class & id,
                # show the ASCII lookup form rather than the binary
                try:
                    # if it's an ACK-ACK or ACK-NAK, we show what it's acknowledging in plain text
                    if self._ubx_class == b'\x05':  # ACK
                        if att == 'clsID':
                            clsid = val
                            val = ubt.UBX_CLASSES[clsid]
                        if att == 'msgID' and clsid:
                            val = ubt.UBX_MSGIDS[clsid][val]
                    # if it's a CFG-MSG, we show what message class/id it refers to in plain text
                    if self._ubx_class == b'\x06' and self._ubx_id == b'\x01':  # CFG-MSG
                        if att == 'msgClass':
                            clsid = val
                            val = ubt.UBX_CONFIG_CATEGORIES[val]
                        if att == 'msgID' and clsid:
                            val = ubt.UBX_CONFIG_MESSAGES[clsid + val]
                except KeyError:
                    pass  # ignore any dictionary lookup errors and just show original binary value
                rep += att + '=' + str(val)
                if i < len(self.__dict__) - 1:
                    rep += ", "
        rep += ")>"
        return rep

    def serialize(self) -> bytes:
        '''
        Return message content as byte array suitable for writing to a stream.
        '''

        return (ubt.UBX_HDR + self._ubx_class + self._ubx_id + self._length
                +self._payload + self._checksum)

    @staticmethod
    def parse(message: bytes, validate: bool=False) -> object:
        '''
        Parse UBX byte array to UBXMessage object.

        Includes option to validate incoming payload length and checksum
        (UXBMessage will calculate and assign it's own values anyway).
        '''

        lenm = len(message)
        hdr = message[0:2]
        clsid = message[2:3]
        msgid = message[3:4]
        lenb = message[4:6]
        payload = message[6:lenm - 2]
        leni = len(payload)
        ckm = message[lenm - 2:lenm]
        ckv = UBXMessage.calc_checksum(clsid + msgid + lenb + payload)
        if validate:
            if hdr != ubt.UBX_HDR:
                raise ube.UBXParseError(f"Invalid message header {hdr} - should be {ubt.UBX_HDR}")
            if leni != UBXMessage.bytes2len(lenb):
                raise ube.UBXParseError(f"Invalid payload length {lenb} - should be {UBXMessage.len2bytes(leni)}")  # pylint: disable=line-too-long
            if ckm != ckv:
                raise ube.UBXParseError(f"Message checksum {ckm} invalid - should be {ckv}")
        return UBXMessage(clsid, msgid, payload)

    @staticmethod
    def bytes2len(length: bytes) -> int:
        '''
        Convert payload length as bytes to integer.
        '''

        return int.from_bytes(length, 'little', signed=False)

    @staticmethod
    def len2bytes(length: int) -> bytes:
        '''
        Convert payload length as integer to two little-endian bytes.
        '''

        return length.to_bytes(2, byteorder="little", signed=False)

    @staticmethod
    def calc_checksum(content: bytes) -> bytes:
        '''
        Return the Fletcher-8 checksum for the message content
        (content = clsid + msgid + length + payload).
        '''

        check_a = 0
        check_b = 0

        for char in content:
            check_a += char
            check_a &= 0xFF
            check_b += check_a
            check_b &= 0xFF

        return bytes((check_a, check_b))

    @staticmethod
    def isvalid_checksum(message: bytes) -> bool:
        '''
        Validate input message's checksum
        ('message' includes header and checksum)
        '''

        lenm = len(message)
        ckm = message[lenm - 2:lenm]
        return ckm == UBXMessage.calc_checksum(message[2:lenm - 2])

    @staticmethod
    def ubx_str2bytes(clsname: str, msgname: str):
        '''
        Convert plain text UBX message class to bytes
        e.g. 'CFG-MSG' to b'/x06/x01'.
        '''

        try:
            clsid = UBXMessage.key_from_val(ubt.UBX_CLASSES, clsname)
            msgid = UBXMessage.key_from_val(ubt.UBX_MSGIDS[clsid], msgname)
            return (clsid, msgid)
        except KeyError as err:
            raise ube.UBXMessageError(f"Undefined message, class {clsname}, id {msgname}") from err

    @staticmethod
    def key_from_val(dictionary: dict, value):
        '''
        Helper method - get dictionary key corresponding to (unique) value.
        '''

        val = None
        for key, val in dictionary.items():
            if val == value:
                return key
        raise ube.UBXMessageError(f"Undefined message type {val}")

    @property
    def identity(self) -> str:
        '''
        Message identity getter.
        Returns identity in plain text form e.g. 'CFG-MSG'.
        '''

        try:
            umsg_name = ubt.UBX_MSGIDS[self._ubx_class][self._ubx_id]
        except KeyError as err:
            raise ube.UBXMessageError(f"Message type {self._ubx_class},{self._ubx_id} not defined") from err
        return umsg_name

    @property
    def header(self) -> bytes:
        '''Header getter'''
        return self._header

    @property
    def msg_cls(self) -> bytes:
        '''Class id getter'''
        return self._ubx_class

    @property
    def msg_id(self) -> bytes:
        '''Message id getter'''
        return self._ubx_id

    @property
    def length(self) -> bytes:
        '''Payload length getter (as 2 little-endian bytes)'''
        return self._length

    @property
    def payload(self) -> bytes:
        '''Payload getter - returns the raw payload bytes'''
        return self._payload

    @payload.setter
    def payload(self, payload: bytes):
        '''
        Payload setter.

        Dynamically adds and populates public class attributes in accordance
        with the class's payload definition in UBX_PAYLOADS_INPUT/OUTPUT.

        The private attribute '_payload' will always hold the raw payload bytes.
        '''

        self._payload = payload
        self._length = self.len2bytes(len(self._payload))
        offset = 0
        self._index = 0
        try:

            # lookup attributes from the relevant input/output dictionary
            if self._inout == INPUT:
                pdict = ubt.UBX_PAYLOADS_INPUT[self.identity]
            else:
                pdict = ubt.UBX_PAYLOADS_OUTPUT[self.identity]
            # parse each attribute
            for key in pdict.keys():
                (offset, att) = self._payload_attr(payload, offset, pdict, key)
            # recalculate checksum based on payload content
            self._checksum = self.calc_checksum(self._ubx_class + self._ubx_id
                                                +self._length + self._payload)

        except ube.UBXTypeError as err:
            raise ube.UBXTypeError(f"Undefined attribute type {att} in message class {self.identity}") \
                    from err
        except KeyError as err:
            raise ube.UBXMessageError(f"Undefined message class={self._ubx_class}, id={self._ubx_id}") \
                    from err

    def _payload_attr(self, payload : bytes, offset: int, pdict: dict, key: str):
        '''
        Recursive routine to parse individual payload attributes to their appropriate types
        '''
        # pylint: disable=no-member

        # print(f" _PAYLOAD_ATTR - identity={self.identity}, key = {key}")
        att = pdict[key]  # get attribute type
        if isinstance(att, dict):  # attribute is a dict i.e. a nested repeating group
            # get preceding attribute containing number of items in this repeating group
            # assumed to be 'numCh' unless otherwise specified in UBX_PAYLOADS
            if self.identity in 'TODO-OTHER-IDENTITIES-WITH-REPEATING-GROUPS':  # TODO
                rng = self.numCh  # or whatever
            else:
                rng = self.numCh
            for i in range(rng):
                self._index = i + 1
                for key1 in att.keys():
                    (offset, _) = self._payload_attr(payload, offset, att, key1)
        elif att == ubt.CH:  # attribute is a single variable-length string (e.g. INF-NOTICE)
            atts = len(payload)
            val = payload
        elif att[0:1] == 'X' or key in ('clsID', 'msgClass', 'msgID'):  # attribute is a bitmask or a ubx msgcls/id
            atts = int(att[1:3])  # attribute size in bytes
            val = payload[offset:offset + atts]  # the raw value in bytes
        else:  # attribute is an integer or float
            atts = int(att[1:3])
            val = payload[offset:offset + atts]
            if att[0:1] == 'U':  # unsigned integer
                val = int.from_bytes(val, 'little', signed=False)
            if att[0:1] == 'I':  # signed integer
                val = int.from_bytes(val, 'little', signed=True)
            if att[0:1] == 'R':  # float
                val = struct.pack('f', val)

        if not isinstance(att, dict):
            if self._index > 0:  # add 2-digit suffix to repeating attribute names
                key = key + "_{0:0=2d}".format(self._index)
            setattr(self, key, val)
            offset += atts

        return (offset, att)


# Quick test routine
if __name__ == "__main__":

    t = UBXMessage(b'\x06', b'\x01', b'\xf0\x03\x00\x01\x01\x01\x00\x00')
    print(t)
    t = UBXMessage('CFG', 'CFG-MSG', b'\xf1\x04\x00\x01\x01\x01\x00\x00')
    print(t)
    t = UBXMessage('INF', 'INF-NOTICE', 'Now is the time for all good men to come to the aid of the party')
    print(t)
    t = UBXMessage.parse(b'\xb5\x62\x05\x01\x02\x00\x06\x01\x0f\x38', False)
    print(t)
    t = UBXMessage.parse(b'\xb5\x62\x04\x02\x02\x00\x06\x01\x0f\x38', True)  # should produce UBXParseError