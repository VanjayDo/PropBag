#!/bin/env python
#coding: utf-8
#用于https://www.so-kindle.com/站点的自动登录, 获取积分

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import string

#设置所需参数
VALS={
	"ACCOUNT" :"",	# 填入你的账号名
	"PASSWORD" :""	# 填入你的账号密码
}

def quit(driver):
	driver.quit()
	exit(0)

def login(driver):
	print ("Logging......")
	driver.get("https://www.so-kindle.com/login")
	time.sleep(5)
	driver.find_element_by_id("account").clear()
	driver.find_element_by_id("account").send_keys(VALS.get("ACCOUNT"))
	time.sleep(2)
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("password").send_keys(VALS.get("PASSWORD"))
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="loginform"]/div[3]/div/button').click()
	time.sleep(5)
	try:
		driver.find_element_by_id('navbar')
	except NoSuchElementException:
		print("Login failed,\nplease check your account & password & network,\nor maybe you are limited from loginning.")
		quit(driver)
	else:
		print("Login successfully.")
		return driver
	
if __name__=="__main__":
	driver = webdriver.PhantomJS()
	driver=login(driver)
	quit(driver)