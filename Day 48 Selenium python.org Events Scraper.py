from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

tracked_website = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

driver.get("https://www.python.org/")
time_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
title_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

event_dict = {x:{'time': time_list[x].text, 'name': title_list[x].text} for x in range(5)}
print(event_dict)

driver.close()
