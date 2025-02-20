import requests
from datetime import datetime
from config.settings import USERNAME, TOKEN
from src.frontend.gui_utils import show_error_message, show_success_message

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


def posting_pixel(quantity):
    today = datetime.now()
    today = today.strftime("%Y%m%d")
    pixel_parameters = {
        "date": today,
        "quantity": quantity
    }
    response = requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1", json=pixel_parameters, headers=headers)
    data = response.json()
    if data["message"] == "Success.":
        show_success_message()
    else:
        show_error_message()
    

def update_pixel(quantity):
    today = datetime.now()
    today = today.strftime("%Y%m%d")
    pixel_parameters = {
        "quantity": quantity
    }
    response = requests.put(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{today}", json=pixel_parameters, headers=headers)
    data = response.json()
    print(data)
    if data["message"] == "Success.":
        show_success_message()
    else:
        show_error_message()


def delete_pixel():
    today = datetime.now()
    today = today.strftime("%Y%m%d")
    response = requests.delete(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{today}", headers=headers)
    data = response.json()
    if data["message"] == "Success.":
        show_success_message()
    else:
        show_error_message()
