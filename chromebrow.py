from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_src_url(urls: dict):
    chrome_opts = Options()
    chrome_opts.add_argument('--headless')
    driver = webdriver.Chrome('./chromedriver-windows-32bit.exe', chrome_options=chrome_opts)

    src_urls = {}
    for name, url in urls.items():
        driver.get(url)
        video_element = driver.find_element_by_xpath('//video')
        src_urls[name] = video_element.get_attribute('src')

    driver.quit()

    return src_urls
