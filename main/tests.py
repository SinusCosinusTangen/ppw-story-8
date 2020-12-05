from django.test import TestCase, Client
from django.test import LiveServerTestCase, TestCase, tag
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create your tests here.
class SearchBoxTest(StaticLiveServerTestCase):

    def setUp(self):
        # self.display = Display(visible=0, size=(1000, 1200))
        # self.display.start()
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.selenium = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        super(SearchBoxTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SearchBoxTest, self).tearDown()
        # self.display.stop()
        return

    def test_connection(self):
        browser = self.selenium
        url = self.live_server_url + '/'
        browser.get(url)
        assert "Story 8" in browser.title

    # def test_search_box_input(self):
    #     browser = self.selenium
    #     url = self.live_server_url + '/'
    #     browser.get(url)
        
    #     wait = WebDriverWait(browser, 20)
    #     wait.until(EC.presence_of_element_located((By.ID, "keyword")))
        
    #     searchbox = browser.find_element_by_id('keyword')
    #     searchbox.send_keys('Frozen 2')
        
    #     wait = WebDriverWait(browser, 20)
    #     wait.until(EC.presence_of_element_located((By.XPATH, '//td[text()="Frozen 2"]')))
        
    #     assert "Frozen 2" in browser.page_source

class MainTestCase(TestCase):
    def test_eksistensi_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # You can also use path names instead of explicit paths.
        response = self.client.get(reverse('main:main'))
        self.assertEqual(response.status_code, 200)
