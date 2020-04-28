#!bin/python
from flask import Flask,jsonify,abort
from flask import make_response
from flask import request


app = Flask(__name__)

questoes_iniciais = [
    {
        'id': 1,
        'pergunta': 'O que quer dizer RPC?',
        'erradas': ['Random Person Changer', 'Renato passa pelo centro' ],
        'corretas': ['Remote procedure call']
    },
    {
        'id': 2,
        'pergunta': 'Quanto vale 2**6?',
        'erradas': [12,36,26,32],
        'corretas': [64]
    }
]

respostas_iniciais = {
        'marcio':{1:'Random Person Changer'},
        'maria':{1:'Remote Procedure Call', 2: 64},
        }
import copy
def reseta():
    global respostas
    global questoes
    respostas = copy.deepcopy(respostas_iniciais)
    questoes = copy.deepcopy(questoes_iniciais)

reseta() #quando eu rodo isso eu crio as variaveis respostas e questoes
         #se sao as variaveis que você deve manipular

@app.route('/autoteste/reseta', methods = ['POST'])
def reseta_request():
    reseta()
    return jsonify({'status':'resetado'}),200

@app.route('/')
def index():
        return "Testes automáticos!"

'''
REPARE:

Você deve alterar os objetos respostas e questoes

NAO ALTERE NUNCA os objetos respostas_iniciais e questoes_iniciais
'''


'''
Ao acessar a URL /autoteste/questoes o usuario deve receber
uma lista completa de todas as questoes
'''
@app.route('/autoteste/questoes/')
def get_questoes():
    return jsonify(questoes)

@app.route('/autoteste/respostas/')
def get_respostas():
    return jsonify(respostas)
'''
Podemos acessar uma questao especifica na URL
/autoteste/questao/<int:q_id>

Se a questao existir, retorne a questao

Se nao existir, retorne um texto de erro e o codigo 404
'''
@app.route("/autoteste/questao/<int:id_questao>/", methods=['GET'])
def get_questoes_id(id_questao):
    for i in questoes:
        if id_questao == i['id']:
            return jsonify(i)
    dic = {}
    dic['erro'] = 'Questao nao encontrada'
    return jsonify(dic), 404
'''
Ao usarmos o verbo POST na url autoteste/questao

queremos criar uma nova questao.

no corpo da mensagem, enviamos o texto da questao (na chave pergunta),
uma lista de alternativas incorretas (na chave erradas) e uma lista
de alternativas corretas (na chave corretas).

Por exemplo:
    {
        'pergunta': 'O que quer dizer RPC?',
        'erradas': ['Random Person Changer', 'Renato passa pelo centro' ],
        'corretas': ['Remote procedure call']
    }

voce deve armazenar essa nova questao e retornar 
uma representacao JSON dela, com o codigo 201 (created)

Se um dos 3 campos estiver faltando, voce deve retornar um 
texto de erro, e o codigo 400
'''
@app.route("/autoteste/questao", methods=['POST'])
def criar_questao():
    new_question = request.json
    tamanho = len(new_question)
    id_dic = len(questoes)
    id_dic += 1
    if tamanho < 3:
        return "Parametros Insuficientes", 400
    new_question['id'] = id_dic
    questoes.append(new_question)
    return jsonify(new_question), 201

'''
Agora melhore sua funçao, fazendo com que, ao ser acrescentada uma
questão, ela automaticamente ganhe a próxima id disponível

(isso não necessariamente vai ser usado no proximo teste, mas vai
ser importante eventualmente)
'''

'''
Ao usarmos o verbo PUT na url 
/autoteste/questao/<int:q_id>/erradas

queremos adicionar mais alternativas erradas à questão.

enviamos, no corpo do request, uma lista de alternativas 
incorretas, e elas devem ser acrescentadas à questão.

por exemplo:
    {"erradas":[1,2,3,4,5]}

Se a questao não existir, devemos retornar o codigo 404
e uma mensagem de erro

Se a questão existir, devemos retornar a questao modificada
'''
@app.route("/autoteste/questao/<int:id_questao>/erradas", methods=['PUT'])
def alterar_erradas(id_questao):
    alternativas = request.json
    for i in questoes:
        if id_questao == i['id']:
            for j in alternativas['erradas']:
                for k in i['erradas']:
                    if j == k:
                        return 'Alternativa errada já presente'
                i['erradas'].append(j)
            return jsonify(i)
    return 'not found', 404
