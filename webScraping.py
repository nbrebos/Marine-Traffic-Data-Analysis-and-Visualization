# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

# Initialize a new Chrome browser instance using the Selenium WebDriver
driver = webdriver.Chrome()

# Define the base URL for the data on vessels
base_url = "https://www.marinetraffic.com/en/data/?asset_type=vessels&columns=shipname,recognized_next_port,current_port,ship_type,area,area_local,lat_of_latest_position,lon_of_latest_position,speed,year_of_build,dwt"
# Number of pages to scrape (you can change this)
num_pages = 15
# Initialize lists to store scraped data
df_list = []

# Iterate through the specified number of pages
for _ in range(num_pages):
    # Wait for the page to fully load
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ag-cell-content'))
        WebDriverWait(driver, 20).until(element_present)
    except:
        print("Timed out waiting for page to load")

    # Parse the page source of the driver using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all 'div' elements with class 'ag-cell-content'
    all_info = soup.find_all('div', class_='ag-cell-content')

    # Extract text content from each 'div' element found in 'all_info'
    all_info_content = [div.text for div in all_info]

    # Extract other relevant information from the page
    # Extract relevant information from the page
    shipname = all_info_content[0::12]  # Assuming shipname is at index 0
    recognized_next_port = all_info_content[1::12]  # Assuming recognized_next_port is at index 1
    current_port = all_info_content[2::12]  # Assuming current_port is at index 2
    ship_type = all_info_content[3::12]  # Assuming ship_type is at index 3
    area = all_info_content[4::12]  # Assuming area is at index 4
    area_local = all_info_content[5::12]  # Assuming area_local is at index 5
    latitude = all_info_content[6::12]  # Assuming latitude is at index 6
    longitude = all_info_content[7::12]  # Assuming longitude is at index 7
    speed = all_info_content[8::12]  # Assuming speed is at index 8
    year_of_build = all_info_content[9::12]  # Assuming year_of_build is at index 9
    owner_country = all_info_content[10::12]  # Assuming owner_country is at index 10
    gross_tonnage = all_info_content[11::12]  # Assuming gross_tonnage is at index 11

    # Append data to the ship_data list
    df_list.extend(zip(shipname, recognized_next_port, current_port, ship_type, area, area_local, latitude, longitude, speed, year_of_build, owner_country, gross_tonnage))

    # Find and click the 'Next Page' button
    try:
        next_page_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'MuiButton-root') and contains(@class,'mtapp49')]"))
        next_page_button.click()
    except:
        print("Next page button not found or did not appear in time")
        break  # Break the loop if the button is not found or doesn't work

# Create a Pandas DataFrame to store the scraped data
data = {
    "Ship Name": [name for name, _, _, _, _, _, _, _, _, _, _, _ in df_list],
    "Destinnation Port": [port for _, port, _, _, _, _, _, _, _, _, _, _ in df_list],
    "Current Port": [port for _, _, port, _, _, _, _, _, _, _, _, _ in df_list],
    "Ship Type": [ship_type for _, _, _, ship_type, _, _, _, _, _, _, _, _ in df_list],
    "Global Area": [area for _, _, _, _, area, _, _, _, _, _, _, _ in df_list],
    "Local Area": [area_local for _, _, _, _, _, area_local, _, _, _, _, _, _ in df_list],
    "Latitude": [lat for _, _, _, _, _, _, lat, _, _, _, _, _ in df_list],
    "Longitude": [lon for _, _, _, _, _, _, _, lon, _, _, _, _ in df_list],
    "Speed": [s for _, _, _, _, _, _, _, _, s, _, _, _ in df_list],
    "Year of Build": [year for _, _, _, _, _, _, _, _, _, year, _, _ in df_list],
    "Owner Country": [country for _, _, _, _, _, _, _, _, _, _, country, _ in df_list],
    "Gross Tonnage": [tonnage for _, _, _, _, _, _, _, _, _, _, _, tonnage in df_list]
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("vessel_data.csv", index=False)

# Close the browser
driver.quit()

