try:
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver
    from setting import SCREENSHOT_PATH
    from service.custom_logger import loggers
except Exception as e:
    print(str(e))


class selenium_driver():
    log = loggers()

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())




