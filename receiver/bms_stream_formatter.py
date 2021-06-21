  
import sys
import ast
import pandas as pd

def bms_stream_formatting():
    data = sys.stdin.readlines()
    input_data = ''

    for line in data:
        if 'temperature' in line:
            input_data = line
            
    formated_data_stream = ast.literal_eval(input_data)
    bms_dataframe = pd.DataFrame(formated_data_stream)
    if bms_dataframe.size !=0:
        bms_temperature_list = bms_dataframe['temperature'].values.tolist()
        bms_soc_list = bms_dataframe['soc'].values.tolist()
        bms_charging_rate_list = bms_dataframe['chargeRate'].values.tolist()
        return [bms_temperature_list,bms_soc_list,bms_charging_rate_list]
