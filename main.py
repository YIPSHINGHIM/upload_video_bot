
import os
import time


from dotenv import load_dotenv



import undetected_chromedriver as driver
from selenium import webdriver

# from selenium.webdriver import Chrome
chrome_driver_path = "/usr/local/bin/chromedriver"
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

email = os.getenv('email')
password = os.getenv('password')

# opts = ChromeOptions() 
# opts.add_argument("--window-size=600,300")

driver = driver.Chrome(executable_path=chrome_driver_path
                # ,options=opts
)

driver.get("https://studio.youtube.com")
# driver.set_window_size(1689, 1056)

time.sleep(2)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f'{email}\n')
time.sleep(2)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(f'{password}\n')

upload_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'upload-button')))
upload_button.click()


video_path = './web_driver_method/video/CleanShot.mp4'
video_abs_path = os.path.abspath(video_path)
print(video_abs_path)

upload_slot = WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input')))

upload_slot.send_keys(video_abs_path)


time.sleep(10000000)
driver.close()