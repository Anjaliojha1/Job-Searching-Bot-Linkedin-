from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Corrected "datach" to "detach"

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

# Open the URL
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3820373996&f_WT=2&keywords=python%20intern&origin=JOB_SEARCH_PAGE_LOCATION_SUGGESTION&refresh=true")

sign_in = driver.find_element(By.CSS_SELECTOR, value="a.nav__button-secondary.btn-md.btn-secondary-emphasis")

sign_in.click()

email = driver.find_element(By.ID, value="username")
email.send_keys("dnkfnds")
password = driver.find_element(By.ID, value="password")
password.send_keys("09rh")

sign_in_button = driver.find_element(By.CSS_SELECTOR, value="button.btn__primary--large.from__button--floating")
sign_in_button.click()

link_element = driver.find_element(By.CSS_SELECTOR, "div.artdeco-entity-lockup__title a")
link_element.click()

time.sleep(1)
save_button = driver.find_element(By.CSS_SELECTOR, "button.jobs-save-button artdeco-button artdeco-button--secondary artdeco-button--3")
save_button.click()

# Click on the anchor tag element





