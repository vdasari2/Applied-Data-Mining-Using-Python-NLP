#Code to Scrap Data from websites   
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
import time
import spacy 
import requests

f = open('companieslist.json')
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

# positionname = ['Business Analyst','Data Analyst','Data Science Analyst']
positionname = ['SDE','Software Developer','Front End Developer','Back End Developer','Senior Developer']
data = json.load(f)
f.close() 
for (k, v) in data.items(): 
   driver = webdriver.Safari()  
   driver.get(str(v))  
   time.sleep(2) 
   length = driver.find_elements(By.XPATH, "//div[@data-bind='foreach: opportunities']/div")
   print("Total Number of Positions",len(length))
   time.sleep(4)  
   positionlink = [] 
   positionname = []
   for i in range(0,len(length)): 

      #rolename 
      rolename = driver.find_element(By.XPATH, f"//div[@data-bind='foreach: opportunities']//div[@id='Opportunity{i}']//div[@class='row']//div[1]//h3//a")
      x = rolename.text.strip()

      #get href link name
      printlink = driver.find_element(By.XPATH, f"//div[@data-bind='foreach: opportunities']//div[@id='Opportunity{i}']//div[@class='row']//div//h3//a").get_attribute("href")

      #check if there are any new positions opened 
      posteddate = driver.find_element(By.XPATH, f"//div[@data-bind='foreach: opportunities']//div[@id='Opportunity{i}']//div[@class='row']//div[2]//h3")
      # print(name.text.strip())
      if (posteddate.text.strip() == "Today"): 	
            output = query({
                "inputs": {
                    "source_sentence": f"{x}",
                    "sentences": [
                        "Data Analyst",
                        "Risk Analyst",
                        "Data Science Analyst",
                        "Business Analyst",
                        "Senior Data Science Analyst",
                        "Senior Business Analyst",
                        "Data Scientist",
                        "Junior Data Scientist",
                        "Senior Data Scientist"
                    ]
                },
            })
            output.sort(reverse=True)
            result = map(lambda x: x * 100,output)
            final_result = list(result)
            if final_result[0] > 70:
                positionlink.append(printlink) 
            #print(listofpositions)
      else:
         continue
   driver.close() 
   if(len(positionlink) == 0):
      print("No new positions opened today")
   else:
      print(positionlink)
   for i in range(len(positionlink)):
      driver = webdriver.Safari()
      driver.get(str(positionlink[i]))  
      time.sleep(3)
      driver.close()

