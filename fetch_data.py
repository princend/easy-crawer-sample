import requests
from bs4 import BeautifulSoup

def fetch_data():
    url = "https://ssr1.scrape.center/"
    response = requests.get(url)
    response.raise_for_status()  # 确保请求成功

    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    for item in soup.find_all('div', class_='el-card__body'):
       
        title = item.find('h2', class_='m-b-sm').text
        img = item.find('img', class_='cover')['src']
        score = item.find('p', class_='score').text
        # link = item.find('a', class_='title')['href']
        data.append({
            'title': title,
            'img':img,
            'score':score
            # 'link': link
        })
        

    return data
