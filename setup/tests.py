from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    
    def setUp(self):
        '''Configurar o webdriver'''
        self.browser = webdriver.Chrome(r"C:\Users\carlo\Documents\GitHub\Aplicacao_TDD_no_Django\chromedriver.exe")
        
    def tearDown(self):
        '''fechar o browser'''
        self.browser.quit()