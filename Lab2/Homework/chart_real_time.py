from urllib.request import urlopen
from bs4 import BeautifulSoup
website = urlopen('http://nhaczingmp3.com/bang-xep-hang/bai-hat-Viet-Nam/IWZ9Z08I.html')
html_content = website.read().decode('utf8')
website.close()
soup = BeautifulSoup(html_content, 'html.parser')
ul_chart = soup.find('ul', 'box-song')
li_chart_list = ul_chart.find_all('li')
for li in li_chart_list:
    a = li.a
    print(a['title'])
    print('- '*30)
