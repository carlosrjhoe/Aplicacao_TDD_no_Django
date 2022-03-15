from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimailMobelTestCase(TestCase):
    
    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal = 'leão',
            predador = 'sim',
            venenozo = 'não',
            domestico = 'não'
        )

    def test_animal_cadastrado_com_caracteristicas(self):
        '''teste que verifica se o animal está cadastrado com sua respectivas caracteristicas'''
        self.assertEqual(self.animal.nome_animal, 'leão')
        