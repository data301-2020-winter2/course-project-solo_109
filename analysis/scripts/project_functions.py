{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_clean(path_or_url):\n",
    "    \n",
    "    # Method 1 (Load data, remove unecessary columns)\n",
    "    gpu_df1 = (\n",
    "        pd.read_csv(path_or_url)\n",
    "        .drop(['Best_Resolution', 'Boost_Clock', 'DVI_Connection', 'Dedicated', 'DisplayPort_Connection', 'HDMI_Connection', 'Integrated', 'Open_GL', 'PSU', 'Power_Connector', \n",
    "               'ROPs', 'Resolution_WxH', 'SLI_Crossfire', 'Shader', 'VGA_Connection'], axis = 1, inplace = True)\n",
    "    )\n",
    "    \n",
    "    return gpu_df1\n",
    "    # Method 2 (Remove unnecessary string values/deal with missing data)\n",
    "    gpu_df2 = (\n",
    "        gpu_df1\n",
    "        .replace(to_replace = ['\\\\n', '\\\\n-'], value = '', inplace = True)\n",
    "        .replace(to_replace = '-', value = np.NaN, inplace = True)\n",
    "        .replace(to_replace = ' Watts', value = ' W', inplace = True)\n",
    "        .fillna({'Architecture':'Unknown', 'Core_Speed':'0 MHz', 'Max_Power':'0 W', 'Memory_Bandwidth':'0GB/sec', \n",
    "                 'Pixel_Rate':'0 GPixel/s', 'Release_Price':'$0.00', 'Texture_Rate':'0 GTexel/s'}, inplace = True)\n",
    "    )\n",
    "    \n",
    "    return gpu_df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
