from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def gmail_sign_in(driver):
    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')

    input = WebDriverWait(driver, 3600).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.gravatar-wrapper-24'))
    )
    driver.implicitly_wait(1)

    driver.get("https://www.youtube.com/feed/history/comment_history")


with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)

    gmail_sign_in(driver)

    delbtnshow = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'ytd-comment-history-entry-renderer:not([is-dismissed]) .yt-icon-button[aria-label="Action menu"]'))
    )

    while delbtnshow:
        delbtnshow = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ytd-comment-history-entry-renderer:not([is-dismissed]) .yt-icon-button[aria-label="Action menu"]'))
        )

        print(delbtnshow)
        driver.implicitly_wait(3)

        try:
            delbtnshow.click()
        except Exception as e:
            print(e)
            continue

        actionBtns = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'paper-listbox ytd-menu-navigation-item-renderer'))
        )

        if actionBtns:
            print('Found %d action buttons.' % len(actionBtns))

        delbtn = None

        if len(actionBtns) > 1:
            delbtn = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'paper-listbox ytd-menu-navigation-item-renderer:nth-child(2)'))
            )
 
        else:
            delbtn = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'paper-listbox ytd-menu-navigation-item-renderer'))
            )
 
        try:
            delbtn.click()
        except Exception as e:
            print(e)
            continue
  
        print(delbtn)

        time.sleep(0.5)

        crmBtn = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#confirm-button .yt-button-renderer'))
        )

        crmBtn.click()

        time.sleep(0.5)


  
