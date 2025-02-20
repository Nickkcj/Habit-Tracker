import requests
from datetime import datetime
from habit_tracker.config.settings import USERNAME, TOKEN


parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


def create_account():
    response = requests.post(url="https://pixe.la/v1/users", json=parameters)
    


def create_graph():
    graph_parameters = {
        "id": "graph1",
        "name": "Course Videos Seen",
        "unit": "videos",
        "type": "int",
        "color": "sora"
    }
    response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs", json=graph_parameters, headers=headers)
    


def posting_pixel():
    today = datetime.now()
    today = today.strftime("%Y%m%d")
    pixel_parameters = {
        "date": today,
        "quantity": "15"
    }
    response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1", json=pixel_parameters, headers=headers)
    




def update_pixel():
    today = datetime.now()
    today = today.strftime("%Y%m%d")
    pixel_parameters = {
        "quantity": "10"
    }
    response = requests.put(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{today}", json=pixel_parameters, headers=headers)
    


def delete_pixel():
    today = datetime.now()
    today = today.strftime("%Y%m%d")
    response = requests.delete(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{today}", headers=headers)
    