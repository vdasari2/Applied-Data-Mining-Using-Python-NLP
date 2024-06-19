from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Safari()  
driver.get("https://careers.walmart.com/results?q=analyst&page=1&sort=rank&jobCategory=00000161-7bf4-da32-a37b-fbf7c59e0000,00000161-7bfd-da32-a37b-fbff3a4a0000,00000161-7bff-da32-a37b-fbffc8c10000,00000161-8bd0-d3dd-a1fd-bbd0febc0000,00000161-8be6-da32-a37b-cbe70c150000&jobSubCategory=0000018b-4920-d494-a3cb-edb3f3c30000,0000018b-4926-dbdf-a19b-6fbe42760000,0000018b-4930-de4a-ad9f-59ff51360000,0000018b-48a1-de4a-ad9f-58ff99ef0000,0000017c-a4f6-dfa9-a77d-acf64f2f0000,0000018b-48dd-de4a-ad9f-58dffc9d0000,0000018b-4919-d494-a3cb-ed9be5390000,0000018b-4926-da98-adfb-79e7eca60000,0000018b-492b-de4a-ad9f-59ffa0d10000,0000018b-492d-de4a-ad9f-59ff17530000,0000018b-492c-d283-abeb-5b7c8e360000&jobDepartmentCode=00000159-7627-d286-a3f9-7ea7d10c0000&expand=department,brand,type,rate&type=jobs")
time.sleep(5)
posteddate = driver.find_element(By.XPATH, "//label[@title='Job Post Date']")
posteddate.click()
time.sleep(5)
length = driver.find_elements(By.XPATH, "//li[@class = 'search-result job-listing   ']")
print("Total Number of Positions",len(length))
time.sleep(4)  
for i in range(0,len(length)):
    