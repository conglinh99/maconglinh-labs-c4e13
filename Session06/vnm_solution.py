from urllib.request import urlopen
from bs4 import BeautifulSoup

#1. Download website
url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
website = urlopen(url)
html_content = website.read().decode('utf8')
# print(text)
# 2. Put html_content into BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
# 3. Find table
table_data = soup.find('table', id='tableContent')

# temp = open('temp.html', 'w')
# temp.write(table_data.prettify())
# temp.close()
# 4. find all trs
trs = table_data.find_all('tr')
# print(trs[0].prettify())
data_list = []
for tr in trs:
    tds = tr.find_all('td')
    data = {}
    for index, td in enumerate(tds):
        content = td.string
        if content != None:
            if index == 0:
                data['title'] = content.strip()
            elif index == 1:
                data['Quý 4 - 2016'] = content
            elif index == 2:
                data['Quý 1 - 2017'] = content
    if data != {}:
        data_list.append(data)

print(data_list)
