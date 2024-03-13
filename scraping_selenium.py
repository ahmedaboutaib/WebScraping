from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select  # Importer Select ici
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Define the website to scrape
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'

# Initialize WebDriver (using Firefox in this example)
driver = webdriver.Firefox()

# Open the website
driver.get(website)

# Wait for the button "All matches" to be clickable
all_matches_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='page-wrapper']/div/home-away-selector/div/div/div/div/label[2]"))
)

# Click on the button
all_matches_button.click()

# Wait for the dropdown to load
time.sleep(2)

# Using the "box" section as a reference to help locate an element inside
box = driver.find_element(By.CLASS_NAME, 'panel-body')

# Select dropdown and select element inside by visible text
dropdown = Select(box.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')

# Wait for the table to load
time.sleep(5)

# Select elements in the table
matches = driver.find_elements(By.CSS_SELECTOR, 'tr')
print(f"Liste des éléments trouvés dans le tableau: {matches}")

# Store the text of each match in a list
all_matches = [match.text for match in matches]
print(f"Texte de chaque match: {all_matches}")
# Quit the WebDriver
driver.quit()

# Create a DataFrame in Pandas and export to CSV
df = pd.DataFrame({'goals': all_matches})
print(df)
df.to_csv('tutorial.csv', index=False)
