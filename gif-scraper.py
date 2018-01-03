# reddit science gifs scraper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from bs4 import BeautifulSoup as bs


chromedriver = '/Users/samuelaltarac/Desktop/python programs/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.reddit.com/r/ScienceGIFs/')

descriptions_list = []
links_list = []
tags_list = []
l = 0
j = 0
k = 0

for i in range(0, 6):

    try:
        html_doc = browser.page_source
        soup = bs(html_doc, 'html.parser')
        # divthings = soup.find_all("div", {'class': 'thing'})
        links = soup.find_all("a", {'class': 'thumbnail'})
        titles = soup.find_all("a", {'class': 'title'})
        tags = soup.find_all("span", {'class': 'linkflairlabel'})

#         check(tags)
# str(k) + ' ' +
        for title in titles:
            descriptions_list.append(title.text)
            l+=1

        for link in links:
            links_list.append(link['href'])
            j+=1

        for tag in tags:
            tags_list.append(tag.text)
            k+=1

        next_button = browser.find_element_by_link_text('NEXT ›')
        next_button.send_keys(Keys.RETURN)
    except:
        print('Stopped')
        break



# print(links_list)
# print(tags_list)
print(descriptions_list)


browser.quit()


tags_list.insert(110, 'none')
d = {'tags': tags_list, 'descriptions' : descriptions_list, 'links': links_list}

df = pd.DataFrame(data=d)

df.to_csv('science_GIFs3.csv')
