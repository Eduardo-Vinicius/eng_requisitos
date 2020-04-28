import requests
import unittest

url = 'http://localhost:5004/autoteste/'

class TestStringMethods(unittest.TestCase):


    def atest_000_todas_questoes(self):
        r = requests.get(url+'questoes')
        self.assertEqual(type(r.json()),type([]))
        self.assertTrue(len(r.json())>=2)
    
    #essa funcao não é um teste, mas auxilia os testes    
    def verifica_questao(self,texto_questao):
        r = requests.get(url+'questoes')
        lista_questoes = r.json()
        for dic_questao in lista_questoes:
            if dic_questao['pergunta'] == texto_questao:
                return True
        return False

    def atest_001_questoes_presentes(self):
        self.assertTrue(self.verifica_questao('O que quer dizer RPC?'))
        self.assertFalse(self.verifica_questao('Is this the real life?'))
        self.assertFalse(self.verifica_questao('Or is it just fantasy?'))
        self.assertTrue(self.verifica_questao('Quanto vale 2**6?'))

    def atest_002_respostas(self):
        r = requests.get(url+'respostas')
        self.assertEqual(type(r.json()),type({}))
        self.assertTrue(len(r.json())>=2)
    
    def atest_003_respondedores_presentes(self):
        r = requests.get(url+'respostas')
        dic_devolvido = r.json()
        self.assertTrue('marcio' in dic_devolvido)
        self.assertFalse('bonde' in dic_devolvido)

    def atest_004_busca_questao(self):
        r = requests.post(url+'reseta')
        r = requests.get(url+'questao/1')
        dic_retornado = r.json()
        self.assertEqual(dic_retornado['id'],1)
        self.assertEqual(dic_retornado['corretas'],['Remote procedure call'])
        r = requests.get(url+'questao/2')
        dic_retornado = r.json()
        self.assertEqual(dic_retornado['id'],2)
        self.assertIn(12,dic_retornado['erradas'])

    def atest_005_cria_questao(self):
        q1 = {
            'pergunta': 'Quanto vale 3+4?',
            'erradas': [12,36,26,32],
            'corretas': [7]
        }

        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
        self.assertTrue(self.verifica_questao(q1['pergunta']))

    def atest_006_reset(self):
        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }

        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
        self.assertTrue(self.verifica_questao(q1['pergunta']))
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
        self.assertFalse(self.verifica_questao(q1['pergunta']))
        self.assertTrue(self.verifica_questao('O que quer dizer RPC?'))
        self.assertTrue(self.verifica_questao('Quanto vale 2**6?'))
        
        r = requests.get(url+'questoes')
        self.assertEqual(len(r.json()),2)

    def atest_007_questao_inexistente(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
        r = requests.get(url+'questao/1')
        self.assertEqual(r.status_code,200)
        dic_retornado = r.json()
        self.assertEqual(dic_retornado['id'],1)
        self.assertEqual(dic_retornado['corretas'],['Remote procedure call'])
        r = requests.get(url+'questao/10')
        self.assertEqual(r.status_code,404)
        dic_retornado = r.json()
        self.assertEqual(dic_retornado['erro'],'Questao nao encontrada')
    
    def atest_008_questao_incompleta(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }
       
        q_copy = q1.copy()
        del q_copy['pergunta']
        r = requests.post(url+'questao',json = q_copy)
        self.assertEqual(r.status_code,400)


        q_copy = q1.copy()
        del q_copy['erradas']
        r = requests.post(url+'questao',json = q_copy)
        self.assertEqual(r.status_code,400)


        q_copy = q1.copy()
        del q_copy['corretas']
        r = requests.post(url+'questao',json = q_copy)
        self.assertEqual(r.status_code,400)

        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
    
    def atest_009_questao_adiciona_alternativas_erradas(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        erradas = {}
        erradas['erradas'] = ['roberto pula o caminhao']
        r = requests.put(url+'questao/1/erradas', json = erradas)
        self.assertEqual(r.status_code,200)
        
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['erradas']),3)
        self.assertEqual(devolvida['erradas'][-1],'roberto pula o caminhao')

        #tentei colocar de novo
        r = requests.put(url+'questao/1/erradas', json = erradas)
        
        #mas isso nao tem efeito adicional
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['erradas']),3)
    
    def atest_010_adiciona_alternativas_erradas_404(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        erradas = {}
        erradas['erradas'] = ['roberto pula o caminhao']

        #se tento adicionar em uma questao que nao existe
        r = requests.put(url+'questao/3/erradas', json = erradas)
        self.assertEqual(r.status_code,404)
    
    def atest_011_questao_adiciona_alternativas_corretas(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        corretas = {}
        corretas['corretas'] = ['roberto pula o caminhao']
        r = requests.put(url+'questao/1/corretas', json = corretas)
        self.assertEqual(r.status_code,200)
        
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['corretas']),2)
        self.assertEqual(devolvida['corretas'][-1],'roberto pula o caminhao')

        #tentei colocar de novo
        r = requests.put(url+'questao/1/corretas', json = corretas)
        
        #mas isso nao tem efeito adicional
        r = requests.get(url+'questao/1')
        devolvida = r.json()
        self.assertEqual(len(devolvida['corretas']),2)
    
    def atest_012_adiciona_alternativas_corretas_404(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        corretas = {}
        corretas['corretas'] = ['roberto pula o caminhao']

        #se tento adicionar em uma questao que nao existe
        r = requests.put(url+'questao/3/corretas', json = corretas)
        self.assertEqual(r.status_code,404)

    def test_013_responder(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
        r1 = {'usuario':'marcio',
              'resposta':12}
        r = requests.put(url+'responder/2', json=r1)
        self.assertEqual(r.status_code,200)
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        self.assertEqual(len(dic_recebido),2)
        self.assertEqual(len(dic_recebido['marcio']),2)

        
        r = requests.put(url+'responder/2', json=r1)
        self.assertEqual(r.status_code,409)
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        self.assertEqual(len(dic_recebido),2)
        self.assertEqual(len(dic_recebido['marcio']),2)
        
        r2 = {'usuario':'don juan',
              'resposta':12}
        r = requests.put(url+'responder/2', json=r2)
        self.assertEqual(r.status_code,200)
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        self.assertEqual(len(dic_recebido),3)
        self.assertEqual(len(dic_recebido['don juan']),1)
    
    def test_013b_responder_questao_invalida(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        #nao consigo responder a questao 3
        r1 = {'usuario':'marcio',
              'resposta':12}
        r = requests.put(url+'responder/3', json=r1)
        self.assertEqual(r.status_code,404)
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        self.assertEqual(len(dic_recebido),2)
        self.assertEqual(len(dic_recebido['marcio']),1)
        
        #agora crio a questao e tento novamente
        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }

        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)

        #minha segunda tentativa
        r1 = {'usuario':'marcio',
              'resposta':12}
        r = requests.put(url+'responder/3', json=r1)
        self.assertEqual(r.status_code,200)
        r = requests.get(url+'respostas')
        dic_recebido = r.json()
        self.assertEqual(len(dic_recebido),2)
        self.assertEqual(len(dic_recebido['marcio']),2)

    def test_014_desempenho(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)
       
        r = requests.get(url+'maria/resultados')
        self.assertEqual(r.json()['usuario'],'maria')
        self.assertEqual(r.json()['acertos'],2)
        self.assertEqual(r.json()['erros'],0)
        self.assertEqual(r.json()['nao respondidas'],0)
    
    def test_100_id_crescente(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }
        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
        r = requests.get(url+'questao/3')
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['pergunta'],q1['pergunta'])
        


    
    def test_101_sem_ids_repetidas(self):
        r = requests.post(url+'reseta')
        self.assertEqual(r.status_code,200)

        q1 = {
            'pergunta': 'Um tijolo pesa um quilo mais meio tijolo. Quanto pesa um tijolo inteiro?',
            'erradas': [12,36,26,32],
            'corretas': [2]
        }
        r = requests.post(url+'questao',json = q1)
        self.assertEqual(r.status_code,201)
        q2 = {
            'pergunta': 'Quanto vale 3+4?',
            'erradas': [12,36,26,32],
            'corretas': [7]
        }
        r = requests.post(url+'questao',json = q2)
        self.assertEqual(r.status_code,201)
        q3 = {
            'pergunta': 'Whate is the brother?',
            'erradas': [12,36,26,32],
            'corretas': ['uma geracao marcante']
        }
        r = requests.post(url+'questao',json = q3)
        self.assertEqual(r.status_code,201)
    

        r = requests.get(url+'questoes')
        lista_retornada = r.json()
        self.assertTrue(len(lista_retornada) == 5)

        for dic in lista_retornada:
            self.assertIn('id',dic)

        ids = []
        for dic in lista_retornada:
            ids.append(dic['id'])
        if (len(set(ids)) != len(ids)):
            self.fail('existe alguma id repetida na sua lista de questoes!')



    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
