import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import os
import urllib.request

class unittest_prueba(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")         

    #def test_buscar(self):
    #    driver = self.driver
    #    driver.get("https://es.wikipedia.org/wiki/Web_scraping")
    #    self.assertIn("scraping",driver.title)
    #    time.sleep(5)
    #    assert "No se encontro el elemento:" not in driver.page_source

    def test_html(self):
        driver = self.driver
        driver.get("https://es.wikipedia.org/wiki/Casa")
        #html = driver.page_source
        #file = open("html.txt", "w", encoding="UTF-8")
        #file.write(html)
        #file.close()
        file = open("links.txt", "w")
        for images in driver.find_elements_by_xpath('.//img'):
            #print(a.get_attribute('href'))
            file.write(str(images.get_attribute('src'))+'\n')
        file.close()
    
    def test_dowload_images(self):
        time.sleep(5)
        file_links = open("links.txt", "r")
        i = 0
        while(True):
            linea = file_links.readline()
            if(linea != ""):
                urllib.request.urlretrieve(linea, "filename"+str(i)+".png")
                i += 1
            if not linea:
                break
        file_links.close()

    def closeprogram(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()