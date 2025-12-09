
# Problem 14: Create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library for parsing HTML. Try using it to extract all HTML links from a webpage.

import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response=requests.get(url)
    html=response.text

    soup=BeautifulSoup(html,"html.parser")
    links=[]

    for tag in soup.find_all("a",href=True):
        links.append(tag['href'])
    return links
if __name__ == "__main__":
    url=input("Enter the url:")
    for link in extract_links(url):
        print(link)