'''
faça o mesmo, adicionando alternativas corretas extras
'''
@app.route("/autoteste/questao/<int:id_questao>/corretas", methods=['PUT'])
def alterar_corretas(id_questao):
    alternativas = request.json
    for i in questoes:
        if id_questao == i['id']:
            for j in alternativas['corretas']:
                for k in i['corretas']:
                    if j == k:
                        return 'Alternativa errada já presente'
                i['corretas'].append(j)
            return jsonify(i)
    return 'not found', 404
'''
Agora melhore suas funções de adição de alternativas,
fazendo com que nao sejam adicionadas alternativas repetidas
'''


'''
Respondendo às perguntas

Fazendo um PUT na URL /autoteste/responder/1
o usuario 'fulano' pode responder à pergunta de id 1

ele deve mandar um json como o seguinte:
    { "usuario": "fulano",
      "resposta": "Remote Procedure Call"}
(o número da pergunta nao aparece no dicionario porque
já está na URL)

A sua resposta deve ser armazenada no dicionario respostas

Relembrando:
respostas_iniciais = {
        'marcio':{1:'Random Person Changer'},
        'maria':{1:'Remote Procedure Call', 2: 64},
        }
é um dicionario, cada pessoa é uma chave
o valor da pessoa é um dicionário
(o valor do maria é {1:'Remote Procedure Call', 2: 64})
olhando para esse dicionario, associado a maria, temos 2
chaves, uma para cada pergunta que ela respondeu.
O valor associado a chave 1 é a resposta que maria deu
para a pergunta 1

Se o usuário ja respondeu a pergunta, devemos retornar um erro 
descritivo e o codigo 409 (confito de edição)

Se ele respondeu com uma alternativa que nao está
nem na lista de corretas nem na lista de incorretas
, devemos retornar
um erro descritivo e o codigo 400 (bad request)

Se o usuário nao está na lista de respostas, devemos adicionar
ele (podemos criar um usuário novo ao enviar uma resposta!)
'''
@app.route("/autoteste/responder/<int:id_questao>", methods=['PUT'])
def responder_questao(id_questao):
    dic_recebido = request.json
    user = dic_recebido["usuario"]
    resposta = dic_recebido["resposta"]
    dicionario = dict()
    dicionario[id_questao] = resposta
    valor = id_questao - 1
    lista = []
    tamanho = len(questoes)
    if id_questao > tamanho:
        return 'questao nao encontrada', 404

    for j in questoes[valor]['erradas']:
        lista.append(j)
    for k in questoes[valor]['corretas']:
        lista.append(k)

    if resposta in lista:
        if user not in respostas:
            respostas[user] = dicionario
            return jsonify('usuario n tava')
        else:
            if id_questao in respostas[user]:
                return 'Questão já respondida', 409 
            respostas[user][id_questao] = resposta
            return jsonify('usuario estava')
    else:
        return 'Resposta não encontrada', 404

        

    
    
        #respostas[dic_recebido['usuario']] = {id_questao: dic_recebido['resposta']}
'''
O usuario deve poder ver quantas perguntas ainda nao
respondeu, quantas acertou e quantas errou.

Acessando a url /autoteste/<username>/resultados com o verbo GET
O usuario deve receber um json como o seguinte:

    {
    "usuario": "fulano",
    "acertos": 3,
    "erros": 2,
    "nao respondidas": 2
    }

Por exemplo, se acessarmos a url /autoteste/maria/resultados,
devemos receber

    {
    "usuario": "maria",
    "acertos": 2,
    "erros": 0,
    "nao respondidas": 0
    }


ja vimos urls como /aluno/<int:id_aluno>
Agora, estamos recebendo uma string em vez de uma id.
Para isso, é só escrever /autoteste/<nome_aluno>/resultados no app.route
'''
@app.route("/autoteste/responder/<nome_aluno>/resultados")
def desempenho(nome_aluno):
    dicionario_aluno = {}
    tamanho_respostas = len(respostas[nome_aluno])
    tamanho_perguntas = len(questoes)
    nao_resp = tamanho_perguntas - tamanho_respostas
    dicionario_aluno['usuario'] = nome_aluno
    dicionario_aluno['nao respondidas'] = nao_resp
    dicionario_aluno['acertos'] = 0
    dicionario_aluno['erros'] = 0
    
     

    for i in respostas[nome_aluno]:
        dic_questoes = get_questoes_id(int(i))
        new_dic = dic_questoes.json
        #return jsonify(i)
        if respostas[nome_aluno][i] == new_dic['corretas'][0]:
            dicionario_aluno['acertos'] += 1
        else:
            dicionario_aluno['erros'] += 1
    return jsonify(dicionario_aluno)



if __name__ == '__main__':
   app.url_map.strict_slashes = False
   app.run(debug=True, host='0.0.0.0',port = 5004)
