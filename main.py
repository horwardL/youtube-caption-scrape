import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

""" option = webdriver.ChromeOptions()
option.add_argument(" - incognito") """

# define browser driver
driver = webdriver.Chrome("./chromedriver.exe")

# create file
f = open("transcript.txt", "w")

# urls you want the to get the caption from
urls = ["https://www.youtube.com/watch?v=9JzFcGdpT8E",
        "https://www.youtube.com/watch?v=t0Iq8A17xjY",
        "https://www.youtube.com/watch?v=jhu5hygytHo",
        "https://www.youtube.com/watch?v=HATPHZ6P7c4",
        "https://www.youtube.com/watch?v=4YjNe3qvVlI",
        "https://www.youtube.com/watch?v=ZtaHg1C25Kk",
        "https://www.youtube.com/watch?v=DJ-yBmEEkgA",
        "https://www.youtube.com/watch?v=IwpeNnScDEk",
        "https://www.youtube.com/watch?v=13YQVcuT30Q",
        "https://www.youtube.com/watch?v=FKhgrb2zaMA",
        "https://www.youtube.com/watch?v=Z0qadZZyQ2k",
        "https://www.youtube.com/watch?v=l8ryJlm3KRE",
        "https://www.youtube.com/watch?v=6hFk6N0FfOE",
        "https://www.youtube.com/watch?v=iQOwAUeCOt8",
        "https://www.youtube.com/watch?v=1xHrxMpp56M",
        "https://www.youtube.com/watch?v=lUTcgqbh-rc"]

for url in urls:
    # load url
    driver.get(url)

    """ try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/yt-icon-button/button")))
    except TimeoutException:
        print("Timed out waitin for page to load")
        driver.quit() """

    # wait until page load
    time.sleep(10)

    # press the play button to stop the playing video
    play_button = driver.find_element_by_xpath(
        # button full xpath
        "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[21]/div[2]/div[1]/button")
    play_button.click()

    # get then press the munu
    menu_button = driver.find_element_by_xpath(
        "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/yt-icon-button/button")
    menu_button.click()

    time.sleep(3)

    # get and press transcript button make show transcript
    transcript_button = driver.find_element_by_xpath(
        "/html/body/ytd-app/ytd-popup-container/iron-dropdown/div/ytd-menu-popup-renderer/paper-listbox/ytd-menu-service-item-renderer/paper-item")
    transcript_button.click()

    time.sleep(5)

    # use class name to get all the caption text
    caption_ele = driver.find_elements_by_class_name("cue")
    #caption_ele = driver.find_elements_by_xpath("//*[@id='body']/ytd-transcript-body-renderer/div[4]/div[2]")
    captions = [c.text for c in caption_ele]

    # write to ouput file
    for text in captions:
        f.write(text)
        f.write(" ")

    f.write("\n\n")
    time.sleep(5)

f.close()
driver.quit()
