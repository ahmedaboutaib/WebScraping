from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Define the website to scrape
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'

# Initialize WebDriver (using Firefox in this example)
driver = webdriver.Firefox()

try:
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

    # Switch to the iframe if needed
    iframe = driver.find_element(By.ID, "google_ads_iframe_/22945385001/desktop-sticky_0")
    driver.switch_to.frame(iframe)

    # Now interact with the dropdown
    dropdown = Select(box.find_element(By.ID, 'country'))
    
    # Handle the dropdown option selection with error handling
    try:
        dropdown.select_by_visible_text('Spain')
    except Exception as e:
        print(f"Error selecting dropdown option: {e}")

    # Switch back to default content if you switched to iframe
    driver.switch_to.default_content()

    # Wait for the table to load
    time.sleep(5)

    # Select elements in the table
    matches = driver.find_elements(By.CSS_SELECTOR, 'tr')
    print(f"Liste des éléments trouvés dans le tableau: {matches}")

    # Store the text of each match in a list
    all_matches = [match.text for match in matches]
    #print(f"Texte de chaque match: {all_matches}")

    # Create a DataFrame in Pandas
    df = pd.DataFrame({'goals': all_matches})

    # Save to Excel (.xlsx) file
    excel_file = 'tutorial.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"Data saved to {excel_file}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the WebDriver
    driver.quit()
