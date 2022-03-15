from urllib import response
from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

class IndexViewTestcase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        
    def test_index_view_retorna_caracteristicas_do_animal(self):
        '''teste que verifica se a index retorna a caracteristicas do animal pesquizado'''
        response = self.client.get('/',
            {'caracteristicas':'resultado'}
        )        
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        