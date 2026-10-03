import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
URL = os.environ["LBC_URL"]

res = requests.get()
soup = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())