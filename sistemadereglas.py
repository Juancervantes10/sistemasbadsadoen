from reglas import *

class sistemadereglas(KnowledgeEngine):
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="si")), (reglas(obs="si")),(reglas(mes="si")), (reglas(cepi="si")))
  def m1(self):
    print("Tiene buena higiene dental")
        
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="si")), (reglas(obs="si")), (reglas(mes="si")), (reglas(cepi="no")))
  def m2(self):
    print('Tiene mala higiene dental')    
        
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="si")), (reglas(obs="si")), (reglas(mes="no")), (reglas(cepi="si")))
  def m3(self):
    print('Debe mejorar su higiene dental  ')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="si")), (reglas(obs="si")), (reglas(mes="no")), (reglas(cepi="no")))
  def m4(self):
    print('Tiene un transtorno llamado blancorexia')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="si")), (reglas(obs="no")), (reglas(mes="si")), (reglas(cepi="si")))
  def m5(self):
    print('Deberia usar enjuage bucal')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="si")), (reglas(obs="no")), (reglas(mes="si")), (reglas(cepi="no")))
  def m6(self):
    print('Mejora su hingiene dental')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="si")), (reglas(obs="no")), (reglas(mes="no")), (reglas(cepi="si")))
  def m7(self):
    print('Se cepilla los dientes todos los dias del mes')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="si")), (reglas(obs="no")), (reglas(mes="no")), (reglas(cepi="no")))
  def m8(self):
    print('No se cepilla los dientes todos los dias del mes')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="no")), (reglas(obs="si")), (reglas(mes="si")), (reglas(cepi="si")))
  def m9(self):
    print('Deberia cepillarse todos los dias')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="no")), (reglas(obs="si")), (reglas(mes="si")), (reglas(cepi="no")))
  def m10(self):
    print('Deberia cepillarse todos los dias y usar enjuage bucal')  
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="no")), (reglas(obs="si")), (reglas(mes="no")), (reglas(cepi="si")))
  def m11(self):
    print('reducir las veces que se cepilla al dia, cepillarse todos los dias y usar enjuage bucal')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="no")), (reglas(obs="si")), (reglas(mes="no")), (reglas(cepi="no")))
  def m12(self):
    print('Deberia cambiar las cantidades de veces que se cepilla al dia')  
        
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="no")), (reglas(obs="no")), (reglas(mes="si")), (reglas(cepi="si")))
  def m13(self):
    print('Debe cepillarse los dientes diarios y seguir usando el enjuague bucal')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="no")), (reglas(obs="no")), (reglas(mes="si")), (reglas(cepi="no")))
  def m14(self):
    print('si se cepilla los dientes todos los dias y todas las semanas')
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="no")), (reglas(obs="no")), (reglas(mes="no")), (reglas(cepi="si")))
  def m15(self):
    print('no se cepilla los dientes todos los dias y toda las semanas') 
    
  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="no")), (reglas(obs="no")), (reglas(mes="no")), (reglas(cepi="no")))
  def m16(self):
    print('elimina todos los resudios entre los dientes') 

  @Rule(AND(NOT(reglas(cepillare="si"))), (reglas(enjuage="si")), (reglas(obs="si")), (reglas(mes="si")),(reglas(cepi="si")))
  def m17(self):
    print('Deberias usar ceda dental para eliminar todo el resudio que hay entre los dientes')

  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="no")), (reglas(obs="no")),(reglas(mes="no")), (reglas(cepi="no")))
  def m18(self):
    print("Debes comenzar a mejorar tu higiene denta")

  @Rule(AND(reglas(cepillare="si")), (reglas(enjuage="si")), (reglas(obs="si")),(reglas(mes="si")), (reglas(cepi="si")))
  def m18(self):
    print("Tienes la mejor Higiene dental")
        