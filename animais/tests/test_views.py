from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestcase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'calopsita',
            predador = 'não',
            venenozo = 'não',
            domestico = 'sim'
        )
        
    def test_index_view_retorna_caracteristicas_do_animal(self):
        '''teste que verifica se a index retorna a caracteristicas do animal pesquizado'''
        response = self.client.get('/',
            {'buscar':'calopsita'}
        )
        caracteristica_animal_pesquizado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_animal_pesquizado[0].nome_animal, 'calopsita')