import requests
import pytest
from endpoint.EndPointFactory import EndPoint


def test_books():
    response = requests.get(EndPoint.BASE_URI_API)
    print("\nStatus Code = ", response.status_code)
    print("Request URL = ", response.url)

    data = response.json()
    print(data)

    da1 = data['books'][0]['isbn']
    da2 = data['books'][0]['title']
    da3 = data['books'][0]['subTitle']
    da4 = data['books'][0]['author']
    da5 = data['books'][0]['publish_date']
    da6 = data['books'][0]['publisher']
    da7 = data['books'][0]['pages']
    da8 = data['books'][0]['description']
    da9 = data['books'][0]['website']
    print(da1)
    print(da2)
    print(da3)
    print(da4)
    print(da5)
    print(da6)
    print(da7)
    print(da8)
    print(da9)

