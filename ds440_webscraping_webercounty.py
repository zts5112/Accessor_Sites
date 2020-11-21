from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://www3.co.weber.ut.us/psearch/")

search_address = driver.find_element_by_id("address")

search_address.send_keys('829 E 725 N')

search_address.send_keys(Keys.RETURN)

link = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[3]/td[1]/a').get_attribute("href")
driver.get(link)

market_value_current = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[1]').get_attribute("textContent")
current_year = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/form/font').get_attribute("textContent")
market_year_dict = {current_year: market_value_current}
print("Current Market: ", market_year_dict)

taxable_value = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]').get_attribute("textContent")
taxable_dict = {current_year: taxable_value}
print("Taxable: ", taxable_dict)

driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/form/select/option[3]").click()

prev_year = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/form/font').get_attribute("textContent")
prev_market_value = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[1]').get_attribute("textContent")
prev_market_year_dict = {prev_year:prev_market_value}
print("Prev Market: ", prev_market_year_dict)

taxable_value = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]').get_attribute("textContent")
taxable_dict = {prev_year: taxable_value}
print("Taxable: ", taxable_dict)

driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/form/select/option[4]").click()

prev2_year = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/form/font').get_attribute("textContent")
prev2_market_value = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[1]').get_attribute("textContent")
prev2_market_year_dict = {prev2_year:prev2_market_value}
print("Prev Market: ", prev2_market_year_dict)

taxable_value = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]').get_attribute("textContent")
taxable_dict = {prev2_year: taxable_value}
print("Taxable: ", taxable_dict)

link = driver.find_element_by_xpath('/html/body/table/tbody/tr[4]/td/div/table/tbody/tr/td[4]/div/a').get_attribute("href")
driver.get(link)

parcel_id = driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/table/tbody/tr[4]/td/div').get_attribute("textContent")
parcel_id = parcel_id[10:]
print("Parcel: ", parcel_id)

property_type = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[1]/td[2]/span').get_attribute("textContent")
property_type = property_type.strip()
print("Property Type: ", property_type)

description = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[2]/td[2]/span').get_attribute("textContent")
description = description.strip()
print("Description: ", description)

stories = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[3]/td[2]/span').get_attribute("textContent")
stories = stories.strip()
print("Stories: ", stories)

above_grade_sq_feet = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[4]/td[2]/span').get_attribute("textContent")
above_grade_sq_feet = above_grade_sq_feet.strip()
print("Above Grade: ", above_grade_sq_feet)

basement_sq_feet = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[5]/td[2]/span').get_attribute("textContent")
basement_sq_feet = basement_sq_feet.strip()
print("Basement Sq feet: ", basement_sq_feet)

total_sq_feet = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[6]/td[2]/span').get_attribute("textContent")
total_sq_feet = total_sq_feet.strip()
print("total: ", total_sq_feet)

basement_percent_complete = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[7]/td[2]/span').get_attribute("textContent")
basement_percent_complete = basement_percent_complete.strip()
print("Basement percent complete: ", basement_percent_complete)

garage_sq_feet = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[8]/td[2]').get_attribute("textContent")
garage_sq_feet = garage_sq_feet.strip()
print("Garage: ", garage_sq_feet)

percent_complete = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[9]/td[2]/span').get_attribute("textContent")
percent_complete = percent_complete.strip()
print("Percent Complete: ", percent_complete)

exterior = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[10]/td[2]/span').get_attribute("textContent")
exterior = exterior.strip()
print("exterior: ", exterior)

roof_cover = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[11]/td[2]/span').get_attribute("textContent")
roof_cover = roof_cover.strip()
print("Roof Cover: ", roof_cover)

year_built = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[12]/td[2]/span').get_attribute("textContent")
year_built = year_built.strip()
print("Year Built: ", year_built)

lot_size_acres = driver.find_element_by_xpath('/html/body/table/tbody/tr[6]/td/table/tbody/tr[13]/td[2]/span').get_attribute("textContent")
lot_size_acres = lot_size_acres.strip()
print("Lot Size: ", lot_size_acres)

driver.quit()