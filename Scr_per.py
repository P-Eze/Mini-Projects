from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://workadvisor.co.uk/company-reviews/'

>>> uClient = uReq(my_url)
#opening connection, grabbing page
>>> page_html = uClient.read()
#offloads content from above step into a variable
>>> uClient.close()
#close when web client has finished running
page_soup = soup(page_html,"html.parser")

company = page_soup.findAll("div",{"class":"row company"})