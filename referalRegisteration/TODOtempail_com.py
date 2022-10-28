from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import re
import sys

userProfileDir='/home/endu/.config/chromium/Default'
adblockDir='/home/endu/.config/chromium/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/4.46.0_0'

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("incognito")
options.add_argument("user-data-dir=%s" % userProfileDir)
options.add_argument("load-extension=%s" % adblockDir)
options.add_argument("file-url-path-alias=/gen=/usr/lib/chromium/gen")
try:
        if sys.argv[1]:
                proxy=sys.argv[1]
                options.add_argument("proxy-server=%s" % proxy)
except Exception as e:
        pass

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_extension('/home/endu/Downloads/AdBlock — best ad blocker(4.46.0)2022-04-24.crx')
driver = webdriver.Chrome(options=options, executable_path=r"chromedriver")

# try:

#         # to skirt adblock first-run notification
#         driver.set_page_load_timeout(1)
#         while len(driver.window_handles) != 2:
#                 sleep(1)

#         killed=False

#         while not killed:
#                 for i in driver.window_handles:
#                         driver.switch_to.window(i)
#                         if driver.current_url.find('https://getadblock.com') != -1:
#                                 driver.close()
#                                 killed=True

#         driver.set_page_load_timeout(10000)
# except Exception as e:
#         pass

driver.switch_to.window(driver.window_handles[0])

referal = 'https://r.honeygain.me/ELBETAA2FC'
tempmail_url = 'https://tempail.com'
pw = 'Moron101!'
driver.get(tempmail_url)
email_address = ''

while not email_address:
        try:
                if driver.find_element(by=By.ID, value='eposta_adres'):
                        email_address = driver.find_element(by=By.ID, value='eposta_adres').get_property('value')
                        if not re.search('^\w+@\w+\.\w+$', email_address):
                                email_address=''
                if not email_address:
                        sleep(2)
        except Exception as e:
                pass

# input("Is this email address fine? " + email_address)

driver.get(referal)
driver.find_element(by=By.CLASS_NAME, value='a-claimNow').click()

while len(driver.find_elements(by=By.TAG_NAME, value='input')) != 5:
        sleep(1)

while driver.find_elements(by=By.TAG_NAME, value='input')[0].get_attribute('type') != 'email':
        sleep(1)

while driver.find_elements(by=By.TAG_NAME, value='input')[1].get_attribute('type') != 'password':
        sleep(1)

# not interactable error

email_field = driver.find_elements(by=By.TAG_NAME, value='input')[0]
pwd_field = driver.find_elements(by=By.TAG_NAME, value='input')[1]
## TO DO until value of input equals email, try to input

while email_field.get_property('value') != email_address:
        try:
                email_field.clear()
                email_field.click()
                email_field.send_keys(email_address)
                pwd_field.clear()
                pwd_field.click()
                pwd_field.send_keys(pw)
        except Exception as e:
                pass


print("sent email to " + email_address)

driver.find_elements(by=By.TAG_NAME, value='button')[0].click()

driver.get(tempmail_url)

# wait till email gets here
while driver.page_source.find("Welcome to Honeygain") == -1:
        sleep(1)

try:
        driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Welcome to Honeygain").click()
except Exception as e:
        pass

try:
        driver.switch_to.frame(driver.find_element(by=By.TAG_NAME, value='iframe'))
except Exception as e:
        pass

verification_link=""

while not verification_link:
        for a in driver.find_elements(by=By.TAG_NAME, value='a'):
                if re.search('^https:\/\/dashboard\.honeygain.+$', a.get_attribute('href')):
                        verification_link=a.get_attribute('href')

## GOING TO VERIFICATION LINK

driver.get(verification_link)

try:
        driver.close()
        driver.quit()
except Exception as e:
        pass


## WRITING CREDENTIALS TO FILE

try:
        f = open('/home/endu/Documents/honeygainCreds', 'a')
        f.write(email_address + '\t' + pw + '\n')
        f.close()
except:
        print("error writing creds to file")

print("registered " + email_address + " with default password")
