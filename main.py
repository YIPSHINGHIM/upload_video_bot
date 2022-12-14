
import os
import time

import undetected_chromedriver as driver
from dotenv import load_dotenv
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
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(f'{password}\n')\

file_name = os.listdir('./video')
print(file_name)

video_path_list = []
for file in file_name:
    video_path = f'./video/{file}'
    video_path_list.append(video_path)

print(video_path_list)


def upload_func(video_path):
    
    # * find the upload button and click it
    upload_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'upload-button')))
    upload_button.click()


    # * upload the video 
    video_abs_path = os.path.abspath(video_path)
    print(video_abs_path)

    upload_slot = WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.XPATH,'/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input')))
    upload_slot.send_keys(video_abs_path)

    # * set the video is not for child 
    no_for_kid_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, 'VIDEO_MADE_FOR_KIDS_NOT_MFK')))
    no_for_kid_button.click()
    time.sleep(1)


    # * set the video is not for child 
    visibility_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'step-badge-3')))
    visibility_button.click()
    time.sleep(1)

    # * make the video private 
    private_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'private-radio-button')))
    private_button.click()
    time.sleep(3)

    # * done 
    done_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'done-button')))
    done_button.click()
    time.sleep(1)

    # * close button
    close_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/ytcp-button')))
    close_button.click()
    time.sleep(5)

# upload_func(video_path)


for filname in video_path_list:
    upload_func(filname)


time.sleep(10000)
driver.close()