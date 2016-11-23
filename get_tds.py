from lxml import html
import requests
import time

tds = []
for i in range(1,33):

        url = 'http://www.oireachtas.ie/members-hist/default.asp?housetype=0&HouseNum='+str(i)+'&disp=mem'
        page = requests.get(url)
        tree = html.fromstring(page.content)
        tds_this_house = tree.xpath('//b/text()')
        tds.append(tds_this_house)

        print("House: %d, TD's scraped: %d"%(i, len(tds)))
        print(tds_this_house)
        time.sleep(20)

