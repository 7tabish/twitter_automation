import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xml.etree.ElementTree as ET
import random
tree = ET.parse('data.xml')
root = tree.getroot()




driver=webdriver.Chrome()
driver.maximize_window()
def login(username,password):
    driver.implicitly_wait(15)
    driver.get('https://twitter.com/AccendoM/following')
    driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys(usernmae)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys(password)
    print('click on login button')
    driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
    driver.implicitly_wait(10)
    print('sleep for 5 sec')
time.sleep(5)


def follow():

    for follow_no in range(1,19): #total accounts are 18 that are showing against this url
        try:
            driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > section > div > div > div > div:nth-child('+str(follow_no)+') > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-46vdb2.r-1777fci.r-5f2r5o.r-bcqeeo > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep > div.css-1dbjc4n.r-k200y.r-1n0xq6e > div > div > span > span').click()
            print('following account no :'+str(follow_no))
            time.sleep(2)
        except Exception as e:
            print(e)


def posting_comments():
        for accounts in range(1,19):
            try:
                driver.find_element_by_css_selector("#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > section > div > div > div > div:nth-child("+str(accounts)+") > div > div").click()
                print('opening account '+str(accounts))
                time.sleep(2)
                driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(3) > section > div > div > div > div:nth-child(1) > div > article > div > div.css-1dbjc4n.r-18u37iz.r-thb0q2 > div.css-1dbjc4n.r-1iusvr4.r-46vdb2.r-1777fci.r-5f2r5o.r-bcqeeo.r-1mi0q7o > div.css-1dbjc4n.r-18u37iz.r-1wtj0ep.r-156q2ks.r-1mdbhws > div:nth-child(1) > div > div > div:nth-child(1) > svg').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div').send_keys(read_comments()) #enter the comments by getting from function
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/span/span').click() #clicking on reply button
                time.sleep(2)
                driver.back() #moving back to main screen
                time.sleep(3)
            except Exception as e:
                print("account not found !")




def read_comments():
    print('reading comments')
    main_category='comment'
    comment_id=random.randint(1,9)# to get the random no for comment and use that random no to get text from xml file
    print(comment_id)
    for main_supres in root.iter('SupRes'):
       for supres_type in main_supres.iter('type'):
           if supres_type.get(main_category+str(comment_id)):
               supres_text=supres_type.get(main_category+str(comment_id))
               return supres_text #returning the commment text










usernmae="your username"
password="your passwordf"


login(usernmae,password)
follow()
posting_comments();

