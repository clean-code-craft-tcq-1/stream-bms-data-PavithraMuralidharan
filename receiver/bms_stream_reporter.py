def bms_param_min(bms_param_data):
    if len(bms_param_data) !=0:
        return round(min(bms_param_data),3)
    return "Data not available"


def bms_param_max(bms_param_data):
    if len(bms_param_data) != 0:
        return round(max(bms_param_data), 3)
    return "Data not available"



def displayOutput(bms_data):
    bms_temperature_list = bms_data[0]
    bms_soc_list = bms_data[1]
    bms_chargeRate_list = bms_data[2]

    print('Max Temperature:', bms_param_max(bms_temperature_list))
    print('Min Temperature:', bms_param_min(bms_temperature_list))
    print('Moving average of last five values of temperature:', moving_average_last_5(bms_temperature_list))

    print('Max SOC:', bms_param_max(bms_soc_list))
    print('Min SOC:', bms_param_min(bms_soc_list))
    print('Moving average of last five values of chargeRate:', moving_average_last_5(bms_soc_list))

    print('Max chargeRate:', bms_param_max(bms_chargeRate_list))
    print('Min chargeRate:', bms_param_min(bms_chargeRate_list))
    print('Moving average of last five values of chargeRate:', moving_average_last_5(bms_chargeRate_list))
    return 'Success'



def moving_average_last_5(bms_param_data):
    length = len(bms_param_data)
    if length >= 5:
        moving_average = round((sum(bms_param_data[-5:])/5),3)
        return moving_average
    return "Data Insufficent"
