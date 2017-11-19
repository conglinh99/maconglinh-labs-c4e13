# 1. table -> tbody
# 2. all tr
# 3. for each in range -> all tds
# 4.for each tds -> string
from urllib.request import urlopen
from bs4 import BeautifulSoup

web = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
html_content = web.read().decode('utf8')
web.close()

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', id= 'tableContent')
td_list = table.find_all('td')
for td in td_list:
    print(td.get_text())
