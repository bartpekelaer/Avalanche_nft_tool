"""
ui.py

User Interface

Functions:
jload(): Load a JSON file and return its contents as a dictionary.
jdump(): Write a Python object as a JSON-formatted string to a file.
jdumps(): Encode a Python object as a JSON-formatted string and write it to a file.
yload(): Load a YAML file and return its contents as a dictionary.
ydump(): Write a Python object as a YAML-formatted string to a file.
jloads(): Load a JSON-formatted string from a file and returns its contents as a dictionary.


"""


__author__ = ""
__version__ = "0.1.0"
__licence__ = "MIT"

# Standard Library Imports
import datetime
import json

# 3rd Party Library Imports
from mimetypes import guess_extension
from urllib.request import urlopen
from urllib.error import HTTPError
import yaml


# Local Module Imports

# Global Constants

# Global Variables

# Global Initializations

# Classes

# Functions
def jload(filename: str) -> dict:
    """Load a JSON file and return its contents as a dictionary.

    :param filename: The path of the JSON file to load.
    :type filename: str
    :return: A dictionary containing the contents of the JSON file.
    :rtype: dict
    """    
    with open(filename, 'r') as file:
        data = json.load(file)
        
        return data


def jloads(filename: str) -> dict:
    """Load a JSON-formatted string from a file and returns its contents as a dictionary.

    :param filename: The path of the file containing the JSON-formatted string.
    :type filename: str
    :return: A dictionary containing the contents of the JSON-formatted string.
    :rtype: dict
    """
    with open(filename, 'r') as file:
        data = json.loads(file)
        
        return data


def jdump(filename: str, arg) -> None:
    """Write a Python object as a JSON-formatted string to a file.

    :param filename: The path of the file to write the JSON-formatted string to.
    :type filename: str
    :param arg: The Python object to write as a JSON-Formatted string.
    :type arg: any
    :return: None
    """
    with open(filename, 'w') as file:
        json.dump(arg, file, indent=4)


def jdumps(filename: str, arg) -> None:
    """Encode a Python object as a JSON-formatted string and write it to a file.

    :param filename: The path of the file to write the JSON-formatted string to.
    :type filename: str
    :param arg: The Python object to encode as a JSON-formatted string.
    :type arg: any
    :return: None
    """ 
    with open(filename, 'w') as file:
        json.dumps(arg, file, indent=4)


def yload(filename):
    """Load a YAML file and return its contents as a dictionary.

    :param filename: The path of the YAML file to load.
    :type filename: str
    :return: A dictionary containing the contents of the YAML file.
    :rtype: dict
    """
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    
    return data


def ydump(filename: str, arg) -> None:
    """Write a Python object as a YAML-formatted string to a file.

    :param filename: The path of the file to write the YAML-formatted string to.
    :type filename: str
    :param arg: The Python object to write as a YAML-Formatted string.
    :type arg: any
    :return: None
    """
    with open(filename, 'w') as file:
        yaml.dump(arg, file, default_flow_style=False)


def timestamp_to_time(timestamp: int) -> str:
    """ Convert a UNIX timestamp to a formatted time string.

    :param timestamp: The UNIX timestamp to convert.
    :type timestamp: int
    :return: The formatted time string.
    :rtype: str
    """
    dt = datetime.datetime.fromtimestamp(timestamp)
    
    time = dt.strftime('%I:%M, %p')
    
    return time


def timestamp_to_time_and_date(timestamp: int) -> str:
    """Convert a UNIX timestamp to a formatted date and time string.

    :param timestamp: The UNIX tiemstamp to convert.
    :type timestamp: int
    :return: The formatted time and date string.
    :rtype: str
    """
    dt = datetime.datetime.fromtimestamp(timestamp)
    
    time = dt.strftime('%I:%M, %p')
    date = dt.strftime('%B %d, %Y')
    
    return (date, time)


def url_encode_spaces(link: str) -> str:
    """Convert spaces in a URL to URL encoding.

    This function takes in a URL string and replaces any spaces in the string with the URL-Encoded equivalent, '%20'.
    This is useful for ensuring that URLs with spaces are formatted correctly for use in web applications.

    :param link: The URL string to convert.
    :type link: str
    :return: The converted URL string.
    :rtype: str
    """
    return link.replace(' ', '%20') if ' ' in link else link


def ipfs_url_convert(link: str) -> str:
    """Convert IPFS links to a standard format for easier use with requests.

    This function takes in a URL string and checks if it starts with any of the IPFS-related prefixes specified in `prefix_map`.
    If a matching prefix is found, the function replaces it with `IPFS_URL` and returns the modified URL string.
    If no matching prefix is found, the original URL string is returned.

    :param link: The URL string to convert.
    :type link: str
    :return: The converted URL string.
    :rtype: 
    """
    config = yload('config/config.yaml')
    ipfs_prefix_map = config['ipfs_prefix_map']
    ipfs_url = config['urls']['ipfs']
        
    prefix = next((p for p in ipfs_prefix_map if link.startswith(p)), None)
    if prefix:
        length = ipfs_prefix_map[prefix]
        return f'{ipfs_url}{link[length:]}'
    return link


def check_extension(link: str) -> str:
    """Determine the file extension for a given URL.

    This function takes in a URL string and checks if the URL ends with any of the file extensions specified in `extension_map`.
    If a matching extension is found, the function returns the extension.
    If no matching extension is found, the function uses `urllib` to attempt to determine the content type of the URL,
    and returns the appropriate file extension if it can be determined.
    If the content type cannot be determined after 3 retries, the function returns "png" as a fallback.

    :param link: The URL string to check.
    :type link: str
    :return: The file extension for the given URL.
    :rtype: str
    """
    config = yload('config/config.yaml')
    extension_map = config.get('extensionmap', {})
    
    extension = ''
    
    if link is not None:
        for ext, content_type in extension_map.items():
            if link.endswith(ext):
                extension = ext
                break
            
        if not extension:
            retries = 3
            while retries > 0:
                try:
                    response = urlopen()
                    content_type = response.info().get_content_type()
                    extension = guess_extension(content_type)
                    if extension:
                        extension = extension[1:]
                        break
                except HTTPError:
                    retries -= 1
                    continue
    return extension or 'png'


# Run