try:
    from service.custom_logger import loggers
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.alert import Alert
    from service.driver_profile import selenium_driver
except Exception as e:
    print(str(e))


# class fun():

class fun():
    def __init__(self, driver):  # TODO : Need to add driver and remove inheritance
        super().__init__()
        self.driver = driver
        self.logger = loggers()  # self.driver = driver

    def get_url_and_start(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.execute_script("document.body.style.zoom='100%'")


    def get_screenshot_and_save(self, name):
        try:
            self.driver.get_screenshot_as_file(SCREENSHOT_PATH + name)

        except Exception as e:
            self.log.exception(str(e))

    def by(self, by):
        _by = str(by).upper()

        if _by == 'XPATH':
            return By.XPATH
        elif _by == 'CSS':
            return By.CSS_SELECTOR
        elif _by == 'CLASS':
            return By.CLASS_NAME
        elif _by == 'TEXT':
            return By.LINK_TEXT
        elif _by == 'ID':
            return By.ID
        elif _by == 'NAME':
            return By.NAME
        elif _by == 'PARTIAL_TEXT':
            return By.PARTIAL_LINK_TEXT
        elif _by == 'TAG':
            return By.TAG_NAME
        else:
            self.logger.error('Locator not Provided')

    # UI ACTION METHODS ####################################

    def find_ui_element(self, locator_type, locator):
        try:
            return self.driver.find_element(self.by(locator_type), locator)

        except Exception as e:
            self.logger.exception(str(e))
            return False

    def wait_explicit(self, ec, element, locator_type, string_param):
        # title_is
        # title_contains
        # presence_of_element_located
        # visibility_of_element_located
        # visibility_of
        # presence_of_all_elements_located
        # text_to_be_present_in_element
        # text_to_be_present_in_element_value
        # frame_to_be_available_and_switch_to_it
        # invisibility_of_element_located
        # element_to_be_clickable

        # TODO: Need to add Below mentioned
        # staleness_of
        # element_to_be_selected
        # element_located_to_be_selected
        # element_selection_state_to_be
        # element_located_selection_state_to_be
        # alert_is_present

        try:

            # Switch & Case Statement for Wait

            return {'TITLE_IS': lambda: WebDriverWait(self.driver, 10).until(EC.title_is(string_param)),
                    'TITLE_CONTAINS': lambda: WebDriverWait(self.driver, 10).until(EC.title_contains(title=string_param)),
                    'PRESENCE_OF_ELEMENT_LOCATED': lambda: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(element)),
                    'VISIBILITY_OF_ELEMENT_LOCATED': lambda: WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(self.find_ui_element(locator_type, element))),
                    'VISIBILITY_OF': lambda: WebDriverWait(self.driver, 10).until(
                        EC.visibility_of(self.find_ui_element(locator_type=locator_type, locator=element))),
                    'PRESENCE_OF_ALL_ELEMENTS_LOCATED': lambda: WebDriverWait(self.driver, 20).until(
                        EC.presence_of_all_elements_located(self.find_ui_element(locator_type, element))),
                    'TEXT_TO_BE_PRESENT_IN_ELEMENT': lambda: WebDriverWait(self.driver, 20).until(
                        EC.text_to_be_present_in_element(self.find_ui_element(locator_type, element), string_param)),
                    'TEXT_TO_BE_PRESENT_IN_ELEMENT_VALUE': lambda: WebDriverWait(self.driver, 20).until(
                        EC.text_to_be_present_in_element_value(self.find_ui_element(locator_type, element), string_param)),

                    'FRAME_TO_BE_AVAILABLE_AND_SWITCH_TO_IT': lambda: WebDriverWait(self.driver, 20).until(
                        EC.frame_to_be_available_and_switch_to_it(self.find_ui_element(locator_type, element))),

                    'INVISIBILITY_OF_ELEMENT_LOCATED': lambda: WebDriverWait(self.driver, 20).until(
                        EC.invisibility_of_element_located(self.find_ui_element(locator_type, element))),

                    'ELEMENT_TO_BE_CLICKABLE': lambda: WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable(self.find_ui_element(locator_type, element))),

                    }.get(str(ec).upper())

        except Exception as e:
            self.logger.exception(str(e))
            return False

    def click(self, locator_type, locator):
        self.find_ui_element(locator_type, locator).click()

    def type(self, locator_type, locator, data):
        self.find_ui_element(locator_type, locator).send_keys(data)

    def select_from_drop_down(self, locator_type, locator, option, option_type='TEXT'):
        try:
            select = Select(self.find_ui_element(locator_type, locator))
            _option = option_type
            if option_type == 'TEXT':
                select.select_by_visible_text(option)
            elif option_type == 'VALUE':
                select.select_by_value(option)
            elif option_type == 'INDEX':
                select.select_by_index(option)
        except Exception as e:
            self.logger.exception(str(e))

    def get_all_options(self, locator_type, locator):

        return Select(self.find_ui_element(locator_type, locator)).options

    def double_click(self, locator_type, locator):
        try:
            Action = ActionChains(self.driver)
            Action.double_click(self.find_ui_element(locator_type, locator)).perform()

        except Exception as e:
            self.logger.exception(str(e))

    def right_click(self, locator_type, locator):
        try:
            Action = ActionChains(self.driver)
            Action.context_click(self.find_ui_element(locator_type, locator)).perform()

        except Exception as e:
            self.logger.exception(str(e))

    def mouse_hover(self, locator_type, locator):
        try:
            Action = ActionChains(self.driver)
            Action.move_to_element(self.find_ui_element(locator_type, locator))

        except Exception as e:
            self.logger.exception(str(e))

    def click_iframe(self, locator_type, locator):
        try:
            self.driver.switch_to.frame(self.find_ui_element(locator_type, locator))
            return True
        except Exception as e:
            self.logger.exception(str(e))
            return False

    def iframe_wrap(self, func, locator, locator_type):  # Switch to iframe decorator [Note: Recommended to Use as It may create a bug]

        def wrapper(wrap_locator, wrap_locator_type):
            self.driver.switch_to.frame(self.find_ui_element(wrap_locator_type, wrap_locator))
            action = func(locator, locator_type)
            self.driver.switch_to.default_content()
            return action

        return wrapper(locator, locator_type)

    def get_title(self):
        try:
            return self.driver.title
        except Exception as e:
            self.logger.exception(str(e))

