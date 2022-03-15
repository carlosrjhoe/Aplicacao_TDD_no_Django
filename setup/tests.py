from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisTestCase(LiveServerTestCase):
    
    def setUp(self):
        '''Configurar o webdriver'''
        self.browser = webdriver.Chrome(r"C:\Users\carlo\Documents\GitHub\Aplicacao_TDD_no_Django\chromedriver.exe")
        
    def tearDown(self):
        '''fechar o browser'''
        self.browser.quit()
        
    def test_buscando_um_novo_animal(self):
        '''Teste se um usuário encontra um animal na pesquisa'''
        # Vini, deseja encontar um novo animal, para adotar
        # Ele enconta o buscar Animal e decide usar o site
        home_page = self.browser.get(self.live_server_url + '/') 
        # Porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.XPATH, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        