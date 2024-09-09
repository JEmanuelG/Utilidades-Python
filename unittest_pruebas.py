# Unittest - Sirve para crear pruebas dentro del propio código

def multiplicar(numero1, numero2):
    return numero1 * numero2

resultado = multiplicar(2, 4)
print(resultado)


import unittest

class Pruebas(unittest.TestCase):
   
    def test(self):
        self.assertEqual(multiplicar(8, 2), 16)

        # metemos un error para ejemplificar
        #self.assertEqual(multiplicar(8, 2), 10)

if __name__ == '__main__':
    unittest.main()

