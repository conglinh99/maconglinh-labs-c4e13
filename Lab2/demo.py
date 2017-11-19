from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen('http://dantri.com.vn')
html_content = website.read().decode('utf8')

website.close()


soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())
ul_news = soup.find('ul', 'ul1 ulnew')
# print(ul_news.prettify())
li_news_list = ul_news.find_all('li')
for li in li_news_list:
    # print(li.prettify())
    a_detail = li.h4.a
    title = a_detail['title'] #Attribute
    content = a_detail.string #content
    print(content)
    print('-' * 20)
