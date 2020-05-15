'''
Implemente a função recursiva soma_n_primeiros.

Ela recebe um número e retorna a soma de todos os numeros inteiros até ele

por exemplo, soma_n_primeiros(3) retorna 6 (que é 1+2+3)
por exemplo, soma_n_primeiros(5) retorna 15 (que é 1+2+3+4+5)
por exemplo, soma_n_primeiros(100) retorna 5050 (que é 1+2+3+4+5...+99+100)
por exemplo, soma_n_primeiros(1) retorna 1

O primeiro teste pega o "caso simples": n=1
Depois de passar ele, implemente a recursao
usando que soma_n_primeiros(100) = soma_n_primeiros(99)+100
'''
def soma_n_primeiros(n):
    if n == 0 or n == 1:
        return 1
    return n + soma_n_primeiros(n-1)

'''
Implemente uma função recursiva soma_lista
que recebe uma lista e retorna a soma
de todos os seus elementos 

por exemplo, soma_lista([10,2]) retorna 12
por exemplo, soma_lista([10,2,3]) retorna 15

O primeiro teste pega o "caso simples": listas com 0 ou 1 elemento
Depois de passar ele, implemente a recursao
usando que soma_lista([5, resto]) = soma_lista(resto)+5
'''
def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    elif len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])



'''
Implemente uma função recursiva conta_recursiva, que 
recebe uma lista e um numero, e diz quantas vezes o número
aparece na lista.

Por exemplo conta_recursiva([0,1,2,1,4],1) retorna 2
Por exemplo conta_recursiva([0,1,2,1,4],4) retorna 1
Por exemplo conta_recursiva([0,1,2,1,4],5) retorna 0
Por exemplo conta_recursiva([],5) retorna 0

O primeiro teste pega o "caso simples": listas com 0 ou 1 elemento
Depois de passar ele, implemente a recursao
usando que conta_recursiva([5, resto],5) = conta_recursiva(resto)+1
usando que conta_recursiva([8, resto],5) = conta_recursiva(resto)
'''

def conta_recursiva(lista, numero):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        if numero == lista[0]:
            return 1
        else:
            return 0
            
    primeiro = lista[0]
    if numero == primeiro:
        return conta_recursiva(lista[1:], numero) + 1
    else:
        return conta_recursiva(lista[1:], numero)




'''
Implemente uma função recursiva filtro_recursivo
ela recebe uma lista e um numero e retorna a lista,
tirando todas as vezes que o número aparece

Por exemplo filtro_recursivo([0,1,2,1,4],1) retorna [0,2,4]
Por exemplo filtro_recursivo([0,1,2,1,4],4) retorna [0,1,2,1]
Por exemplo filtro_recursivo([0,1,2,1,4],5) retorna [0,1,2,1,4]
Por exemplo filtro_recursivo([],5) retorna []

O primeiro teste pega o "caso simples": listas com 0 ou 1 elemento
Depois de passar ele, implemente a recursao usando as duas ideias abaixo
filtro_recursivo([5, resto],5) = filtro_recursivo(resto);
filtro_recursivo([8, resto],5) = [8]+filtro_recursivo(resto);
'''
def filtro_recursivo(lista, numero):
    teste = []
    if len(lista) == 0:
        return []
    elif len(lista) == 1:
        if numero != lista[0]:
            return lista

    primeiro = lista[0]
    if numero == primeiro:
        return filtro_recursivo(lista[1:], numero) 
    else:
        teste.append(primeiro)
        return teste + filtro_recursivo(lista[1:], numero)

'''
Defina uma função recursiva palindromo_recursivo, 
que recebe uma string e retorna
True se ela é um palindromo, False caso contrario.

Um palindromo é uma string "espelhada"

Por exemplo palindromo_recursivo('abbabba') retorna True
Por exemplo palindromo_recursivo('aaa') retorna True
Por exemplo palindromo_recursivo('aaaa') retorna True
Por exemplo palindromo_recursivo('aac') retorna False
Por exemplo palindromo_recursivo('a') retorna True
Por exemplo palindromo_recursivo('') retorna True

O primeiro teste pega o "caso simples": listas com 0 ou 1 elemento
Depois de passar ele, implemente a recursao
usando que palindromo('a'+umastring+'a') = palindromo(umastring)
(ou seja, 'a'+umastring+'a' é palindromo quando umastring é palindromo)
note que para palindromo('a'+umastring+'b'), nao precisamos de
recursao: a resposta é False

dicas:
    string[0] é o primeiro elemento
    string[-1] é o ultimo
    string[1:-1] é a string sem o primeiro nem o ultimo
    (teste no terminal do python!)
'''
def palindromo_recursivo(string):
    if len(string) <= 2:
        return True
    if string[0] == string[-1]:
        return palindromo_recursivo(string[1:-1])
    else:
        return False


