import unittest
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from InitDriver.DriverBuild import DriverFactory
logger = logging.getLogger('server_logger')


class AccentureTest(unittest.TestCase):

    def test_1broken_image(self):
        logger.info("Test case : test_broken_image")
        driver = DriverFactory.create_chrome_driver()
        driver.get("https://the-internet.herokuapp.com/broken_images")
        broken = 0
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'content')))
            logger.info('Page loaded successfully')
            image_list = driver.find_elements_by_tag_name("img")
            #print("image list : ", len(image_list))
            logging.info("Total images on page : [%s]", len(image_list))
            for image_object in image_list:
                if image_object.get_attribute("naturalWidth") == '0':
                    logger.info("[%s] is broken.", image_object.get_attribute("outerHTML"))
                    broken += 1
                else:
                    logger.info("[%s] is not broken.", image_object.get_attribute("outerHTML"))
            driver.close()
        except Exception as ex:
            logger.warning('Page or element not loaded.' + ex)

        #Assertion for count of broken image
        self.assertEqual(broken, DriverFactory.read_data("BrokenImageCount"), "Broken image count does not match.")

    def test_2basic_auth(self):
        logger.info("Test case : test_basic_auth")
        driver = DriverFactory.create_chrome_driver()
        driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
        try:
            Ele = driver.find_element_by_class_name('example')
            logger.info("User logged in successfully.")
        except Exception as ex:
            logger.error("Error while logging in." + ex)
        self.assertEqual(True, Ele.is_displayed(), 'Assertion error, Error while logging in.')
        driver.close()

    def test_3slider(self):
        logger.info("Test case : test_slider")
        driver = DriverFactory.create_chrome_driver()
        driver.get('https://the-internet.herokuapp.com/horizontal_slider')
        try:
            slider = driver.find_element_by_xpath("//div[@class='sliderContainer']/input")
            slider_span = driver.find_element_by_xpath("//span[@id='range']")
            driver.execute_script('arguments[0].click()', slider_span)
            max_value = str(int(float(slider.get_attribute("max"))))
            min_value = str(int(float(slider.get_attribute("min"))))
            logger.info('Slider element is present.')
            logger.info("max value of slider : %s", max_value)
            move = ActionChains(driver)
            move.click_and_hold(slider).move_by_offset(60, 0).release().perform()
            self.assertEqual(slider_span.text, max_value, 'Slider is not set to max value')
            logger.info('Slider set to : %s', max_value)
            logger.info("min value of slider : %s", min_value)
            action = ActionChains(driver)
            action.click(slider).perform()
            for i in range(5):
                action.send_keys(Keys.ARROW_LEFT).perform()
            self.assertEqual(slider_span.text, min_value, 'Slider is not set to min value')
            logger.info('Slider set to : %s', min_value)
            driver.close()
        except Exception as ex:
            logger.error("Error while slider verification." + ex)

    def test_4hover_user(self):
        logger.info("Test case : test_hover_user")
        driver = DriverFactory.create_chrome_driver()
        driver.get('https://the-internet.herokuapp.com/hovers')
        try:
            ele = driver.find_elements_by_class_name('figure')
            profile = driver.find_elements_by_class_name('figcaption')
            logger.info("numbers of users : %s", len(ele))
            action = ActionChains(driver)
            for i in range(len(ele)):
                action.move_to_element(ele[i]).perform()
                logger.info("Hover on user : %s", i)
                self.assertEqual(True, profile[i].is_displayed(), 'Mouse hove not verified with user data ' + str(i))
            driver.close()
        except Exception as ex:
            logger.error("Error while verifying user details using mouse hover." + ex)


if __name__ == '__main__':
    unittest.main()
