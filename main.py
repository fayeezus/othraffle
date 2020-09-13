import random
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
catchall = input("Catchall: ") #enter your catchall domain
while True:

    print("Starting Browser")
    first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria', 'Alfonso','Mannix','Peter','Dante','Deborah','Xanthus','Lester','Jolie','Forrest','Orli','Adele','Shad','Mufutau','Hamish','Kirk','Wesley','Shad','Candace','Zachery','Maxine','Candace','Fitzgerald','Blythe','Margaret','Drew','Sawyer','Nomlanga','Ulla','Daniel','Ethan','Clayton','Veda','Yasir','Ashely','Mufutau','Leo','Flavia','Dante','Brielle','Nell','Ariana','Ashely','Jason','Patrick','Brennan','Mallory','Hyatt','Reuben','Uta','Althea','Mara','Megan','Lara','Jena','Carissa','September','Courtney','Pearl','Joelle','Chloe','Charles','Sigourney','Lyle','Ashton','Nell','Giacomo','Jemima','Brandon','Elmo','Lois','Brody','Malcolm','Blair','Gisela','Orson','Lila','Madeson','Dustin','Plato','Pearl','Althea','Slade','Iris','Burton','Dahlia',]
    last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
    instagram = ['mrchiipz','smallheartsphotography','akothary22','_jerry.jerry','_jerry.jerry','nathansheckels','ismael_mrgz','bameronshlong','_.popsss','cmhennessey','jaybo_9o1','na_ren_draw','sun_of_a_gun__','ericcccc666','dustybruh','danyvas13','ossskyy','cgiang1023','ms.jackiearana_s','joshua_p3rez','fayeezus.nyc','nycalert','danny__nyc','kuuresento','kickdavid_','harriii_00','axpz_s2k','bryguy.773','__nicojrosa']
    first = random.choice(first_names)
    last = random.choice(last_names)
    chooseinsta = random.choice(instagram)
    email = (first+last+"@"+catchall)
    options = Options()
    options.add_argument('ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--enable-javascript")
    options.add_argument("--headless")
    #options.add_argument("start-maximized")
    #options.add_argument("--enable-logging --v=1")
    driver = webdriver.Chrome("C:/Users/User/Desktop/test/chromedriver", options=options)
    driver.get("https://offthehook.ca/pages/nike-dunk-low-sp-champ-colors-raffle")
    #driver.set_window_position(0,0)
    driver.set_window_size(500,500)
    time.sleep(2)
    print("continuing raffle..")

    fn = driver.find_element_by_css_selector('#content > div > div > div > div > div > form > div > div:nth-child(3) > div:nth-child(1) > div > input')
    fn.send_keys(first)
    print("using first name: " + first)

    em = driver.find_element_by_css_selector('#content > div > div > div > div > div > form > div > div:nth-child(3) > div:nth-child(2) > div > input')
    em.send_keys(last)
    print("using last name: " + last)

    f8 = driver.find_element_by_xpath('/html/body/div[1]/div/a')
    f8.click()

    s1 = driver.find_element_by_xpath('//*[@id="downshift-0-input"]')
    s1.click()
    s4 = driver.find_element_by_xpath('//*[@id="downshift-0-item-3"]')
    s4.click()

    s2 = driver.find_element_by_css_selector('#content > div > div > div > div > div > form > div > div:nth-child(4) > div:nth-child(2) > div > input')
    s2.send_keys(chooseinsta)
    print ("using instagram: " + chooseinsta)

    si = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/form/div/div[5]/div/div/input')
    si.send_keys(email)
    print("using email: " + email)
    
    s6 = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/form/div/div[7]/div')
    s6.click()

    print("Successfully entered OffTheHook raffle with email: " + email) 

    time.sleep(3)
    driver.close()