import imp
from urllib import request, response
from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index

class AnimaisURLSTesttCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_rota_url_utiliza_view_index(self):
        '''teste de a home da aplicação utiliza a função index da view'''
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
        