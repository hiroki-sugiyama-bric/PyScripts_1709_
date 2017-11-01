from datetime import datetime

def create_year_to_millisec_str(dt):
    year_to_sec_str = dt.strftime('%Y%m%d%H%M%S')
    millisec = dt.microsecond // 1000
    millisec_str = f'{millisec:03d}'

    return year_to_sec_str + millisec_str
    

