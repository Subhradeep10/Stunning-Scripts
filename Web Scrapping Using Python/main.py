import requests
from bs4 import BeautifulSoup
# In the URL we put the url of the page to be scraped
# Like url = "https://www.<yourWebsite>.com/"
url = ""

r = requests.get(url)
htmlcontent = r.content

prettyHtmlContent = BeautifulSoup(htmlcontent, 'html.parser')
# This provides the total html content of given website.
print(prettyHtmlContent.prettify())

# This helps to get the title content in a website.
title = prettyHtmlContent.title
# print(title)