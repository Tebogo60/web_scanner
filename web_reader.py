import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.prettify())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
