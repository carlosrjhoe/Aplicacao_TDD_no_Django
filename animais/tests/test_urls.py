import imp
from django.test import TestCase
from django.urls import reverse
from animais.views import index

class AnimaisURLSTesttCase(TestCase):
    
    def test_rota_url_utiliza_view_index(self):
        '''teste de a home da aplicação utiliza a função index da view'''
        root = reverse('/')
        self.assertEqual(root.func, index)
        