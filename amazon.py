from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Selenium WebDriver (using Chrome for this example)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (without opening the browser)
driver = webdriver.Chrome(options=options)

# Open amazon.in
driver.get("https://www.amazon.in")
time.sleep(2)  # Wait for page to load

# Search for "lg soundbar"
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("lg soundbar")
search_box.submit()
time.sleep(2)  # Wait for search results to load

# Get product names and associated prices from the first page of search results
products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
product_data = []

for product in products:
    try:
        # Get the product name
        product_name = product.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text

        # Get the product price, if not available, set it to 0
        try:
            product_price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text.replace(',', '')
        except:
            product_price = "0"  # If price not found, set as zero

        # Append product name and price to the list
        product_data.append((product_name, int(product_price)))
    except:
        continue  # Ignore products without proper structure

# Sort products by price
product_data.sort(key=lambda x: x[1])

# Output sorted products
for price, name in product_data:
    print(f"{price} {name}")

# Close the browser session
driver.quit()
