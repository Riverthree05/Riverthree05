#importacion del modulo unittest para poder reailzar las pruebas unitarias
import unittest

#importar de la clase calculadora desde el archivo calculadora.py
from calculadora import Calculadora

#definir la clase de pruebas que hereda de unittest.TestCase

class Testcalculadora(unittest.TestCase):
    
    #metodo que se ejecuta en cada prueba
    def setUp(self):
        self.calc = Calculadora()
        
        #prueba del metodo suma
    def test_suma(self):
            #prueba de la suma de dos numeros positivos
            self.assertEqual(self.calc.sumar(5,7), 12)
            #prueba de la suma de dos ceros
            self.assertEqual(self.calc.sumar(0,0), 0)
            
    def test_resta(self):
            #prueba de la resta de dos numeros positivos
            self.assertEqual(self.calc.restar(5,7), -2)
            #prueba de la resta de dos ceros
            self.assertEqual(self.calc.restar(5,5), 0)
    
    def test_multiplicacion(self):
            #prueba multuplicacion de dos numeros positivos
            self.assertEqual(self.calc.multiplicar(5,7), 35)
            #prueba de la multiplicacion por cero
            self.assertEqual(self.calc.multiplicar(5,0), 0)
            #prueba de la multipliacion de un numero negatico por un positivo
            self.assertEqual(self.calc.multiplicar(-5,7), -35)
    
    def test_division(self):
            #prueba division de exacta
            self.assertEqual(self.calc.dividir(10,5), 2)
            #prueba de la division con resultado decimal 
            self.assertAlmostEqual(self.calc.dividir(10,3), 3.3333333333333335)
            #prueba de la division presiodica usando assertAkmostEqual
            self.assertAlmostEqual(self.calc.dividir(1,3), 0.3333333333333333)
            
#Bloque condicional que permite ejecutar las pruebas directamente
if __name__ == '__main__':
    #inicialixar la ejecucuion de todas las pruebas definidas en la clase
    unittest.main()

