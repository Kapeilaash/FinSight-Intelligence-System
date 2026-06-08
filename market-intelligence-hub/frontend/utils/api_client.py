import requests

def call_backend(path: str, data: dict):
    return requests.post(path, json=data).json()
