import requests
import datetime as dt


#-----------------------ENVIRONMENT VARIABLES--------------------------------------#
APP_ID = "<app-id>"
APP_KEY = "<app-key>"

READ_GET = "<api-url>"
WRITE_POST = "<api-url>"

#---------------------------------------------------------------------------------#
host_domain = "<domain-name>"
endpoint = "<domain-endpoint>"
url = host_domain + endpoint


header = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY
}



def call_url(activity):
    request_body = {
        "query": activity
    }
    response = requests.post(url = url, json= request_body, headers= header)
    response_data = response.json()

    time = dt.datetime.now()
    current_date = f"{time.day}/{time.month}/{time.year}"
    current_time = f"{time.hour}:{time.minute}:{time.second}"
    exercises = response_data["exercises"]

    for exercise in exercises:
        exercise_name = exercise["name"]
        exercise_duration = exercise["duration_min"]
        exercise_calories = exercise["nf_calories"]

        #make a call to google sheets API to store the data
        print(f"{exercise_name}-{exercise_duration}-{exercise_calories}")
        exercise_data_dict = {
            "workout" : {
                "date": current_date,
                "time": current_time,
                "exercise": exercise_name,
                "duration": exercise_duration,
                "calories" : exercise_calories
            }
        }
        sheet_resposne = requests.post(url=WRITE_POST, json=exercise_data_dict)
        print(sheet_resposne.text)




    
    # print(response.json())

def run_program():
    activity = input("Tell me what exercises you did? : ")
    data = call_url(activity)


run_program()