'''
Implemente uma função recursiva troca_recursiva
ela recebe uma lista e dois numeros (tirar e colocar) 
e retorna a lista, trocando o numero tirar pelo colocar

Por exemplo troca_recursiva([0,1,2,1,4],1,5) retorna [0,5,2,5,4]
Por exemplo troca_recursiva([0,1,2,1,4],4,7) retorna [0,1,2,1,7]
Por exemplo troca_recursiva([0,1,2,1,4],5,6) retorna [0,1,2,1,4]
Por exemplo troca_recursiva([],5) retorna []

O primeiro teste pega o "caso simples": listas com 0 ou 1 elemento
Depois de passar ele, implemente a recursao usando as duas ideias abaixo
troca_recursiva([5, resto],5,3) = [3]+troca_recursiva(resto);
troca_recursiva([8, resto],5,7) = [8]+troca_recursiva(resto)
'''
def troca_recursiva(lista, tirar, colocar):
    if len(lista) == 0:
        return []
    elif len(lista) == 1:
        if lista[0] == tirar:
            lista[0] = colocar
            return lista
        else:
            return lista
    primeiro = lista[0]
    
    colocar_lista = []
    colocar_lista.append(colocar)

    resto_lista = []
    resto_lista.append(primeiro)
    

    if primeiro == tirar:
        return colocar_lista + troca_recursiva(lista[1:], tirar, colocar)
    else:
        return resto_lista + troca_recursiva(lista[1:], tirar, colocar)

'''
Agora, a idéia é implementar uma funcao soma para listas de listas

Por exemplo, considere a lista [[[1,2,3],[4,5],11,4],9,8,4]

O seu primeiro elemento é uma lista
[[1,2,3],[4,5],11,4]

Essa lista tem o primeiro elemento sendo uma lista: [1,2,3]
e o segundo também: [4,5]

Ou seja, uma lista de listas pode conter listas que também contem listas: 
[[[[[1]]],2]] é uma lista de listas válida

Para ajudar, escrevi uma funcao eh_lista que retorna True se um objeto é lista e 
False se não é
'''
def eh_lista(a):
        return isinstance(a,list)


''' 
Escreva uma funcao soma_ll que recebe uma lista de listas e retorna a soma de 
todos os números
Por exemplo, soma_ll([[[1,2,3],[4,5],11,4],9,8,4]) é 46
'''
def soma_ll(lista):

    'verificando'
    if len(lista) == 0 or (len(lista) == 1 and lista[0] == 0 or lista[0] == []):
        return 0
        
    #colocando valor
    valor = lista[0]
    if len(lista) == 1:
        if eh_lista(valor) == False:
            return valor
        else:
            return soma_ll(valor)

    total = 0
    contador = 0

    for i in lista:
        if eh_lista(i):
            contador = soma_ll(i)
        else:
            contador = i
        total += contador
    return total

'''
Implemente uma função anagramas 
que recebe uma palavra e devolve uma lista com todos 
os seus "embaralhamentos" (anagramas)

Por exemplo, anagramas('ab') deve retornar ['ab','ba']
'''

def anagramas(palavra):
    if palavra == "":
        return [palavra]
    else:
        lista = []
        for i in anagramas(palavra[1:]):
            for j in range(len(i)+1):
                lista.append(i[:j]+palavra[0]+i[j:])
        return lista

'''
A partir daqui, não tem nada pra você implementar
'''

import random


import unittest
import sys


