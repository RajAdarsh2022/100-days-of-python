import requests

parameters = {
    "amount":10,
    "type": "boolean",
    "category": 18
}

def getQuestions():
    """Function the fetch question from the Database via API call"""
    try:
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()
        data = response.json()
        return data["results"]
    except Exception as error:
        print("An error occured in fetching data from API")
        print(error)
        return []

question_data = getQuestions()