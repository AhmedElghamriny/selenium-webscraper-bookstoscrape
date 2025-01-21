import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load proxies from file
with open("proxies_list.txt", "r") as file:
    proxies = file.readlines()

# Select a random proxy
proxy = random.choice(proxies).strip()
print(f"Using proxy: {proxy}")

# Configure ChromeDriver to use the proxy
chrome_options = Options()
chrome_options.add_argument(f"--proxy-server=http://{proxy}")  # Use "http://" for the IP:port format

# Path to your ChromeDriver executable
path = "C:/Users/agham/chromedriver-win64/chromedriver.exe"

try:
    # Initialize WebDriver with proxy configuration
    driver = webdriver.Chrome(service=Service(path), options=chrome_options)

    # Website to scrape
    website = "https://books.toscrape.com/"
    driver.get(website)

    all_products = []
    wait = WebDriverWait(driver, 10)

    # Scrape data
    while True:
        div_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.col-sm-8.col-md-9')))
        ol_element = div_element.find_element(By.TAG_NAME, 'ol')
        li_elements = ol_element.find_elements(By.TAG_NAME, 'li')

        for li in li_elements:
            title = li.find_element(By.CSS_SELECTOR, 'h3 a').text
            price = li.find_element(By.CSS_SELECTOR, '.price_color').text
            all_products.append({'title': title, 'price': price})

        current_page = driver.find_element(By.CSS_SELECTOR, '.current')
        if current_page.text == 'Page 50 of 50':
            break

        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.next a')))
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        next_button.click()

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Print the collected product information
    for product in all_products[:5]:  # Print the first 5 products as an example
        print(f"Title: {product['title']}, Price: {product['price']}")

    driver.quit()
