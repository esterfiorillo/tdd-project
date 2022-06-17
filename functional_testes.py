from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()


    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Maria decidiu utilizar o novo app TODO. Ela entra em sua página principal:
        self.browser.get('http://localhost:8000')

@@ -31,8 +34,6 @@ def test_can_start_a_list_and_retrieve_it_later(self):
        # Ela visita a URL: a sua lista TODO ainda está armazenada

        # Satisfeita, ela vai dormir

if __name__ == '__main__':
    unittest.main()