import selenium as sln
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string

import time


#here you put you chrom driver location
path="C:\\Users\\andre\\Desktop\\chromedriver.exe"
driver=webdriver.Chrome(path)
driver2=webdriver.Chrome(path)

def get_tp(adr):
	driver2.get(adr)

	nm=driver2.find_element_by_class_name("page-title").text
	print(nm)
	pr=driver2.find_element_by_class_name("product-new-price").get_attribute("innerText")
	pr=pr.replace('Lei','')
	pr=pr.replace('.','')
	print(pr)
	pr=int(pr)/100
	return [nm,pr]



driver.get("http://www.emag.ro")
elm = driver.find_element(by="id",value='searchboxTrigger')
actions = sln.webdriver.ActionChains(driver)
actions.send_keys_to_element(elm,'asus tuf')
actions.send_keys_to_element(elm,Keys.ENTER)
actions.perform()

#card-item
elms=driver.find_elements_by_xpath("//a[@class='product-title js-product-url']")

text= list()
for elm in elms:
	text.append(elm.get_attribute('href'))


nume = list()
pret= list()

for t in text:
	a=get_tp(t)
	nume.append(a[0])
	pret.append(a[1])

import matplotlib.pyplot as plt

plt.plot(range(0,len(pret)),pret)
plt.show()
