import requests
import pytest
from endpoint.EndPointFactory import EndPoint


def test_books():
    response = requests.get(EndPoint.BASE_URI_API)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)

    data = response.json()
    print(data)

