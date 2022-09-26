import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\chromedriver")

driver.get("https://benchmarktest.dat.com/Web/Home/HomePage.aspx?m=2370345&i=483&h=13")


driver.find_element_by_name("ctl00$ContentPlaceHolderBody$txtUserID").send_keys("savitha.jangir@dat.com")
driver.find_element_by_name("ctl00$ContentPlaceHolderBody$txtPassword").send_keys("Dat@1234")
driver.find_element_by_id("ctl00_ContentPlaceHolderBody_cmdLogin").click()
time.sleep(2)


driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Real Time Estimator']").click()
time.sleep(2)
driver.back()


driver.find_element(By.XPATH,"//a[normalize-space()='Batch Estimator']").click()
time.sleep(2)
driver.back()


driver.find_element(By.XPATH,"//a[normalize-space()='Company Reports']").click()
time.sleep(2)
driver.back()


driver.find_element(By.XPATH,"//a[normalize-space()='Video Tutorials']").click()
time.sleep(2)
driver.back()


driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[3]/div[2]/div[1]/div[3]/ul[1]/li[2]/a[1]").click()
obj=driver.switch_to.alert
obj.accept()
driver.find_element(By.XPATH,"//a[normalize-space()='3PL Template']").click()
obj=driver.switch_to.alert
obj.accept()
driver.find_element(By.XPATH,"//a[normalize-space()='LTLE Template']").click()
obj=driver.switch_to.alert
obj.accept()


driver.find_element(By.XPATH,"//a[normalize-space()='Online Submission form']").click()
time.sleep(2)
driver.back()


driver.find_element(By.XPATH,"//a[normalize-space()='Users']").click()
all_handles = driver.window_handles
print(all_handles)
time.sleep(2)
driver.back()


driver.find_element(By.XPATH,"//a[normalize-space()='Companies']").click()
all_handles = driver.window_handles
print(all_handles)
time.sleep(2)
driver.back()


driver.find_element(By.XPATH,"//a[normalize-space()='Admin Pages']").click()
all_handles=driver.window_handles
print(all_handles)
time.sleep(2)
# for handle in all_handles:
#     if handle != all_handles:
#         driver.switch_to.window(handle)
#         driver.find_element(By.XPATH,"")
driver.back()





driver.find_element(By.XPATH,"//a[contains(text(),'My Profile')]").click()
time.sleep(2)
driver.back()

driver.find_element(By.XPATH,"//a[normalize-space()='DAT Policy']").click()
time.sleep(2)
driver.back()


driver.find_element(By.XPATH,"//a[contains(text(),'Contact Us')]").click()
time.sleep(2)
driver.back()


parent_handle1 = driver.current_window_handle
driver.find_element(By.XPATH,"//a[@title='DATCON']//img").click()
time.sleep(5)
for handle in parent_handle1:
    if handle!= parent_handle1:
        driver.switch_to.window(parent_handle1)
        time.sleep(2)
        break


driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[3]/div[2]/div[2]/span[2]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/a[1]/span[1]/img[1]").click()
time.sleep(2)
driver.back()




parent_handle1 = driver.current_window_handle
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[3]/div[2]/div[2]/span[2]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/span[1]/a[1]").click()
time.sleep(2)
for handle in parent_handle1:
    if handle!=parent_handle1:
        driver.switch_to.window(parent_handle1)
        time.sleep(2)
        break


parent_handle1 = driver.current_window_handle
driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[3]/div[2]/div[2]/span[2]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/a[1]/span[1]").click()
time.sleep(2)
for handle in parent_handle1:
    if handle!=parent_handle1:
        driver.switch_to.window(parent_handle1)
        time.sleep(2)
        break


driver.quit()



