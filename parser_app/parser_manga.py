import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://remanga.org'

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}
#1
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#2
def get_data(html):
    bs = BS4(html.text, 'html.parser')
    items = bs.find_all('div', class_='Grid_gridItem__aPUx1 p-1')
    manga_list = []
    for item in items:
        title = item.find('div', class_='pr-2 pl-0.5 mb-1').get_text(strip=True)
        year = item.find('div', class_='flex items-center').get_text(strip=True)
        # image = URL + item.find('div', class_='Vertical_wrapper__GnC8C').find('img').get('src')
        manga_list.append(
            {'title': title,
             'year': year,
             # 'image': image
             }
        )
    return manga_list


#3
def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        manga_list2 = []
        for page in range(1, 2):
            response = get_html('https://remanga.org/manga', params={'page': page})
            manga_list2.extend(get_data(response))
        return manga_list2
    else:
        raise Exception('Error in parsing')

# print(parsing())
