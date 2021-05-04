import requests
from bs4 import BeautifulSoup

URL = "https://corona.mako.co.il/?item=line-graph-canvas"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
covid_19_state = soup.find('div', class_='base-stats main-stats')
# print(covid_19_state)

titles_arr = covid_19_state.find_all('h5', class_='stat-title')
"""
every object in titles_arr saved : <h5 class="stat-title">content</h5>
so to slice only the content between >content< we need to slice str
"""
for i in range(len(titles_arr)):
    start_content_index = str(titles_arr[i]).index('>') + 1
    end_content_index = str(titles_arr[i]).index('/') - 1
    titles_arr[i] = str(titles_arr[i])[start_content_index:end_content_index]
print("titles: ", titles_arr)

numbers_arr = covid_19_state.find_all('p', class_='stat-total')
"""
every object in number saved : <p class="stat-total">3,646</p>
so to slice only the number between >number< we need to slice str
"""
for i in range(len(numbers_arr)):
    start_content_index = str(numbers_arr[i]).index('>') + 1
    end_content_index = str(numbers_arr[i]).index('/') - 1
    numbers_arr[i] = str(numbers_arr[i])[start_content_index:end_content_index]
print("numbers ", numbers_arr)

print(*titles_arr, sep='\t \t \t')
print(*numbers_arr, sep='\t \t \t \t \t \t')