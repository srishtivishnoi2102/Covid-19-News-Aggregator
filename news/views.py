from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
URL="https://indianexpress.com/article/india/coronavirus-covid-19-cases-tracker-india-latest-news-today-live-updates-corona-cases-deaths-in-india-state-wise-lockdown-update-6469876/"

r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
headings = soup.findAll('div', attrs = {'class':'heading-lvblg'}) 
headings_content = soup.findAll('div', attrs = {'class':'body-lvblg'}) 
# print(soup.prettify())

headings_list=[]
for heading in headings:
	headings_list.append(heading.text)

content_list=[]
for content in headings_content:
	content_list.append(content.text)

news_dict=dict(zip(headings_list,content_list))

def index(request):
    return render(request, 'news/index.html', {'news_dict':news_dict})
