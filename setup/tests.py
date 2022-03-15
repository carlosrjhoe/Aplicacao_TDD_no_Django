from select import select
from django.test import LiveServerTestCase
from selenium import webdriver

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
        brand_element = self.browser.find_element_by_class_name('navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        # Ele vê um campo para pesquisar animais pelo nome
        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso')
        # Ele pesquisa por leão e clica no botão pesquisar
        buscar_animal_input.send_keys('leão')
        self.browser.find_element_by_css_selector('form button').click()
        # O site exibe 4 caraquiteristicas do animal pesquisado
        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)
        # Ele desiste de adotar um leão.
        