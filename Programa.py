import requests
import time
from random import randint
import json
import os

class TelegramBot:
    def __init__(self):
        iTOKEN  = '1835081325:AAHi3XKV_N_GHb_AB7hLTq8njtYar2IEWqA'
        self.iURL = f'https://api.telegram.org/bot{iTOKEN}/'

    def Iniciar(self):
        iUPDATE_ID = None
        while True:
            iATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
            IDADOS = iATUALIZACAO["result"]
            if IDADOS:
                for dado in IDADOS:
                    iUPDATE_ID = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.gerar_respostas(mensagem, primeira_mensagem)
                    self.responder(resposta, chat_id)

    def ler_novas_mensagens(self, iUPDATE_ID):
        iLINK_REQ = f'{self.iURL}getUpdates?timeout=5'
        if iUPDATE_ID:
            iLINK_REQ = f'{iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(iLINK_REQ)
        return json.loads(iRESULT.content)

    def gerar_respostas(self, mensagem, primeira_mensagem):
        print('mensagem do cliente: ' + str(mensagem))
        if primeira_mensagem == True or mensagem.lower() in ('falame', 'fala'):
            return f'''Olá seja bem vindo(a) a FalaMe, temos alguns tipos de frases para você, qual você escolhe?{os.linesep}1 - Frases de Dúvida{os.linesep}2 - Frases para Refletir{os.linesep}3 - Frases sobre a Vida'''
        elif mensagem == '1':
            mandar = randint(1, 3)
            if mandar == 1:
                return f'''Nossas dúvidas são traidoras e nos fazem perder o que, com frequência, poderíamos ganhar, por simples medo de arriscar.{os.linesep}William Shakespeare'''
            if mandar == 2:
                return f'''O problema do mundo de hoje é que as pessoas inteligentes estão cheias de dúvidas, e as pessoas idiotas estão cheias de certezas...{os.linesep}Bertrand Russell'''
            if mandar == 2:
                return f'''Os únicos limites das nossas realizações de amanhã são as nossas dúvidas e hesitações de hoje.{os.linesep}Franklin Roosevelt'''
        elif mensagem == '2':
            mandar = randint(1, 3)
            if mandar == 1:
                return f'''O medo é um preconceito dos nervos. E um preconceito, desfaz-se - basta a simples reflexão.{os.linesep}Machado de Assis'''
            if mandar == 2:
                return f'''Entre as penas humanas, a mais dolorosa é a de prever muitas coisas e não poder fazer nada.{os.linesep}Heródoto'''
            if mandar == 2:
                return f'''Nunca a natureza é tão aviltada como quando a ignorância supersticiosa tem a arma do poder.{os.linesep}Voltaire'''
        elif mensagem == '3':
            mandar = randint(1, 3)
            if mandar == 1:
                return f'''Ser feliz sem motivo é a mais autêntica forma de felicidade.{os.linesep}Carlos Drummond de Andrade'''
            if mandar == 2:
                return f'''Viver é a coisa mais rara do mundo. A maioria das pessoas apenas existe.{os.linesep}Oscar Wilde'''
            if mandar == 3:
                return f'''A única alegria no mundo é começar. É bom viver porque viver é começar sempre, a cada instante.{os.linesep}Cesare Pavese'''
        else:
            return f'''Não entendi'''


    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("respondi: " + str(resposta))


bot = TelegramBot()
bot.Iniciar()