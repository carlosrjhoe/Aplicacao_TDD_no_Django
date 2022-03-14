from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    
    def setUp(self):
        '''Configurar o webdriver'''
        self.browser = webdriver.Chrome(r"C:\Users\carlo\Documents\GitHub\Aplicacao_TDD_no_Django\chromedriver.exe")
        
    def tearDown(self):
        '''fechar o browser'''
        self.browser.quit()
        
    def test_para_verificar_a_janela_esta_ok(self):
        self.browser.get(self.live_server_url)
        
    def test_falhador(self):
        '''teste de exemplo de erro'''
        self.fail('Teste falhou!')
        
    def test_buscando_um_novo_animal(self):
        '''Teste se um usuário encontra um animal na pesquisa'''
        