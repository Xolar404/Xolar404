import time
import pyautogui
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

print()
print("----------Scrape Pseudo Instagram----------")
print()

def launch_link(link):
    global driver
    driver = webdriver.Firefox()
    driver.get(link)
    time.sleep(4)

launch_link("https://www.instagram.com/")

def accept_coockies():
    time.sleep(6)
    click_on_cookies = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
    click_on_cookies.click()
    time.sleep(4)

accept_coockies()

def login(pseudo="YOUR PSEUDO", password="YOUR PASSWORD"):

    username = driver.find_element(By.NAME, "username")
    username.click()
    username.send_keys(pseudo)

    mdp = driver.find_element(By.NAME, "password")
    mdp.click()
    mdp.send_keys(password)

    time.sleep(2)

    connect = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
    connect.click()

login()

def redirect_on_followers(followers):
    time.sleep(5)
    driver.get(followers)

redirect_on_followers("https://www.instagram.com/france/followers/")

def click_on_show_followers():
    
    time.sleep(3)
    show_followers = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span")
    show_followers.click()                              
    time.sleep(13)

click_on_show_followers()

def scrap_pseudo():
    try:
        for number in range(1, 1001):
            #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            pyautogui.scroll(-900)                                   
            get_pseudo = driver.find_element(By.XPATH, f"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{number}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")
            print(get_pseudo.text)
            
    except KeyboardInterrupt:
        print("CTRL+C")
    except selenium.common.exceptions.NoSuchElementException:
        scrap_pseudo()
    finally:
        print()
        print("Au revoir ;)")

scrap_pseudo()
