from selenium import webdriver
from getpass import getpass
import time


def start(username, pasword):
    i = __file__.rfind('/')
    driver = webdriver.Firefox(executable_path=__file__[:i + 1] + 'geckodriver.exe')
    driver.get('https://instagram.com/')
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(pasword)
    driver.find_elements_by_tag_name('button')[1].click()  # login button
    time.sleep(5)

    try:
    # not now button
        driver.find_element_by_xpath("// html // body // div[4] // div // div // div // div[3] // button[2]").click()
        time.sleep(2)
    except:
        print('not now button is not.')
    #search
    driver.find_element_by_xpath("//html//body//div[1]//section//nav//div[2]//div//div//div[2]").click()
    time.sleep(2)


"""
0925
0946
1027
"""


def init():
    print('DEBUG mode is True')
    username = input('username: ')
    # # pasword = getpass('password(invisable): ')
    pasword = input('password: ')
    print('Pelase wait...')
    start(username, pasword)


if __name__ == '__main__':
    init()
