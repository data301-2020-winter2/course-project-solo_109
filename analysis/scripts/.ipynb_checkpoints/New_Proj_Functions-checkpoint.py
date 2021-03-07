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
    
    return(gpu_df_end)