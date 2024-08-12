from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://amazon.in")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Wrist Watches")

search_button = driver.find_element(By.XPATH, "//input[@value='Go']")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Go']")))
search_button.click()

display_filter = driver.find_element(By.XPATH, "//span[contains(text(), 'Analogue')]")
display_filter.click()

material_filter = driver.find_element(By.XPATH, "//span[contains(text(), 'Leather')]")
material_filter.click()

brand_filter = driver.find_element(By.XPATH, "//span[contains(text(), 'Titan')]")
brand_filter.click()

discount_filter = driver.find_element(By.XPATH, "//span[contains(text(), '25% Off or more')]")
discount_filter.click()

search_results = driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")
if len(search_results) >= 5:
    fifth_element = search_results[4]
    print(fifth_element.text)
else:
    print("There are fewer than five search results.")

input("Press Enter to quit the driver...")

driver.quit()
