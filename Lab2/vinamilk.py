from urllib.request import urlopen
from bs4 import BeautifulSoup
#Download page
website = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
# website =urlopen(url)
html_content = website.read().decode('utf8')
# put html_content into BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

table_data = soup.find('table', id='tableContent')

temp = open('temp.html', 'w')
temp.write(table_data.prettify())
temp.close()
# 4 find all trs
trs = table_data.find_all('tr')
data = {

}
for td in tds:
    tds = tr.find_all('td')
    for index, td in enumerate(tds):
        content = td.string
        if content != None:
            if index == 0:
                data['title'] = content.strip()
            
