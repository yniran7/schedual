import json
from using_json_schema import event_text_to_json_event
from tests.utils import str_date_to_date
import datetime

test_results_filename = 'test_results.txt'

def write_to_file(text):
    with open(test_results_filename, 'a+') as f:
        f.write(text)

def prompt1(options = None):
    prompt = "meeting tomorrow at 18:00 for an hour with Tom Koren and Tal Dokhnian in the gym, we are going to talk about life"
    res = event_text_to_json_event(prompt, options)
    
    print(res)
    
    event = res["events"][0]
    
    start_date = str_date_to_date(event["start_datetime"])
    end_date = str_date_to_date(event["end_datetime"])
    
    expected_start_date = datetime.datetime.now().replace(hour=18, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
    expected_end_date = datetime.datetime.now().replace(hour=19, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
    expected_participants = set(["Tom Koren", "Tal Dokhnian"])
    expected_location = "gym"
    
    status_event_count = True if(len(res["events"]) == 1) else f'Should be 1'
    status_start_date = True if(start_date == expected_start_date) else f'Should be {expected_start_date}'
    status_end_date = True if(end_date == expected_end_date) else f'Should be {expected_end_date}'
    status_location = True if(expected_location == event["location"].lower()) else f'Should be {expected_location}'
    status_description = True if(event["description"] != '') else f'Should not be empty'
    status_participants = True if(set(event["participants"]) == expected_participants) else f'Should be {expected_participants}'
    
    
    summery = {
        "response": res,
        "status_event_count": status_event_count,
        "status_start_date": status_start_date,
        "status_end_date": status_end_date,
        "status_location": status_location,
        "status_description": status_description,
        "status_participants": status_participants,
        "options": options
    }
          
    write_to_file(json.dumps(summery, indent=2) + ',')


for i in range(1):
    options = {
        # "temperature": round(random.uniform(0,1), 2),
        # "top_p": round(random.uniform(0,0.5), 2)
    }
    
    prompt1(options)
    
    print(f'Finished round: {i}')