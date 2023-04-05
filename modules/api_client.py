"""
api_client.py

API Client functions
"""


__author__ = ""
__version__ = "0.1.0"
__licence__ = "MIT"

# Standard Library Imports

# 3rd Party Library Imports
from requests import request

# Local Module Imports

# Global Constants

# Global Variables

# Global Initializations

# Classes

# Functions
def query_api(apiurl: str, endpoint: str, address: str) -> dict:
    """Query an API endpoint with the provided URL, endpoint, and address.

    :param apiurl: The base URL of the API to query.
    :type apiurl: str
    :param endpoint: The specific endpoint of the API to query.
    :type endpoint: str
    :param address: The address to query data for.
    :type address: str
    :return: A dictionary containing the result of the API query.
    :rtype: dict
    """
    url = apiurl + endpoint + address
    response = request('GET', url)
    return response.json()['result']

# Run