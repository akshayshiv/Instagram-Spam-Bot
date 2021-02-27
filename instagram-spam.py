from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from re import sub
from decimal import Decimal

#Opens firefox because the selenium api(geckodriver) is no longer supported on chromne
browser = webdriver.Firefox()

#Goes to instagram.com 
browser.get('https://www.instagram.com/')

#Waits for the page to load so that the css selectors can be loaded in and parsed for
sleep(2) 
#finds the text box where people have to enter their username and password and stores it
# so that we can push to that text box later
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

#your instagram credentials here, where it says YOURUSERNAME and YOURPASSWORD, type in your info
username_input.send_keys("YOURUSERNAME")
password_input.send_keys("YOURPASSWORD")

#Find the login button and click it to enter instagram
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

#Asks the user who they want to spam and what they want to spam with
inputted = input("Who would you like to mess with? ")
browser.get("https://www.instagram.com/"+inputted) #goes to the designated website of the person you want to spam
sleep(1)
spam_or_DM = input("Do you want to spam or DM? ")
if spam_or_DM == "DM" or spam_or_DM == "dm":

    find_messages = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button") #use this if you don't follow them
    #find_messages = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[1]/div/button") #use this if you do follow them
    find_messages.click()
    sleep(2)
    while True:
        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("YOURMESSAGE")
        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(Keys.ENTER)
else:
    comment = input("What do you want to comment?")
    pos = 0
    posts = int(input("How many posts do you want to spam on? "))
    while(pos != posts): #Change this value to what you want, I kept it at while True so it would run forever
        #Finds the first picture by the class name
        pic = browser.find_elements_by_class_name("_9AhH0")    
        pic[pos].click()
        sleep(2)
        to_comment = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button")
        to_comment.click()
        sleep(1)
        comment += str(pos) #Adding a counter so Instagram doesn't block for commenting the same thing over and over again
        pos+=1 #increments the counter so the next comment is not the same
        #finds the comment button and sends the keys that you input (what you want to comment) over and over again
        #It then sends and sleeps for 30 seconds so that you dont get barred for posting comments too fast
        for i in range(10):
            temp = comment + str(i)
            browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(temp)
            browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(Keys.ENTER)
            sleep(30)
        to_close = browser.find_element_by_xpath("/html/body/div[5]/div[3]/button")
        to_close.click()
        sleep(2)


