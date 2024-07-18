import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Ensure that the environment variables are set
username = os.getenv('UNIUSER')
password = os.getenv('UNIPASS')

if not username or not password:
    raise ValueError("Please set the USERNAME and PASSWORD environment variables")

# Ask user for the file URL
file_url = input("Enter the URL of the file to download: ").strip()

# Clean and parse the URL
# file_url = urllib.parse.quote(file_url, safe=':/?=&')  # Clean and encode URL

# URL of the login page
login_url = "https://online.uom.lk/login/index.php"

# Your login credentials
payload = {
    'username': username,
    'password': password
}

# Create a session to persist cookies
session = requests.Session()

try:
    # Get the login page
    response = session.get(login_url)
    response.raise_for_status()  # Check for HTTP errors

    # Parse the login page to find the login token
    soup = BeautifulSoup(response.text, 'html.parser')
    login_token = soup.find('input', {'name': 'logintoken'})
    if login_token:
        payload['logintoken'] = login_token['value']

    # Perform login
    login_response = session.post(login_url, data=payload)
    login_response.raise_for_status()  # Check for HTTP errors

    # Download the file
    file_response = session.get(file_url)
    file_response.raise_for_status()  # Check for HTTP errors

    # Save the file
    filename = os.path.basename(urllib.parse.urlparse(file_url).path)
    with open(filename, 'wb') as file:
        file.write(file_response.content)

    print(f"File '{filename}' downloaded successfully.")

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as e:
    print(f"An error occurred: {e}")
