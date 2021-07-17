# #!/usr/bin/env python
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

#Logging Config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filename='selenium-test.log',
    )

# crmDrvPath = '/usr/local/bin/chromedriver'

# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(r'C:\Users\IEUser\Downloads\chromedriver_win32\chromedriver.exe')

    url = "https://www.saucedemo.com"
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get(url)

    driver.find_element_by_id('user-name').send_keys('standard_user')
    driver.find_element_by_id('password').send_keys('secret_sauce')
    driver.find_element_by_css_selector('.btn_action').click()
    print(driver.current_url)
    print(url + '/inventory.html')
    logging.info(url + '/inventory.html')
    
    if url + '/inventory.html' == driver.current_url:
        print("### TEST PASSED - " + user + " Logged in Successfully")  
    else:
        print("### TEST FAILED - " + user + " unable to login")

    # Inventory List 
    items = driver.find_elements_by_css_selector("div.inventory_item")
    successful_btn_index = []

    # Adding items to cart
    for item in items:
        btn = item.find_element_by_css_selector("button.btn_primary.btn_inventory")
        itemName = item.find_element_by_css_selector("div.inventory_item_name")
        initCartVal = 0 if not is_selector_exist("span.shopping_cart_badge", driver) else driver.find_element_by_css_selector("span.shopping_cart_badge").text
        btn.click()
        currentCartVal = driver.find_element_by_css_selector("span.shopping_cart_badge").text
        item_index = items.index(item)
        if int(currentCartVal) == int(initCartVal) + 1:
            print(itemName.text + " has been added to cart")
            logging.info(itemName.text + " has been added to cart")
            successful_btn_index.append(item_index)
        else:
            print("Failed to add " + itemName.text + " to cart")
            logging.warning("Failed to add " + itemName.text + " to cart")
        time.sleep(1)
    
    #Check if cart contains all added items
    logging.info("### Checking if items were added to cart... ###")
    cartVal = 0 if not is_selector_exist("span.shopping_cart_badge", driver) else driver.find_element_by_css_selector("span.shopping_cart_badge").text
    print("### Total number of items on Page is: " + str(len(items)))
    logging.info("### Total number of items on Page is: " + str(len(items)))
    print("### Total items in the cart is " + str(cartVal))
    logging.info("### Total items in the cart is " + str(cartVal))
    if str(cartVal) == str(len(items)):
        print("### TEST PASSED - Cart contains all added items for user: " + user)
        logging.info("### TEST PASSED - Cart contains all added items for user: " + user)
    else:
        print("### TEST FAILED- Cart does not contain all added items for user: " + user)
        logging.warning("### TEST FAILED- Cart does not contain all added items for user: " + user)
    
      #Remove all items from cart
    logging.info("### Start removing items from cart... ###")

    for index in successful_btn_index:
        btn = items[index].find_element_by_css_selector("button.btn_secondary.btn_inventory")
        itemName = items[index].find_element_by_css_selector("div.inventory_item_name")
        oldCartVal = int(driver.find_element_by_css_selector("span.shopping_cart_badge").text)
        btn.click()
        if len(driver.find_elements_by_css_selector("span.shopping_cart_badge")) != 0:
            newCartVal = int(driver.find_element_by_css_selector("span.shopping_cart_badge").text)
            if newCartVal == oldCartVal - 1:
                print(itemName.text + " has been successfully removed from cart")
                logging.info(itemName.text + " has been successfully removed from cart")
            else:
                print("Failed to remove " + itemName.text + " from cart")
                logging.warning("Failed to remove " + itemName.text + " from cart")
        else:
            print(itemName.text + " has been removed from cart")
            logging.info(itemName.text + " has been removed from cart")
            print("No more item in the cart")
            logging.info("No more item in the cart")

def is_selector_exist(selector, driver = None, webelement = None):
    if driver != None:
        counter_element = driver.find_elements_by_css_selector(selector)
    else:
        if webelement != None:
            counter_element = webelement.find_elements_by_css_selector(selector)
        else:
            counter_element = driver.find_elements_by_css_selector(selector)
    if len(counter_element) == 0:
        return False
    else:
        return True

login('standard_user', 'secret_sauce')
