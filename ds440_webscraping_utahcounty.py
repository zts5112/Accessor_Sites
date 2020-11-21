from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://www.utahcounty.gov/LandRecords/AddressSearchForm.asp")

search_street = driver.find_element_by_id("av_street")
search_house = driver.find_element_by_id("av_house")
search_location = driver.find_element_by_id("av_location")
search_dir = driver.find_element_by_id("av_dir")
search_streettype = driver.find_element_by_id('street_type')

search_house.send_keys('66')
search_street.send_keys('680')
search_dir.send_keys('S')
search_location.send_keys('Mapleton')
search_streettype.send_keys('W')

search_button = driver.find_elements_by_xpath("//input[@name='Submit']")[0]
search_button.click()


elems = driver.find_elements_by_tag_name('a')
for elem in elems:
    href = elem.get_attribute('href')
    if 'SerialVersions' in href:
        href_serial = href
        break 
driver.get(href_serial)

elems = driver.find_elements_by_tag_name('a')
for elem in elems:
    href = elem.get_attribute('href')
    if 'av_serial' in href:
        href_serial = href
        break 
driver.get(href_serial)

############################################### GETTING PROPERTY VALUATIONS ###############################################

tabs = driver.find_elements_by_tag_name('li')
tabs[1].click()

current_value_year = driver.find_element_by_xpath('//*[@id="TabbedPanels1"]/div/div[2]/table/tbody/tr[3]/td[1]/a').get_attribute("textContent")
#print("Value Year: ", current_value_year)
market_value_current = driver.find_element_by_xpath('//*[@id="TabbedPanels1"]/div/div[2]/table/tbody/tr[3]/td[13]/div').get_attribute("textContent")
#print("Market Value Prev: ", market_value_current)
current_market_value = {current_value_year: market_value_current}
#print("Year and Market Value: ", current_market_value)

prev_value_year = driver.find_element_by_xpath('//*[@id="TabbedPanels1"]/div/div[2]/table/tbody/tr[4]/td[1]/a').get_attribute("textContent")
market_value_prev = driver.find_element_by_xpath('//*[@id="TabbedPanels1"]/div/div[2]/table/tbody/tr[4]/td[13]/div').get_attribute("textContent")
prev_market_value = {prev_value_year: market_value_prev}
#print("Prev Year and Market Value: ", prev_market_value)

prev2_value_year = driver.find_element_by_xpath('//*[@id="TabbedPanels1"]/div/div[2]/table/tbody/tr[5]/td[1]/a').get_attribute("textContent")
market_value_prev2 = driver.find_element_by_xpath('//*[@id="TabbedPanels1"]/div/div[2]/table/tbody/tr[5]/td[13]/div').get_attribute("textContent")
prev2_market_value = {prev2_value_year: market_value_prev2}
#print("Prev2 Year and Market Value: ", prev2_market_value)

############################################### GETTING PARCEL, BEDROOMS, BATHS ETC ###############################################

driver.get(href_serial)
change_page = driver.find_elements_by_name('nav')
change_page[0].send_keys('Appraisal Information')

owner = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr[6]/td[2]/table/tbody/tr/td').get_attribute("textContent")
#print("Owner: ", owner)

parcel_id = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr[2]/td[1]/strong[2]').get_attribute("textContent")
#print("Parcel Id: ", parcel_id)

account_type = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr[8]/td[2]').get_attribute("textContent")
#print("Account Type: ", account_type)

primary_use = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr[9]/td[2]').get_attribute("textContent")
#print("Primary Use: ", primary_use)

acreage = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[1]/tbody/tr[11]/td[2]').get_attribute("textContent")
#print("Acreage: ", acreage)

land_square_feet = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table[1]/tbody/tr[12]/td[2]").get_attribute("textContent")
#print("Land Square Footage: ", land_square_feet)

house_sq_feet = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[3]/td[2]').get_attribute("textContent")
#print("House Square Feet: ", house_sq_feet)

basement_sq_feet = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[4]/td[2]').get_attribute("textContent")
#print("Basement Square Feet: ", basement_sq_feet)

basement_finished_sq_feet = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[5]/td[2]').get_attribute("textContent")
#print("Basement finished Sq Feet: ", basement_finished_sq_feet)

year_built = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[6]/td[2]').get_attribute("textContent")
#print('Year Built: ', year_built)

quality = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]').get_attribute("textContent")
#print("Quality: ", quality)

condition = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]').get_attribute("textContent")
#print("Condition: ", condition)

exterior = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]').get_attribute("textContent")
#print("exterior: ", exterior)

interior = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]').get_attribute("textContent")
#print("Interior: ", interior)

roof_type = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[2]').get_attribute("textContent")
#print("Roof Type: ", roof_type)

foundation = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td[2]').get_attribute("textContent")
#print("Foundation: ", foundation)

bedroom_count = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[1]/td[2]').get_attribute("textContent")
#print("Bedrooms: ", bedroom_count)

full_baths = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[3]/td[2]').get_attribute("textContent")
#print("Full Baths: ", full_baths)

three_quarter_baths = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[4]/td[2]').get_attribute("textContent")
#print("3/4 Baths: ", three_quarter_baths)

half_baths = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[5]/td[2]').get_attribute("textContent")
#print("Half Baths: ", half_baths)

fireplace = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[7]/td[2]').get_attribute("textContent")
#print("Fireplace: ", fireplace)

#time.sleep(10)

driver.quit()
