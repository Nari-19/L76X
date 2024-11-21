import L76X
import time
import math

try:
    x = L76X.L76X()
    x.L76X_Set_Baudrate(9600)
    x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
    time.sleep(2)
    x.L76X_Set_Baudrate(115200)

    x.L76X_Send_Command(x.SET_POS_FIX_400MS)

    # Set output message
    x.L76X_Send_Command(x.SET_NMEA_OUTPUT)

    x.L76X_Exit_BackupMode()
    while True:
        x.L76X_Gat_GNRMC()
        if x.Status == 1:
            print('Already positioned')
        else:
            print('No positioning')
        
        print('Time {}:{}:{}'.format(x.Time_H, x.Time_M, x.Time_S))
        print('Lon = {}, Lat = {}'.format(x.Lon, x.Lat))
        
        x.L76X_Baidu_Coordinates(x.Lat, x.Lon)
        print('Baidu coordinate: {}, {}'.format(x.Lat_Baidu, x.Lon_Baidu))

except Exception as e:
    print("\nProgram end due to error:", e)
    exit()