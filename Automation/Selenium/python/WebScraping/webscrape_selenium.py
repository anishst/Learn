# https://preettheman.medium.com/how-to-scrape-data-from-any-website-using-python-c46a444b86aa

#IMPORT THESE PACKAGES
import selenium
from selenium import webdriver
import pandas as pd
#OPTIONAL PACKAGE, BUY MAYBE NEEDED
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

#THIS INITIALIZES THE DRIVER (AKA THE WEB BROWSER)
driver = webdriver.Chrome(ChromeDriverManager().install())

#THIS PRETTY MUCH TELLS THE WEB BROWSER WHICH WEBSITE TO GO TO
driver.get('https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=sr_1_3?dchild=1&keywords=laptop&qid=1618857971&sr=8-3')

#TITLE OF PRODUCT
Title = driver.find_element_by_xpath("//*[@id='productTitle']").text
#PRICE OF PRODUCT
Price = driver.find_element_by_xpath("//*[@id='priceblock_dealprice' or @id='priceblock_ourprice' or @id='priceblock_saleprice']").text

#CREATES A EMPTY DATAFRAME
data1 = {'Title':[], 'Price':[],}
fulldf = pd.DataFrame(data1)

#APPENDING THE DATA PULLED FROM ABOVE INTO THE EXISTING DATAFRAME
row = [Title, Price]
fulldf.loc[len(fulldf)] = row

print(row)
print(fulldf)
client = pymongo.MongoClient("192.168.1.50:27017")
db = client['amazon']
printer_collection = db['price_history']
printer_collection.insert_one({'Title':row[0], 'Price':row[1]})

driver.quit()