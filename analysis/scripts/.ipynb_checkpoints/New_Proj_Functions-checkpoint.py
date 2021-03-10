import pandas as pd
import numpy as np

def load_clean(path_or_url):
    # Method 1 (Load data, remove unecessary columns)
    gpu_df1 = (
        pd.read_csv(path_or_url)
        .drop(['Best_Resolution', 'Boost_Clock', 'DVI_Connection', 'Dedicated', 'DisplayPort_Connection', 'HDMI_Connection', 'Integrated', 'Open_GL', 'PSU', 'Power_Connector', 
               'ROPs', 'Resolution_WxH', 'SLI_Crossfire', 'Shader', 'VGA_Connection'], axis = 1, inplace = False)
    )
    
    gpu_df1['Core_Speed'] = gpu_df1['Core_Speed'].map(lambda x: x.lstrip('\n-'))
    gpu_df1['Release_Date'] = gpu_df1['Release_Date'].map(lambda x: x.lstrip('\n'))
    #gpu_df1['Release_Date'] = pd.to_datetime(gpu_df1)
    #gpu_df1.sort('Release_Date')
    
    # Final (Remove unnecessary string values/deal with remaining missing data)
    gpu_df_end = (
        gpu_df1
        .replace(to_replace = '-', value = np.NaN, inplace = False)
        .replace(to_replace = ' Watts', value = ' W', inplace = False)
        .fillna({'Architecture':'Unknown', 'Core_Speed':'0 MHz', 'Max_Power':'0 W', 'Memory_Bandwidth':'0GB/sec', 
                 'Pixel_Rate':'0 GPixel/s', 'Release_Price':'$0.00', 'Texture_Rate':'0 GTexel/s'}, inplace = False)
    )
    
    move_name = 'Name'
    to_first = gpu_df_end.pop(move_name)
    gpu_df_end.insert(0, move_name, to_first)
    gpu_df_end.rename({'Name': 'GPU Name', 'Memory_Speed': 'Clock Speed', 'Direct_X': 'DirectX', 'L2_Cache': 'Cache', 'Max_Power': 'Power Consumption', 'Memory_Bandwidth': 'Bandwidth', 'Memory_Bus': 'Memory Bus', 'Memory_Type': 'Memory Type', 'Pixel_Rate': 'Pixel Speed', 'Release_Date': 'Release Date', 'Release_Price': 'Release Price', 'Texture_Rate': 'Texture Rate'}, axis = 1, inplace = True)
    gpu_df_end.replace({"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}, regex = True, inplace = True)
    gpu_df_end.replace({"-": "/"}, regex = True, inplace = True)
    gpu_df_end.replace({"DX ": "", "0a": "0", "0b": "0", "0c": "0"}, regex  = True, inplace = True)
    
    return(gpu_df_end)