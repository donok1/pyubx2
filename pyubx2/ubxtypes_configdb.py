"""
UBX Protocol Configuration Database Keys

!!! TODO - WORK IN PROGRESS - THIS MAY CHANGE IN FINAL IMPLEMENTATION !!!

Used by CFG-VALGET, CFG-VALSET and CFG-VALDEL message types

Format:
"Configuration Name": (key, "type")

Created on 30 Nov 2020

@author: semuadmin
"""

from pyubx2.ubxtypes_core import (
    E1,
    E2,
    E4,
    I1,
    I2,
    I4,
    I8,
    L,
    R4,
    R8,
    U1,
    U2,
    U4,
    U8,
    X1,
    X2,
    X4,
    X8,
)

# bits 28..30 of Configuration Key ID represent
# storage length of Configuration Value in bytes
UBX_CONFIG_STORSIZE = {
    0x01: 1,
    0x02: 1,
    0x03: 2,
    0x04: 4,
    0x05: 8,
}

UBX_CONFIG_DATABASE = {
    # CFG-ANA AssistNow Autonomous and Offline configuration
    "CFG-ANA-USE_ANA": (0x10230001, L),
    "CFG-ANA-ORBMAXERR": (0x30230002, U2),
    # CFG-BATCH Batched output configuration
    "CFG-BATCH-ENABLE": (0x10260013, L),
    "CFG-BATCH-PIOENABLE": (0x10260014, L),
    "CFG-BATCH-MAXENTRIES": (0x30260015, U2),
    "CFG-BATCH-WARNTHRS": (0x30260016, U2),
    "CFG-BATCH-PIOACTIVELOW": (0x10260018, L),
    "CFG-BATCH-PIOID": (0x20260019, U1),
    "CFG-BATCH-EXTRAPVT": (0x1026001A, L),
    "CFG-BATCH-EXTRAODO": (0x1026001B, L),
    # CFG-GEOFENCE Geofencing configuration
    "CFG-GEOFENCE-CONFLVL": (0x20240011, E1),
    "CFG-GEOFENCE-USE_PIO": (0x10240012, L),
    "CFG-GEOFENCE-PINPOL": (0x20240013, E1),
    "CFG-GEOFENCE-PIN": (0x20240014, U1),
    "CFG-GEOFENCE-USE_FENCE1": (0x10240020, L),
    "CFG-GEOFENCE-FENCE1_LAT": (0x40240021, I4),
    "CFG-GEOFENCE-FENCE1_LON": (0x40240022, I4),
    "CFG-GEOFENCE-FENCE1_RAD": (0x40240023, U4),
    "CFG-GEOFENCE-USE_FENCE2": (0x10240030, L),
    "CFG-GEOFENCE-FENCE2_LAT": (0x40240031, I4),
    "CFG-GEOFENCE-FENCE2_LON": (0x40240032, I4),
    "CFG-GEOFENCE-FENCE2_RAD": (0x40240033, U4),
    "CFG-GEOFENCE-USE_FENCE3": (0x10240040, L),
    "CFG-GEOFENCE-FENCE3_LAT": (0x40240041, I4),
    "CFG-GEOFENCE-FENCE3_LON": (0x40240042, I4),
    "CFG-GEOFENCE-FENCE3_RAD": (0x40240043, U4),
    "CFG-GEOFENCE-USE_FENCE4": (0x10240050, L),
    "CFG-GEOFENCE-FENCE4_LAT": (0x40240051, I4),
    "CFG-GEOFENCE-FENCE4_LON": (0x40240052, I4),
    "CFG-GEOFENCE-FENCE4_RAD": (0x40240053, U4),
    # CFG-HW Hardware configuration
    "CFG-HW-ANT_CFG_VOLTCTRL": (0x10A3002E, L),
    "CFG-HW-ANT_CFG_SHORTDET": (0x10A3002F, L),
    "CFG-HW-ANT_CFG_SHORTDET_POL": (0x10A30030, L),
    "CFG-HW-ANT_CFG_OPENDET": (0x10A30031, L),
    "CFG-HW-ANT_CFG_OPENDET_POL": (0x10A30032, L),
    "CFG-HW-ANT_CFG_PWRDOWN": (0x10A30033, L),
    "CFG-HW-ANT_CFG_PWRDOWN_POL": (0x10A30034, L),
    "CFG-HW-ANT_CFG_RECOVER": (0x10A30035, L),
    "CFG-HW-ANT_SUP_SWITCH_PIN": (0x20A30036, U1),
    "CFG-HW-ANT_SUP_SHORT_PIN": (0x20A30037, U1),
    "CFG-HW-ANT_SUP_OPEN_PIN": (0x20A30038, U1),
    "CFG-HW-ANT_SUP_ENGINE": (0x20A30054, E1),
    "CFG-HW-ANT_SUP_SHORT_THR": (0x20A30055, U1),
    "CFG-HW-ANT_SUP_OPEN_THR": (0x20A30056, U1),
    # CFG-I2C Configuration of the I2C interface
    "CFG-I2C-ADDRESS": (0x20510001, U1),
    "CFG-I2C-EXTENDEDTIMEOUT": (0x10510002, L),
    "CFG-I2C-ENABLED": (0x10510003, L),
    # CFG-I2CINPROT Input protocol configuration of the I2C interface
    "CFG-I2CINPROT-UBX": (0x10710001, L),
    "CFG-I2CINPROT-NMEA": (0x10710002, L),
    "CFG-I2CINPROT-RTCM3X": (0x10710004, L),
    # CFG-I2COUTPROT Output protocol configuration of the I2C interface
    "CFG-I2COUTPROT-UBX": (0x10720001, L),
    "CFG-I2COUTPROT-NMEA": (0x10720002, L),
    # CFG-INFMSG Information message configuration
    "CFG-INFMSG-UBX_I2C": (0x20920001, X1),
    "CFG-INFMSG-UBX_UART1": (0x20920002, X1),
    "CFG-INFMSG-UBX_UART2": (0x20920003, X1),
    "CFG-INFMSG-UBX_USB": (0x20920004, X1),
    "CFG-INFMSG-UBX_SPI": (0x20920005, X1),
    "CFG-INFMSG-NMEA_I2C": (0x20920006, X1),
    "CFG-INFMSG-NMEA_UART1": (0x20920007, X1),
    "CFG-INFMSG-NMEA_UART2": (0x20920008, X1),
    "CFG-INFMSG-NMEA_USB": (0x20920009, X1),
    "CFG-INFMSG-NMEA_SPI": (0x2092000A, X1),
    # CFG-ITFM Jamming and interference monitor configuration
    "CFG-ITFM-BBTHRESHOLD": (0x20410001, U1),
    "CFG-ITFM-CWTHRESHOLD": (0x20410002, U1),
    "CFG-ITFM-ENABLE": (0x1041000D, L),
    "CFG-ITFM-ANTSETTING": (0x20410010, E1),
    "CFG-ITFM-ENABLE_AUX": (0x10410013, L),
    # CFG-LOGFILTER Data logger configuration
    "CFG-LOGFILTER-RECORD_ENA": (0x10DE0002, L),
    "CFG-LOGFILTER-ONCE_PER_WAKE_UP_ENA": (0x10DE0003, L),
    "CFG-LOGFILTER-APPLY_ALL_FILTERS": (0x10DE0004, L),
    "CFG-LOGFILTER-MIN_INTERVAL": (0x30DE0005, U2),
    "CFG-LOGFILTER-TIME_THRS": (0x30DE0006, U2),
    "CFG-LOGFILTER-SPEED_THRS": (0x30DE0007, U2),
    "CFG-LOGFILTER-POSITION_THRS": (0x40DE0008, U4),
    # CFG-MOT Motion detector configuration
    "CFG-MOT-GNSSSPEED_THRS": (0x20250038, U1),
    "CFG-MOT-GNSSDIST_THRS": (0x3025003B, U2),
    # CFG-MSGOUT Message output configuration
    "CFG-MSGOUT-NMEA_ID_DTM_I2C": (0x209100A6, U1),
    "CFG-MSGOUT-NMEA_ID_DTM_SPI": (0x209100AA, U1),
    "CFG-MSGOUT-NMEA_ID_DTM_UART1": (0x209100A7, U1),
    "CFG-MSGOUT-NMEA_ID_DTM_UART2": (0x209100A8, U1),
    "CFG-MSGOUT-NMEA_ID_DTM_USB": (0x209100A9, U1),
    "CFG-MSGOUT-NMEA_ID_GBS_I2C": (0x209100DD, U1),
    "CFG-MSGOUT-NMEA_ID_GBS_SPI": (0x209100E1, U1),
    "CFG-MSGOUT-NMEA_ID_GBS_UART1": (0x209100DE, U1),
    "CFG-MSGOUT-NMEA_ID_GBS_UART2": (0x209100DF, U1),
    "CFG-MSGOUT-NMEA_ID_GBS_USB": (0x209100E0, U1),
    "CFG-MSGOUT-NMEA_ID_GGA_I2C": (0x209100BA, U1),
    "CFG-MSGOUT-NMEA_ID_GGA_SPI": (0x209100BE, U1),
    "CFG-MSGOUT-NMEA_ID_GGA_UART1": (0x209100BB, U1),
    "CFG-MSGOUT-NMEA_ID_GGA_UART2": (0x209100BC, U1),
    "CFG-MSGOUT-NMEA_ID_GGA_USB": (0x209100BD, U1),
    "CFG-MSGOUT-NMEA_ID_GLL_I2C": (0x209100C9, U1),
    "CFG-MSGOUT-NMEA_ID_GLL_SPI": (0x209100CD, U1),
    "CFG-MSGOUT-NMEA_ID_GLL_UART1": (0x209100CA, U1),
    "CFG-MSGOUT-NMEA_ID_GLL_UART2": (0x209100CB, U1),
    "CFG-MSGOUT-NMEA_ID_GLL_USB": (0x209100CC, U1),
    "CFG-MSGOUT-NMEA_ID_GNS_I2C": (0x209100B5, U1),
    "CFG-MSGOUT-NMEA_ID_GNS_SPI": (0x209100B9, U1),
    "CFG-MSGOUT-NMEA_ID_GNS_UART1": (0x209100B6, U1),
    "CFG-MSGOUT-NMEA_ID_GNS_UART2": (0x209100B7, U1),
    "CFG-MSGOUT-NMEA_ID_GNS_USB": (0x209100B8, U1),
    "CFG-MSGOUT-NMEA_ID_GRS_I2C": (0x209100CE, U1),
    "CFG-MSGOUT-NMEA_ID_GRS_SPI": (0x209100D2, U1),
    "CFG-MSGOUT-NMEA_ID_GRS_UART1": (0x209100CF, U1),
    "CFG-MSGOUT-NMEA_ID_GRS_UART2": (0x209100D0, U1),
    "CFG-MSGOUT-NMEA_ID_GRS_USB": (0x209100D1, U1),
    "CFG-MSGOUT-NMEA_ID_GSA_I2C": (0x209100BF, U1),
    "CFG-MSGOUT-NMEA_ID_GSA_SPI": (0x209100C3, U1),
    "CFG-MSGOUT-NMEA_ID_GSA_UART1": (0x209100C0, U1),
    "CFG-MSGOUT-NMEA_ID_GSA_UART2": (0x209100C1, U1),
    "CFG-MSGOUT-NMEA_ID_GSA_USB": (0x209100C2, U1),
    "CFG-MSGOUT-NMEA_ID_GST_I2C": (0x209100D3, U1),
    "CFG-MSGOUT-NMEA_ID_GST_SPI": (0x209100D7, U1),
    "CFG-MSGOUT-NMEA_ID_GST_UART1": (0x209100D4, U1),
    "CFG-MSGOUT-NMEA_ID_GST_UART2": (0x209100D5, U1),
    "CFG-MSGOUT-NMEA_ID_GST_USB": (0x209100D6, U1),
    "CFG-MSGOUT-NMEA_ID_GSV_I2C": (0x209100C4, U1),
    "CFG-MSGOUT-NMEA_ID_GSV_SPI": (0x209100C8, U1),
    "CFG-MSGOUT-NMEA_ID_GSV_UART1": (0x209100C5, U1),
    "CFG-MSGOUT-NMEA_ID_GSV_UART2": (0x209100C6, U1),
    "CFG-MSGOUT-NMEA_ID_GSV_USB": (0x209100C7, U1),
    "CFG-MSGOUT-NMEA_ID_RLM_I2C": (0x20910400, U1),
    "CFG-MSGOUT-NMEA_ID_RLM_SPI": (0x20910404, U1),
    "CFG-MSGOUT-NMEA_ID_RLM_UART1": (0x20910401, U1),
    "CFG-MSGOUT-NMEA_ID_RLM_UART2": (0x20910402, U1),
    "CFG-MSGOUT-NMEA_ID_RLM_USB": (0x20910403, U1),
    "CFG-MSGOUT-NMEA_ID_RMC_I2C": (0x209100AB, U1),
    "CFG-MSGOUT-NMEA_ID_RMC_SPI": (0x209100AF, U1),
    "CFG-MSGOUT-NMEA_ID_RMC_UART1": (0x209100AC, U1),
    "CFG-MSGOUT-NMEA_ID_RMC_UART2": (0x209100AD, U1),
    "CFG-MSGOUT-NMEA_ID_RMC_USB": (0x209100AE, U1),
    "CFG-MSGOUT-NMEA_ID_VLW_I2C": (0x209100E7, U1),
    "CFG-MSGOUT-NMEA_ID_VLW_SPI": (0x209100EB, U1),
    "CFG-MSGOUT-NMEA_ID_VLW_UART1": (0x209100E8, U1),
    "CFG-MSGOUT-NMEA_ID_VLW_UART2": (0x209100E9, U1),
    "CFG-MSGOUT-NMEA_ID_VLW_USB": (0x209100EA, U1),
    "CFG-MSGOUT-NMEA_ID_VTG_I2C": (0x209100B0, U1),
    "CFG-MSGOUT-NMEA_ID_VTG_SPI": (0x209100B4, U1),
    "CFG-MSGOUT-NMEA_ID_VTG_UART1": (0x209100B1, U1),
    "CFG-MSGOUT-NMEA_ID_VTG_UART2": (0x209100B2, U1),
    "CFG-MSGOUT-NMEA_ID_VTG_USB": (0x209100B3, U1),
    "CFG-MSGOUT-NMEA_ID_ZDA_I2C": (0x209100D8, U1),
    "CFG-MSGOUT-NMEA_ID_ZDA_SPI": (0x209100DC, U1),
    "CFG-MSGOUT-NMEA_ID_ZDA_UART1": (0x209100D9, U1),
    "CFG-MSGOUT-NMEA_ID_ZDA_UART2": (0x209100DA, U1),
    "CFG-MSGOUT-NMEA_ID_ZDA_USB": (0x209100DB, U1),
    "CFG-MSGOUT-PUBX_ID_POLYP_I2C": (0x209100EC, U1),
    "CFG-MSGOUT-PUBX_ID_POLYP_SPI": (0x209100F0, U1),
    "CFG-MSGOUT-PUBX_ID_POLYP_UART1": (0x209100ED, U1),
    "CFG-MSGOUT-PUBX_ID_POLYP_UART2": (0x209100EE, U1),
    "CFG-MSGOUT-PUBX_ID_POLYP_USB": (0x209100EF, U1),
    "CFG-MSGOUT-PUBX_ID_POLYS_I2C": (0x209100F1, U1),
    "CFG-MSGOUT-PUBX_ID_POLYS_SPI": (0x209100F5, U1),
    "CFG-MSGOUT-PUBX_ID_POLYS_UART1": (0x209100F2, U1),
    "CFG-MSGOUT-PUBX_ID_POLYS_UART2": (0x209100F3, U1),
    "CFG-MSGOUT-PUBX_ID_POLYS_USB": (0x209100F4, U1),
    "CFG-MSGOUT-PUBX_ID_POLYT_I2C": (0x209100F6, U1),
    "CFG-MSGOUT-PUBX_ID_POLYT_SPI": (0x209100FA, U1),
    "CFG-MSGOUT-PUBX_ID_POLYT_UART1": (0x209100F7, U1),
    "CFG-MSGOUT-PUBX_ID_POLYT_UART2": (0x209100F8, U1),
    "CFG-MSGOUT-PUBX_ID_POLYT_USB": (0x209100F9, U1),
    "CFG-MSGOUT-UBX_LOG_INFO_I2C": (0x20910259, U1),
    "CFG-MSGOUT-UBX_LOG_INFO_SPI": (0x2091025D, U1),
    "CFG-MSGOUT-UBX_LOG_INFO_UART1": (0x2091025A, U1),
    "CFG-MSGOUT-UBX_LOG_INFO_UART2": (0x2091025B, U1),
    "CFG-MSGOUT-UBX_LOG_INFO_USB": (0x2091025C, U1),
    "CFG-MSGOUT-UBX_MON_COMMS_I2C": (0x2091034F, U1),
    "CFG-MSGOUT-UBX_MON_COMMS_SPI": (0x20910353, U1),
    "CFG-MSGOUT-UBX_MON_COMMS_UART1": (0x20910350, U1),
    "CFG-MSGOUT-UBX_MON_COMMS_UART2": (0x20910351, U1),
    "CFG-MSGOUT-UBX_MON_COMMS_USB": (0x20910352, U1),
    "CFG-MSGOUT-UBX_MON_HW2_I2C": (0x209101B9, U1),
    "CFG-MSGOUT-UBX_MON_HW2_SPI": (0x209101BD, U1),
    "CFG-MSGOUT-UBX_MON_HW2_UART1": (0x209101BA, U1),
    "CFG-MSGOUT-UBX_MON_HW2_UART2": (0x209101BB, U1),
    "CFG-MSGOUT-UBX_MON_HW2_USB": (0x209101BC, U1),
    "CFG-MSGOUT-UBX_MON_HW3_I2C": (0x20910354, U1),
    "CFG-MSGOUT-UBX_MON_HW3_SPI": (0x20910358, U1),
    "CFG-MSGOUT-UBX_MON_HW3_UART1": (0x20910355, U1),
    "CFG-MSGOUT-UBX_MON_HW3_UART2": (0x20910356, U1),
    "CFG-MSGOUT-UBX_MON_HW3_USB": (0x20910357, U1),
    "CFG-MSGOUT-UBX_MON_HW_I2C": (0x209101B4, U1),
    "CFG-MSGOUT-UBX_MON_HW_SPI": (0x209101B8, U1),
    "CFG-MSGOUT-UBX_MON_HW_UART1": (0x209101B5, U1),
    "CFG-MSGOUT-UBX_MON_HW_UART2": (0x209101B6, U1),
    "CFG-MSGOUT-UBX_MON_HW_USB": (0x209101B7, U1),
    "CFG-MSGOUT-UBX_MON_IO_I2C": (0x209101A5, U1),
    "CFG-MSGOUT-UBX_MON_IO_SPI": (0x209101A9, U1),
    "CFG-MSGOUT-UBX_MON_IO_UART1": (0x209101A6, U1),
    "CFG-MSGOUT-UBX_MON_IO_UART2": (0x209101A7, U1),
    "CFG-MSGOUT-UBX_MON_IO_USB": (0x209101A8, U1),
    "CFG-MSGOUT-UBX_MON_MSGPP_I2C": (0x20910196, U1),
    "CFG-MSGOUT-UBX_MON_MSGPP_SPI": (0x2091019A, U1),
    "CFG-MSGOUT-UBX_MON_MSGPP_UART1": (0x20910197, U1),
    "CFG-MSGOUT-UBX_MON_MSGPP_UART2": (0x20910198, U1),
    "CFG-MSGOUT-UBX_MON_MSGPP_USB": (0x20910199, U1),
    "CFG-MSGOUT-UBX_MON_RF_I2C": (0x20910359, U1),
    "CFG-MSGOUT-UBX_MON_RF_SPI": (0x2091035D, U1),
    "CFG-MSGOUT-UBX_MON_RF_UART1": (0x2091035A, U1),
    "CFG-MSGOUT-UBX_MON_RF_UART2": (0x2091035B, U1),
    "CFG-MSGOUT-UBX_MON_RF_USB": (0x2091035C, U1),
    "CFG-MSGOUT-UBX_MON_RXBUF_I2C": (0x209101A0, U1),
    "CFG-MSGOUT-UBX_MON_RXBUF_SPI": (0x209101A4, U1),
    "CFG-MSGOUT-UBX_MON_RXBUF_UART1": (0x209101A1, U1),
    "CFG-MSGOUT-UBX_MON_RXBUF_UART2": (0x209101A2, U1),
    "CFG-MSGOUT-UBX_MON_RXBUF_USB": (0x209101A3, U1),
    "CFG-MSGOUT-UBX_MON_RXR_I2C": (0x20910187, U1),
    "CFG-MSGOUT-UBX_MON_RXR_SPI": (0x2091018B, U1),
    "CFG-MSGOUT-UBX_MON_RXR_UART1": (0x20910188, U1),
    "CFG-MSGOUT-UBX_MON_RXR_UART2": (0x20910189, U1),
    "CFG-MSGOUT-UBX_MON_RXR_USB": (0x2091018A, U1),
    "CFG-MSGOUT-UBX_MON_SPAN_I2C": (0x2091038B, U1),
    "CFG-MSGOUT-UBX_MON_SPAN_SPI": (0x2091038F, U1),
    "CFG-MSGOUT-UBX_MON_SPAN_UART1": (0x2091038C, U1),
    "CFG-MSGOUT-UBX_MON_SPAN_UART2": (0x2091038D, U1),
    "CFG-MSGOUT-UBX_MON_SPAN_USB": (0x2091038E, U1),
    "CFG-MSGOUT-UBX_MON_TXBUF_I2C": (0x2091019B, U1),
    "CFG-MSGOUT-UBX_MON_TXBUF_SPI": (0x2091019F, U1),
    "CFG-MSGOUT-UBX_MON_TXBUF_UART1": (0x2091019C, U1),
    "CFG-MSGOUT-UBX_MON_TXBUF_UART2": (0x2091019D, U1),
    "CFG-MSGOUT-UBX_MON_TXBUF_USB": (0x2091019E, U1),
    "CFG-MSGOUT-UBX_NAV_AOPSTATUS_I2C": (0x20910079, U1),
    "CFG-MSGOUT-UBX_NAV_AOPSTATUS_SPI": (0x2091007D, U1),
    "CFG-MSGOUT-UBX_NAV_AOPSTATUS_UART1": (0x2091007A, U1),
    "CFG-MSGOUT-UBX_NAV_AOPSTATUS_UART2": (0x2091007B, U1),
    "CFG-MSGOUT-UBX_NAV_AOPSTATUS_USB": (0x2091007C, U1),
    "CFG-MSGOUT-UBX_NAV_CLOCK_I2C": (0x20910065, U1),
    "CFG-MSGOUT-UBX_NAV_CLOCK_SPI": (0x20910069, U1),
    "CFG-MSGOUT-UBX_NAV_CLOCK_UART1": (0x20910066, U1),
    "CFG-MSGOUT-UBX_NAV_CLOCK_UART2": (0x20910067, U1),
    "CFG-MSGOUT-UBX_NAV_CLOCK_USB": (0x20910068, U1),
    "CFG-MSGOUT-UBX_NAV_COV_I2C": (0x20910083, U1),
    "CFG-MSGOUT-UBX_NAV_COV_SPI": (0x20910087, U1),
    "CFG-MSGOUT-UBX_NAV_COV_UART1": (0x20910084, U1),
    "CFG-MSGOUT-UBX_NAV_COV_UART2": (0x20910085, U1),
    "CFG-MSGOUT-UBX_NAV_COV_USB": (0x20910086, U1),
    "CFG-MSGOUT-UBX_NAV_DOP_I2C": (0x20910038, U1),
    "CFG-MSGOUT-UBX_NAV_DOP_SPI": (0x2091003C, U1),
    "CFG-MSGOUT-UBX_NAV_DOP_UART1": (0x20910039, U1),
    "CFG-MSGOUT-UBX_NAV_DOP_UART2": (0x2091003A, U1),
    "CFG-MSGOUT-UBX_NAV_DOP_USB": (0x2091003B, U1),
    "CFG-MSGOUT-UBX_NAV_EOE_I2C": (0x2091015F, U1),
    "CFG-MSGOUT-UBX_NAV_EOE_SPI": (0x20910163, U1),
    "CFG-MSGOUT-UBX_NAV_EOE_UART1": (0x20910160, U1),
    "CFG-MSGOUT-UBX_NAV_EOE_UART2": (0x20910161, U1),
    "CFG-MSGOUT-UBX_NAV_EOE_USB": (0x20910162, U1),
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_I2C": (0x209100A1, U1),
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_SPI": (0x209100A5, U1),
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_UART1": (0x209100A2, U1),
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_UART2": (0x209100A3, U1),
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_USB": (0x209100A4, U1),
    "CFG-MSGOUT-UBX_NAV_ODO_I2C": (0x2091007E, U1),
    "CFG-MSGOUT-UBX_NAV_ODO_SPI": (0x20910082, U1),
    "CFG-MSGOUT-UBX_NAV_ODO_UART1": (0x2091007F, U1),
    "CFG-MSGOUT-UBX_NAV_ODO_UART2": (0x20910080, U1),
    "CFG-MSGOUT-UBX_NAV_ODO_USB": (0x20910081, U1),
    "CFG-MSGOUT-UBX_NAV_ORB_I2C": (0x20910010, U1),
    "CFG-MSGOUT-UBX_NAV_ORB_SPI": (0x20910014, U1),
    "CFG-MSGOUT-UBX_NAV_ORB_UART1": (0x20910011, U1),
    "CFG-MSGOUT-UBX_NAV_ORB_UART2": (0x20910012, U1),
    "CFG-MSGOUT-UBX_NAV_ORB_USB": (0x20910013, U1),
    "CFG-MSGOUT-UBX_NAV_POSECEF_I2C": (0x20910024, U1),
    "CFG-MSGOUT-UBX_NAV_POSECEF_SPI": (0x20910028, U1),
    "CFG-MSGOUT-UBX_NAV_POSECEF_UART1": (0x20910025, U1),
    "CFG-MSGOUT-UBX_NAV_POSECEF_UART2": (0x20910026, U1),
    "CFG-MSGOUT-UBX_NAV_POSECEF_USB": (0x20910027, U1),
    "CFG-MSGOUT-UBX_NAV_POSLLH_I2C": (0x20910029, U1),
    "CFG-MSGOUT-UBX_NAV_POSLLH_SPI": (0x2091002D, U1),
    "CFG-MSGOUT-UBX_NAV_POSLLH_UART1": (0x2091002A, U1),
    "CFG-MSGOUT-UBX_NAV_POSLLH_UART2": (0x2091002B, U1),
    "CFG-MSGOUT-UBX_NAV_POSLLH_USB": (0x2091002C, U1),
    "CFG-MSGOUT-UBX_NAV_PVT_I2C": (0x20910006, U1),
    "CFG-MSGOUT-UBX_NAV_PVT_SPI": (0x2091000A, U1),
    "CFG-MSGOUT-UBX_NAV_PVT_UART1": (0x20910007, U1),
    "CFG-MSGOUT-UBX_NAV_PVT_UART2": (0x20910008, U1),
    "CFG-MSGOUT-UBX_NAV_PVT_USB": (0x20910009, U1),
    "CFG-MSGOUT-UBX_NAV_SAT_I2C": (0x20910015, U1),
    "CFG-MSGOUT-UBX_NAV_SAT_SPI": (0x20910019, U1),
    "CFG-MSGOUT-UBX_NAV_SAT_UART1": (0x20910016, U1),
    "CFG-MSGOUT-UBX_NAV_SAT_UART2": (0x20910017, U1),
    "CFG-MSGOUT-UBX_NAV_SAT_USB": (0x20910018, U1),
    "CFG-MSGOUT-UBX_NAV_SBAS_I2C": (0x2091006A, U1),
    "CFG-MSGOUT-UBX_NAV_SBAS_SPI": (0x2091006E, U1),
    "CFG-MSGOUT-UBX_NAV_SBAS_UART1": (0x2091006B, U1),
    "CFG-MSGOUT-UBX_NAV_SBAS_UART2": (0x2091006C, U1),
    "CFG-MSGOUT-UBX_NAV_SBAS_USB": (0x2091006D, U1),
    "CFG-MSGOUT-UBX_NAV_SIG_I2C": (0x20910345, U1),
    "CFG-MSGOUT-UBX_NAV_SIG_SPI": (0x20910349, U1),
    "CFG-MSGOUT-UBX_NAV_SIG_UART1": (0x20910346, U1),
    "CFG-MSGOUT-UBX_NAV_SIG_UART2": (0x20910347, U1),
    "CFG-MSGOUT-UBX_NAV_SIG_USB": (0x20910348, U1),
    "CFG-MSGOUT-UBX_NAV_SLAS_I2C": (0x20910336, U1),
    "CFG-MSGOUT-UBX_NAV_SLAS_SPI": (0x2091033A, U1),
    "CFG-MSGOUT-UBX_NAV_SLAS_UART1": (0x20910337, U1),
    "CFG-MSGOUT-UBX_NAV_SLAS_UART2": (0x20910338, U1),
    "CFG-MSGOUT-UBX_NAV_SLAS_USB": (0x20910339, U1),
    "CFG-MSGOUT-UBX_NAV_STATUS_I2C": (0x2091001A, U1),
    "CFG-MSGOUT-UBX_NAV_STATUS_SPI": (0x2091001E, U1),
    "CFG-MSGOUT-UBX_NAV_STATUS_UART1": (0x2091001B, U1),
    "CFG-MSGOUT-UBX_NAV_STATUS_UART2": (0x2091001C, U1),
    "CFG-MSGOUT-UBX_NAV_STATUS_USB": (0x2091001D, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_I2C": (0x20910051, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_SPI": (0x20910055, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_UART1": (0x20910052, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_UART2": (0x20910053, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_USB": (0x20910054, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_I2C": (0x20910056, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_SPI": (0x2091005A, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_UART1": (0x20910057, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_UART2": (0x20910058, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_USB": (0x20910059, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_I2C": (0x2091004C, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_SPI": (0x20910050, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_UART1": (0x2091004D, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_UART2": (0x2091004E, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_USB": (0x2091004F, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_I2C": (0x20910047, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_SPI": (0x2091004B, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_UART1": (0x20910048, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_UART2": (0x20910049, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_USB": (0x2091004A, U1),
    "CFG-MSGOUT-UBX_NAV_TIMELS_I2C": (0x20910060, U1),
    "CFG-MSGOUT-UBX_NAV_TIMELS_SPI": (0x20910064, U1),
    "CFG-MSGOUT-UBX_NAV_TIMELS_UART1": (0x20910061, U1),
    "CFG-MSGOUT-UBX_NAV_TIMELS_UART2": (0x20910062, U1),
    "CFG-MSGOUT-UBX_NAV_TIMELS_USB": (0x20910063, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_I2C": (0x20910386, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_SPI": (0x2091038A, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_UART1": (0x20910387, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_UART2": (0x20910388, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_USB": (0x20910389, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_I2C": (0x2091005B, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_SPI": (0x2091005F, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_UART1": (0x2091005C, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_UART2": (0x2091005D, U1),
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_USB": (0x2091005E, U1),
    "CFG-MSGOUT-UBX_NAV_VELECEF_I2C": (0x2091003D, U1),
    "CFG-MSGOUT-UBX_NAV_VELECEF_SPI": (0x20910041, U1),
    "CFG-MSGOUT-UBX_NAV_VELECEF_UART1": (0x2091003E, U1),
    "CFG-MSGOUT-UBX_NAV_VELECEF_UART2": (0x2091003F, U1),
    "CFG-MSGOUT-UBX_NAV_VELECEF_USB": (0x20910040, U1),
    "CFG-MSGOUT-UBX_NAV_VELNED_I2C": (0x20910042, U1),
    "CFG-MSGOUT-UBX_NAV_VELNED_SPI": (0x20910046, U1),
    "CFG-MSGOUT-UBX_NAV_VELNED_UART1": (0x20910043, U1),
    "CFG-MSGOUT-UBX_NAV_VELNED_UART2": (0x20910044, U1),
    "CFG-MSGOUT-UBX_NAV_VELNED_USB": (0x20910045, U1),
    "CFG-MSGOUT-UBX_RXM_MEASX_I2C": (0x20910204, U1),
    "CFG-MSGOUT-UBX_RXM_MEASX_SPI": (0x20910208, U1),
    "CFG-MSGOUT-UBX_RXM_MEASX_UART1": (0x20910205, U1),
    "CFG-MSGOUT-UBX_RXM_MEASX_UART2": (0x20910206, U1),
    "CFG-MSGOUT-UBX_RXM_MEASX_USB": (0x20910207, U1),
    "CFG-MSGOUT-UBX_RXM_RAWX_I2C": (0x209102A4, U1),
    "CFG-MSGOUT-UBX_RXM_RAWX_SPI": (0x209102A8, U1),
    "CFG-MSGOUT-UBX_RXM_RAWX_UART1": (0x209102A5, U1),
    "CFG-MSGOUT-UBX_RXM_RAWX_UART2": (0x209102A6, U1),
    "CFG-MSGOUT-UBX_RXM_RAWX_USB": (0x209102A7, U1),
    "CFG-MSGOUT-UBX_RXM_RLM_I2C": (0x2091025E, U1),
    "CFG-MSGOUT-UBX_RXM_RLM_SPI": (0x20910262, U1),
    "CFG-MSGOUT-UBX_RXM_RLM_UART1": (0x2091025F, U1),
    "CFG-MSGOUT-UBX_RXM_RLM_UART2": (0x20910260, U1),
    "CFG-MSGOUT-UBX_RXM_RLM_USB": (0x20910261, U1),
    "CFG-MSGOUT-UBX_RXM_RTCM_I2C": (0x20910268, U1),
    "CFG-MSGOUT-UBX_RXM_RTCM_SPI": (0x2091026C, U1),
    "CFG-MSGOUT-UBX_RXM_RTCM_UART1": (0x20910269, U1),
    "CFG-MSGOUT-UBX_RXM_RTCM_UART2": (0x2091026A, U1),
    "CFG-MSGOUT-UBX_RXM_RTCM_USB": (0x2091026B, U1),
    "CFG-MSGOUT-UBX_RXM_SFRBX_I2C": (0x20910231, U1),
    "CFG-MSGOUT-UBX_RXM_SFRBX_SPI": (0x20910235, U1),
    "CFG-MSGOUT-UBX_RXM_SFRBX_UART1": (0x20910232, U1),
    "CFG-MSGOUT-UBX_RXM_SFRBX_UART2": (0x20910233, U1),
    "CFG-MSGOUT-UBX_RXM_SFRBX_USB": (0x20910234, U1),
    "CFG-MSGOUT-UBX_TIM_TM2_I2C": (0x20910178, U1),
    "CFG-MSGOUT-UBX_TIM_TM2_SPI": (0x2091017C, U1),
    "CFG-MSGOUT-UBX_TIM_TM2_UART1": (0x20910179, U1),
    "CFG-MSGOUT-UBX_TIM_TM2_UART2": (0x2091017A, U1),
    "CFG-MSGOUT-UBX_TIM_TM2_USB": (0x2091017B, U1),
    "CFG-MSGOUT-UBX_TIM_TP_I2C": (0x2091017D, U1),
    "CFG-MSGOUT-UBX_TIM_TP_SPI": (0x20910181, U1),
    "CFG-MSGOUT-UBX_TIM_TP_UART1": (0x2091017E, U1),
    "CFG-MSGOUT-UBX_TIM_TP_UART2": (0x2091017F, U1),
    "CFG-MSGOUT-UBX_TIM_TP_USB": (0x20910180, U1),
    "CFG-MSGOUT-UBX_TIM_VRFY_I2C": (0x20910092, U1),
    "CFG-MSGOUT-UBX_TIM_VRFY_SPI": (0x20910096, U1),
    "CFG-MSGOUT-UBX_TIM_VRFY_UART1": (0x20910093, U1),
    "CFG-MSGOUT-UBX_TIM_VRFY_UART2": (0x20910094, U1),
    "CFG-MSGOUT-UBX_TIM_VRFY_USB": (0x20910095, U1),
    # CFG-NAVSPG Standard precision navigation configuration
    "CFG-NAVSPG-FIXMODE": (0x20110011, E1),
    "CFG-NAVSPG-INIFIX3D": (0x10110013, L),
    "CFG-NAVSPG-WKNROLLOVER": (0x30110017, U2),
    "CFG-NAVSPG-USE_PPP": (0x10110019, L),
    "CFG-NAVSPG-UTCSTANDARD": (0x2011001C, E1),
    "CFG-NAVSPG-DYNMODEL": (0x20110021, E1),
    "CFG-NAVSPG-ACKAIDING": (0x10110025, L),
    "CFG-NAVSPG-USE_USRDAT": (0x10110061, L),
    "CFG-NAVSPG-USRDAT_MAJA": (0x50110062, R8),
    "CFG-NAVSPG-USRDAT_FLAT": (0x50110063, R8),
    "CFG-NAVSPG-USRDAT_DX": (0x40110064, R4),
    "CFG-NAVSPG-USRDAT_DY": (0x40110065, R4),
    "CFG-NAVSPG-USRDAT_DZ": (0x40110066, R4),
    "CFG-NAVSPG-USRDAT_ROTX": (0x40110067, R4),
    "CFG-NAVSPG-USRDAT_ROTY": (0x40110068, R4),
    "CFG-NAVSPG-USRDAT_ROTZ": (0x40110069, R4),
    "CFG-NAVSPG-USRDAT_SCALE": (0x4011006A, R4),
    "CFG-NAVSPG-INFIL_MINSVS": (0x201100A1, U1),
    "CFG-NAVSPG-INFIL_MAXSVS": (0x201100A2, U1),
    "CFG-NAVSPG-INFIL_MINCNO": (0x201100A3, U1),
    "CFG-NAVSPG-INFIL_MINELEV": (0x201100A4, I1),
    "CFG-NAVSPG-INFIL_NCNOTHRS": (0x201100AA, U1),
    "CFG-NAVSPG-INFIL_CNOTHRS": (0x201100AB, U1),
    "CFG-NAVSPG-OUTFIL_PDOP": (0x301100B1, U2),
    "CFG-NAVSPG-OUTFIL_TDOP": (0x301100B2, U2),
    "CFG-NAVSPG-OUTFIL_PACC": (0x301100B3, U2),
    "CFG-NAVSPG-OUTFIL_TACC": (0x301100B4, U2),
    "CFG-NAVSPG-OUTFIL_FACC": (0x301100B5, U2),
    "CFG-NAVSPG-CONSTR_ALT": (0x401100C1, I4),
    "CFG-NAVSPG-CONSTR_ALTVAR": (0x401100C2, U4),
    "CFG-NAVSPG-CONSTR_DGNSSTO": (0x201100C4, U1),
    "CFG-NAVSPG-SIGATTCOMP": (0x201100D6, E1),
    # CFG-NMEA NMEA protocol configuration
    "CFG-NMEA-PROTVER": (0x20930001, E1),
    "CFG-NMEA-MAXSVS": (0x20930002, E1),
    "CFG-NMEA-COMPAT": (0x10930003, L),
    "CFG-NMEA-CONSIDER": (0x10930004, L),
    "CFG-NMEA-LIMIT82": (0x10930005, L),
    "CFG-NMEA-HIGHPREC": (0x10930006, L),
    "CFG-NMEA-SVNUMBERING": (0x20930007, E1),
    "CFG-NMEA-FILT_GPS": (0x10930011, L),
    "CFG-NMEA-FILT_SBAS": (0x10930012, L),
    "CFG-NMEA-FILT_GAL": (0x10930013, L),
    "CFG-NMEA-FILT_QZSS": (0x10930015, L),
    "CFG-NMEA-FILT_GLO": (0x10930016, L),
    "CFG-NMEA-FILT_BDS": (0x10930017, L),
    "CFG-NMEA-OUT_INVFIX": (0x10930021, L),
    "CFG-NMEA-OUT_MSKFIX": (0x10930022, L),
    "CFG-NMEA-OUT_INVTIME": (0x10930023, L),
    "CFG-NMEA-OUT_INVDATE": (0x10930024, L),
    "CFG-NMEA-OUT_ONLYGPS": (0x10930025, L),
    "CFG-NMEA-OUT_FROZENCOG": (0x10930026, L),
    "CFG-NMEA-MAINTALKERID": (0x20930031, E1),
    "CFG-NMEA-GSVTALKERID": (0x20930032, E1),
    "CFG-NMEA-BDSTALKERID": (0x30930033, U2),
    # CFG-ODO Odometer and low-speed course over ground filter configuration
    "CFG-ODO-USE_ODO": (0x10220001, L),
    "CFG-ODO-USE_COG": (0x10220002, L),
    "CFG-ODO-OUTLPVEL": (0x10220003, L),
    "CFG-ODO-OUTLPCOG": (0x10220004, L),
    "CFG-ODO-PROFILE": (0x20220005, E1),
    "CFG-ODO-COGMAXSPEED": (0x20220021, U1),
    "CFG-ODO-COGMAXPOSACC": (0x20220022, U1),
    "CFG-ODO-VELLPGAIN": (0x20220031, U1),
    "CFG-ODO-COGLPGAIN": (0x20220032, U1),
    # CFG-PM Configuration for receiver power management
    "CFG-PM-OPERATEMODE": (0x20D00001, E1),
    "CFG-PM-POSUPDATEPERIOD": (0x40D00002, U4),
    "CFG-PM-ACQPERIOD": (0x40D00003, U4),
    "CFG-PM-GRIDOFFSET": (0x40D00004, U4),
    "CFG-PM-ONTIME": (0x30D00005, U2),
    "CFG-PM-MINACQTIME": (0x20D00006, U1),
    "CFG-PM-MAXACQTIME": (0x20D00007, U1),
    "CFG-PM-DONOTENTEROFF": (0x10D00008, L),
    "CFG-PM-WAITTIMEFIX": (0x10D00009, L),
    "CFG-PM-UPDATEEPH": (0x10D0000A, L),
    "CFG-PM-EXTINTSEL": (0x20D0000B, E1),
    "CFG-PM-EXTINTWAKE": (0x10D0000C, L),
    "CFG-PM-EXTINTBACKUP": (0x10D0000D, L),
    "CFG-PM-EXTINTINACTIVE": (0x10D0000E, L),
    "CFG-PM-EXTINTINACTIVITY": (0x40D0000F, U4),
    "CFG-PM-LIMITPEAKCURR": (0x10D00010, L),
    # CFG-QZSS QZSS system configuration
    "CFG-QZSS-USE_SLAS_DGNSS": (0x10370005, L),
    "CFG-QZSS-USE_SLAS_TESTMODE": (0x10370006, L),
    "CFG-QZSS-USE_SLAS_RAIM_UNCORR": (0x10370007, L),
    # CFG-RATE Navigation and measurement rate configuration
    "CFG-RATE-MEAS": (0x30210001, U2),
    "CFG-RATE-NAV": (0x30210002, U2),
    "CFG-RATE-TIMEREF": (0x20210003, E1),
    # CFG-RINV Remote inventory
    "CFG-RINV-DUMP": (0x10C70001, L),
    "CFG-RINV-BINARY": (0x10C70002, L),
    "CFG-RINV-DATA_SIZE": (0x20C70003, U1),
    "CFG-RINV-CHUNK0": (0x50C70004, X8),
    "CFG-RINV-CHUNK1": (0x50C70005, X8),
    "CFG-RINV-CHUNK2": (0x50C70006, X8),
    "CFG-RINV-CHUNK3": (0x50C70007, X8),
    # CFG-SBAS SBAS configuration
    "CFG-SBAS-USE_TESTMODE": (0x10360002, L),
    "CFG-SBAS-USE_RANGING": (0x10360003, L),
    "CFG-SBAS-USE_DIFFCORR": (0x10360004, L),
    "CFG-SBAS-USE_INTEGRITY": (0x10360005, L),
    "CFG-SBAS-PRNSCANMASK": (0x50360006, X8),
    # CFG-SEC Security configuration
    "CFG-SEC-CFG_LOCK": (0x10F60009, L),
    "CFG-SEC-CFG_LOCK_UNLOCKGRP1": (0x30F6000A, U2),
    "CFG-SEC-CFG_LOCK_UNLOCKGRP2": (0x30F6000B, U2),
    # CFG-SIGNAL Satellite systems (GNSS) signal configuration
    "CFG-SIGNAL-GPS_ENA": (0x1031001F, L),
    "CFG-SIGNAL-GPS_L1CA_ENA": (0x10310001, L),
    "CFG-SIGNAL-SBAS_ENA": (0x10310020, L),
    "CFG-SIGNAL-SBAS_L1CA_ENA": (0x10310005, L),
    "CFG-SIGNAL-GAL_ENA": (0x10310021, L),
    "CFG-SIGNAL-GAL_E1_ENA": (0x10310007, L),
    "CFG-SIGNAL-BDS_ENA": (0x10310022, L),
    "CFG-SIGNAL-BDS_B1_ENA": (0x1031000D, L),
    "CFG-SIGNAL-QZSS_ENA": (0x10310024, L),
    "CFG-SIGNAL-QZSS_L1CA_ENA": (0x10310012, L),
    "CFG-SIGNAL-GLO_ENA": (0x10310025, L),
    "CFG-SIGNAL-GLO_L1_ENA": (0x10310018, L),
    # CFG-SPI Configuration of the SPI interface
    "CFG-SPI-MAXFF": (0x20640001, U1),
    "CFG-SPI-CPOLARITY": (0x10640002, L),
    "CFG-SPI-CPHASE": (0x10640003, L),
    "CFG-SPI-EXTENDEDTIMEOUT": (0x10640005, L),
    "CFG-SPI-ENABLED": (0x10640006, L),
    # CFG-SPIINPROT Input protocol configuration of the SPI interface
    "CFG-SPIINPROT-UBX": (0x10790001, L),
    "CFG-SPIINPROT-NMEA": (0x10790002, L),
    "CFG-SPIINPROT-RTCM3X": (0x10790004, L),
    # CFG-SPIOUTPROT Output protocol configuration of the SPI interface
    "CFG-SPIOUTPROT-UBX": (0x107A0001, L),
    "CFG-SPIOUTPROT-NMEA": (0x107A0002, L),
    # CFG-TP Timepulse configuration
    "CFG-TP-PULSE_DEF": (0x20050023, E1),
    "CFG-TP-PULSE_LENGTH_DEF": (0x20050030, E1),
    "CFG-TP-ANT_CABLEDELAY": (0x30050001, I2),
    "CFG-TP-PERIOD_TP1": (0x40050002, U4),
    "CFG-TP-PERIOD_LOCK_TP1": (0x40050003, U4),
    "CFG-TP-FREQ_TP1": (0x40050024, U4),
    "CFG-TP-FREQ_LOCK_TP1": (0x40050025, U4),
    "CFG-TP-LEN_TP1": (0x40050004, U4),
    "CFG-TP-LEN_LOCK_TP1": (0x40050005, U4),
    "CFG-TP-DUTY_TP1": (0x5005002A, R8),
    "CFG-TP-DUTY_LOCK_TP1": (0x5005002B, R8),
    "CFG-TP-USER_DELAY_TP1": (0x40050006, I4),
    "CFG-TP-TP1_ENA": (0x10050007, L),
    "CFG-TP-SYNC_GNSS_TP1": (0x10050008, L),
    "CFG-TP-USE_LOCKED_TP1": (0x10050009, L),
    "CFG-TP-ALIGN_TO_TOW_TP1": (0x1005000A, L),
    "CFG-TP-POL_TP1": (0x1005000B, L),
    "CFG-TP-TIMEGRID_TP1": (0x2005000C, E1),
    "CFG-TP-PERIOD_TP2": (0x4005000D, U4),
    "CFG-TP-PERIOD_LOCK_TP2": (0x4005000E, U4),
    "CFG-TP-FREQ_TP2": (0x40050026, U4),
    "CFG-TP-FREQ_LOCK_TP2": (0x40050027, U4),
    "CFG-TP-LEN_TP2": (0x4005000F, U4),
    "CFG-TP-LEN_LOCK_TP2": (0x40050010, U4),
    "CFG-TP-DUTY_TP2": (0x5005002C, R8),
    "CFG-TP-DUTY_LOCK_TP2": (0x5005002D, R8),
    "CFG-TP-USER_DELAY_TP2": (0x40050011, I4),
    "CFG-TP-TP2_ENA": (0x10050012, L),
    "CFG-TP-SYNC_GNSS_TP2": (0x10050013, L),
    "CFG-TP-USE_LOCKED_TP2": (0x10050014, L),
    "CFG-TP-ALIGN_TO_TOW_TP2": (0x10050015, L),
    "CFG-TP-POL_TP2": (0x10050016, L),
    "CFG-TP-TIMEGRID_TP2": (0x20050017, E1),
    # CFG-TXREADY TX ready configuration
    "CFG-TXREADY-ENABLED": (0x10A20001, L),
    "CFG-TXREADY-POLARITY": (0x10A20002, L),
    "CFG-TXREADY-PIN": (0x20A20003, U1),
    "CFG-TXREADY-THRESHOLD": (0x30A20004, U2),
    "CFG-TXREADY-INTERFACE": (0x20A20005, E1),
    # CFG-UART1 Configuration of the UART1 interface
    "CFG-UART1-BAUDRATE": (0x40520001, U4),
    "CFG-UART1-STOPBITS": (0x20520002, E1),
    "CFG-UART1-DATABITS": (0x20520003, E1),
    "CFG-UART1-PARITY": (0x20520004, E1),
    "CFG-UART1-ENABLED": (0x10520005, L),
    # CFG-UART1INPROT Input protocol configuration of the UART1 interface
    "CFG-UART1INPROT-UBX": (0x10730001, L),
    "CFG-UART1INPROT-NMEA": (0x10730002, L),
    "CFG-UART1INPROT-RTCM3X": (0x10730004, L),
    # CFG-UART1OUTPROT Output protocol configuration of the UART1 interface
    "CFG-UART1OUTPROT-UBX": (0x10740001, L),
    "CFG-UART1OUTPROT-NMEA": (0x10740002, L),
    # CFG-UART2 Configuration of the UART2 interface
    "CFG-UART2-BAUDRATE": (0x40530001, U4),
    "CFG-UART2-STOPBITS": (0x20530002, E1),
    "CFG-UART2-DATABITS": (0x20530003, E1),
    "CFG-UART2-PARITY": (0x20530004, E1),
    "CFG-UART2-ENABLED": (0x10530005, L),
    "CFG-UART2-REMAP": (0x10530006, L),
    # CFG-UART2INPROT Input protocol configuration of the UART2 interface
    "CFG-UART2INPROT-UBX": (0x10750001, L),
    "CFG-UART2INPROT-NMEA": (0x10750002, L),
    "CFG-UART2INPROT-RTCM3X": (0x10750004, L),
    # CFG-UART2OUTPROT Output protocol configuration of the UART2 interface
    "CFG-UART2OUTPROT-UBX": (0x10760001, L),
    "CFG-UART2OUTPROT-NMEA": (0x10760002, L),
    # CFG-USB Configuration of the USB interface
    "CFG-USB-ENABLED": (0x10650001, L),
    "CFG-USB-SELFPOW": (0x10650002, L),
    "CFG-USB-VENDOR_ID": (0x3065000A, U2),
    "CFG-USB-PRODUCT_ID": (0x3065000B, U2),
    "CFG-USB-POWER": (0x3065000C, U2),
    "CFG-USB-VENDOR_STR0": (0x5065000D, X8),
    "CFG-USB-VENDOR_STR1": (0x5065000E, X8),
    "CFG-USB-VENDOR_STR2": (0x5065000F, X8),
    "CFG-USB-VENDOR_STR3": (0x50650010, X8),
    "CFG-USB-PRODUCT_STR0": (0x50650011, X8),
    "CFG-USB-PRODUCT_STR1": (0x50650012, X8),
    "CFG-USB-PRODUCT_STR2": (0x50650013, X8),
    "CFG-USB-PRODUCT_STR3": (0x50650014, X8),
    "CFG-USB-SERIAL_NO_STR0": (0x50650015, X8),
    "CFG-USB-SERIAL_NO_STR1": (0x50650016, X8),
    "CFG-USB-SERIAL_NO_STR2": (0x50650017, X8),
    "CFG-USB-SERIAL_NO_STR3": (0x50650018, X8),
    # CFG-USBINPROT Input protocol configuration of the USB interface
    "CFG-USBINPROT-UBX": (0x10770001, L),
    "CFG-USBINPROT-NMEA": (0x10770002, L),
    "CFG-USBINPROT-RTCM3X": (0x10770004, L),
    # CFG-USBOUTPROT Output protocol configuration of the USB interface
    "CFG-USBOUTPROT-UBX": (0x10780001, L),
    "CFG-USBOUTPROT-NMEA": (0x10780002, L),
}
