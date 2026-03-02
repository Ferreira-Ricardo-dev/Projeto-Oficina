#Arquivo para testar as classes e funções
import unittest

from users import User

class TestUser(unittest.TestCase):
    """Testes para a classe User"""
    def password_logic_test(self):
        user = User('ricardo', 'farias', 'ferreir@2006', 'rick12@')
        
        self.assertEqual('ferreir@2006', user._User_password)

unittest.main()