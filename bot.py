from config import keys
from selenium import webdriver
import time

def order(k):

    driver = webdriver.Chrome('./chromedriver')

    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="s"]/option[1]').click()
    driver.find_element_by_xpath('//*[@id="ard-rrmove-brttons"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k["card"])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["cvv"])
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[1]/option[8]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[2]/option[5]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[2]/div[2]/fieldset/p[2]/label/div/ins').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[3]/div/input').click()
    # driver.find_element_by_xpath('//*[@id="ard-rrmove-brttons"]/input')
    # driver.find_element_by_xpath('')
    # driver.find_element_by_xpath('')

if __name__ == '__main__':
    order(keys)