class TestStringMethods(unittest.TestCase):

    def test_000_soma_n_primeiros_caso_facil(self):
       self.assertEqual(soma_n_primeiros(1) , 1)


    def test_001_soma_n_primeiros_funciona(self):
       self.assertEqual(soma_n_primeiros(3) , 6 )
       self.assertEqual(soma_n_primeiros(5) , 15 )
       self.assertEqual(soma_n_primeiros(100) , 5050 )
       self.assertEqual(soma_n_primeiros(10) , 55)
    
    def test_002_soma_n_primeiros_eh_recursiva(self):
        sys.setrecursionlimit(50)
        try:
            a=soma_n_primeiros(1000)
            print(a)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_100_soma_lista_casos_faceis(self):
        self.assertEqual(soma_lista([1]),1)
        self.assertEqual(soma_lista([]),0)
        self.assertEqual(soma_lista([-3]),-3)
    
    def test_101_soma_lista_funciona(self):
        self.assertEqual(soma_lista([1,2,30]),33)
        self.assertEqual(soma_lista([1,3,5]),9)
        self.assertEqual(soma_lista([10,2,3,4]),19)
        self.assertEqual(soma_lista([-1,-2,-3,-4]),-10)
    

    def test_102_soma_lista_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            soma_lista([1]*100)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_200_conta_caso_facil(self):
         self.assertEqual(conta_recursiva([],5), 0)
         self.assertEqual(conta_recursiva([5],5), 1)
         self.assertEqual(conta_recursiva([1],5), 0)
    
    def test_201_conta_pequena(self):
         self.assertEqual(conta_recursiva([0,1,2,1,4],1), 2)
         self.assertEqual(conta_recursiva([0,1,2,1,4],4), 1)
         self.assertEqual(conta_recursiva([1,1],1), 2)
         self.assertEqual(conta_recursiva([1,1],2), 0)
         self.assertEqual(conta_recursiva([0,1,2,1,4],5), 0)
   
    def test_202_conta_recursiva(self):
        sys.setrecursionlimit(50)
        try:
            conta_recursiva([1]*100,1)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_301_filtro_caso_facil(self):
         self.assertEqual(filtro_recursivo([],5), [])
         self.assertEqual(filtro_recursivo([1],5), [1])
    
    def test_302_filtro_funciona(self):
         self.assertEqual(filtro_recursivo([0,1,2,1,4],1), [0,2,4])
         self.assertEqual(filtro_recursivo([0,1,2,1,4],4), [0,1,2,1])
         self.assertEqual(filtro_recursivo([1,1],1), [])
         self.assertEqual(filtro_recursivo([1,1],2), [1,1])
         self.assertEqual(filtro_recursivo([0,1,2,1,4],5), [0,1,2,1,4])
   
    
    def test_303_filtro_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            filtro_recursivo([1]*100,1)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_400_palindromo_caso_facil(self):    
        self.assertEqual(palindromo_recursivo('a') , True)
        self.assertEqual(palindromo_recursivo('') , True)

    def test_401_palindromo_funciona(self):    
        self.assertEqual(palindromo_recursivo('abbabba'), True)
        self.assertEqual(palindromo_recursivo('aaa') , True)
        self.assertEqual(palindromo_recursivo('aaaa') , True)
        self.assertEqual(palindromo_recursivo('aac') , False)

    
    def test_402_palindromo_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            palindromo_recursivo('a'*100)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
    
    def test_500_troca_caso_facil(self):
         self.assertEqual(troca_recursiva([],5,2), [])
         self.assertEqual(troca_recursiva([1],5,4), [1])
         self.assertEqual(troca_recursiva([5],5,4), [4])
    
    def test_501_troca_funciona(self):
         self.assertEqual(troca_recursiva([0,1,2,1,4],1,7), [0,7,2,7,4])
         self.assertEqual(troca_recursiva([0,1,2,1,4],4,9), [0,1,2,1,9])
         self.assertEqual(troca_recursiva([1,1],1,2), [2,2])
         self.assertEqual(troca_recursiva([1,1],2,7), [1,1])
         self.assertEqual(troca_recursiva([0,1,2,1,4],5,3), [0,1,2,1,4])
         self.assertEqual(troca_recursiva([0,1,2,1,4],0,0), [0,1,2,1,4])
         self.assertEqual(troca_recursiva([0,1,2,1,4],9,9), [0,1,2,1,4])
   
    
    def test_502_troca_recursivo(self):
        sys.setrecursionlimit(50)
        try:
            troca_recursiva([1]*100,1,2)
            self.fail('a sua função é recursiva?')
        except RecursionError:
            print('')
            print('correto, sua funcao é recursiva')
        finally:
            sys.setrecursionlimit(1000)
   
    def test_600_soma_ll(self):
        self.assertEqual(soma_ll([1,2,3]),6)
        self.assertEqual(soma_ll([1,2,3,4]),10)
        self.assertEqual(soma_ll([-1,-2,-3,-4]),-10)
        self.assertEqual(soma_ll([1]),1)
        self.assertEqual(soma_ll([]),0)
        self.assertEqual(soma_ll([-3]),-3)
        self.assertEqual(soma_ll([[],[]]),0)
        self.assertEqual(soma_ll([[1],[2]]),3)
        self.assertEqual(soma_ll([[[1,2,3],[4,5],11],9,8]),43)
        self.assertEqual(soma_ll([[[1,2,3],[4,5],11,4],9,8,4]),51)
        self.assertEqual(soma_ll([[-1],[1]]),0)
        self.assertEqual(soma_ll([[1],[[2],1]]),4)
    



    def test_700_anagramas(self):
        a = anagramas('abc')
        self.assertEqual(set(a),set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        a = anagramas('abcd')
        self.assertEqual(set(a),set(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']))
        a = anagramas('abca')
        self.assertEqual(set(a),set(['abca', 'abac', 'acba', 'acab', 'aabc', 'aacb', 'baca', 'baac', 'bcaa', 'bcaa', 'baac', 'baca', 'caba', 'caab', 'cbaa', 'cbaa', 'caab', 'caba', 'aabc', 'aacb', 'abac', 'abca', 'acab', 'acba']))




    


    
    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

try:
    from recursao_segundo_arquivo_respostas import *
except:
    pass

runTests()

