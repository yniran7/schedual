from datetime import datetime

base_date_format = '%Y-%m-%dT%H:%M:%S'
with_tz_date_format = '%Y-%m-%dT%H:%M:%S%z'

def str_date_to_date(str_date):
    dot_index = str_date.find('.')
    plus_index = str_date.find('+')
    timezone = '' if(plus_index == -1) else str_date[plus_index:]
    
    if(dot_index != -1):
        str_date = str_date[:-(len(str_date)-dot_index)]
        
    str_date += timezone
    chosen = with_tz_date_format if(len(str_date) > 19) else base_date_format
    return datetime.strptime(str_date, chosen)