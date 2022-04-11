from subprocess import call
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import time
import pandas as pd


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    call_return = {}
    
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(1)
    news_page = browser.html
    soup = bs(news_page,'html.parser')
    #this gets all the headlines and teasers
    headlines = soup.find_all('div', {'class':'content_title'})
    teasers = soup.find_all('div', {'class':'article_teaser_body'})
    #create emptly lists to store the headline and teaser texts
    headline_texts = []
    teasers_texts =[]
    #populates the lists with just the text from the html elements
    for h in headlines:
        headline_texts.append(h.get_text())
    for t in teasers:
        teasers_texts.append(t.get_text())
    #selects the first article for a dictionary
    #note:this could have been done faster with find instead of find all but 
    #this could be useful for more situations
    first_article = {'news_title':headline_texts[0],'news_p':teasers_texts[0]}
    call_return.update(first_article)

    url = 'https://spaceimages-mars.com/'

    browser.visit(url)
    time.sleep(1)

    page = browser.html
    soup = bs(page,'html.parser')

    #get the source of the header image which is the top banner picture
    featured_image = url+soup.find('img', 'headerimage')['src']
    call_return['featured image'] =featured_image

    url = 'https://galaxyfacts-mars.com/'

    browser.visit(url)
    time.sleep(1)

    page = browser.html
    soup = bs(page,'html.parser')
    #find  the table
    table = soup.find('table','table')
    #put the table into a dataframe
    table_df = pd.read_html(str(table))[0]
    #remove unwanted data from table
    reduced_table_df = table_df.drop([2],axis =1).drop([0],axis=0)

    #export the table to html
    new_table = reduced_table_df.to_html()
    call_return['table'] =new_table

    url = 'https://marshemispheres.com/'

    browser.visit(url)
    time.sleep(1)

    page = browser.html
    soup = bs(page,'html.parser')

    images = soup.find_all('img', {'class':'thumb'})

    image_urls =[]
    for image in images:
        temp_string = "https://marshemispheres.com/"+image['src']

        #this gets it as intended for assignment however it gives a .tif file which does not display correctly
        # temp_string = image['src'].split('_')
        # temp_string=url+'images/'+temp_string[-3]+'_'+temp_string[-2]
        image_urls.append(temp_string)

    call_return['hemispheres'] = image_urls

    return call_return