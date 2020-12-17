import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class unittest_prueba(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")         

    def test_buscar(self):
        driver = self.driver
        driver.get("https://es.wikipedia.org/wiki/Web_scraping")
        self.assertIn("scraping",driver.title)
        time.sleep(5)
        assert "No se encontro el elemento:" not in driver.page_source

    def closeprogram(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()