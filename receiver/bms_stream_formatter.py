  
import sys
import ast
import pandas as pd

def bms_format_console_pipeline():
    data = sys.stdin.readlines()
    input_data = ''
    
    #get the streaming data from java console output in the pipeline
    for line in data:
        if 'temperature' in line:
            input_data = line
            
    #convert bms data stream string to list of dictionaries
    formated_data_stream = ast.literal_eval(input_data)
    
    #convert the list of dictionaries to a dataframe and return bms parameter lists
    bms_dataframe = pd.DataFrame(formated_data_stream)
    if bms_dataframe.size !=0:
        bms_temperature_list = bms_dataframe['temperature'].values.tolist()
        bms_soc_list = bms_dataframe['soc'].values.tolist()
        bms_charging_rate_list = bms_dataframe['chargeRate'].values.tolist()
        return [bms_temperature_list,bms_soc_list,bms_charging_rate_list]
