# -*- coding: utf-8 -*-
'''
Created on Sat Jun 13 06:49:19 2020

@author: berna
'''
#%% Fontes de ideias para melhoria
#https://medium.com/@jonathanferreiras/chatbot-python-whatsapp-e9c1079da5a
#https://github.com/JuanCarvalho/whatsbot/blob/master/whats_bot.py
#https://www.messagebird.com/en/omnichannel-widget/?utm_source=google&utm_medium=cpc&utm_campaign=ROW%20%7C%20ENG%20%7C%20NonBrand%20%7C%20OCW%20%7C%20OSS%20%7C%20EK0121&utm_term=Chatbot%20%7C%20Whatsapp&utm_source_custom=google&utm_medium_custom=cpc&utm_term_custom=Chatbot%20%7C%20Whatsapp&utm_campaign_custom=ROW%20%7C%20ENG%20%7C%20NonBrand%20%7C%20OCW%20%7C%20OSS%20%7C%20EK0121&utm_content=439067137143&utm_location=1001541&utm_keyword=%2Bchatbot%20%2Bwhatsapp&gclid=Cj0KCQjwz4z3BRCgARIsAES_OVenaIlYCiWEmvkaGYjOd6gUkByR6An_ESq3Fmu7brnWk5fNzoqBKO0aArReEALw_wcB
#https://www.treinaweb.com.br/blog/criando-um-chatbot-com-python/
#https://blog.usejournal.com/build-a-basic-news-fetching-whatsapp-bot-in-python-under-60-lines-of-code-2d992faf7f79
#https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio

import os
import time
import numpy as np
import re
import requests
import json
from chatterbot import ChatBot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys
sys.path.insert(0, r'C:\Users\berna\Desktop\Hackathon CCR')



class wppbot:
    # O local de execução do nosso script
    dir_path = os.getcwd()

    def __init__(self, nome_bot):
        '''
        Inicia o bot e abre o WhatsApp
        Está sendo usado o FireFox (geckodriver) porque o Chrome não tem suporte a emojis
        Já há previsão de comando para treinar o bot para conversar via IA
        Deverá ser evoluída para API.
        '''
        
        self.bot = ChatBot(nome_bot)
        # self.bot.set_trainer(ListTrainer)
        
        # #Chrome
        # self.chrome = self.dir_path + '\chromedriver.exe'
        # self.options = webdriver.ChromeOptions()
        # self.options.add_argument(r'user-data-dir='+self.dir_path+'\profile\wpp')
        # self.driver = webdriver.Chrome(self.chrome, chrome_options=self.options)
        
        # FireFox
        self.ffox = self.dir_path + '\geckodriver.exe'
        self.driver = webdriver.Firefox(executable_path = self.ffox)
        
        # Abre o whatsappweb
        self.driver.get('https://web.whatsapp.com/')
        # Espera o usuário inserir o QR Code e carregar a página
        self.driver.implicitly_wait(15)
        
    
    
    def acompanhar_conversas(self):
        ''' Monitora as mensagens mais recentes em busca de algum comando que dispare o bot'''
        try:
            # Identifica conversas recentes
            elements = self.driver.find_elements_by_xpath("//div[@class='_210SC']")
            
            # Cria um dicionário com nome_conversa : ultima_msg para cada uma das conversas recentes
            msgs = {ee.find_elements_by_xpath(".//div[@class='_3CneP']")[0].find_elements_by_xpath(".//span[@dir='auto']")[0].get_attribute('title') : 
                    ee.find_elements_by_xpath(".//span[@class='_2iq-U']/span[@class='_3ko75 _5h6Y_ _3Whw5']")[0].text 
                    for ee in elements}
            return msgs
        
        except:
            # Em caso de erro retorna um dicionário vazio para não interromper o script
            return {}
    
    
    
    def abre_conversa(self, contato):
        """ Abre a conversa com um contato especifico """
        try:
            # Seleciona a caixa de pesquisa de conversa
            self.caixa_de_pesquisa = self.driver.find_element_by_class_name('_3e4VU')
            # Digita o nome ou numero do contato/grupo
            self.caixa_de_pesquisa.send_keys(contato)
            time.sleep(1)
            # Seleciona o contato
            self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(contato))
            # Entra na conversa
            self.contato.click()
            time.sleep(1)
        except:
            print('')
    

        
    def envia_msg(self, msg):
        """ Envia uma mensagem para a conversa aberta """
        try:
            # Seleciona acaixa de mensagem
            self.caixa_de_mensagem = self.driver.find_elements_by_class_name('_3FRCZ')[1]
            
            # Digita a mensagem. Se for uma lista digita cada frase em uma linha.
            if isinstance(msg, list):
                for m in msg:
                    self.caixa_de_mensagem.send_keys(m)
                    self.caixa_de_mensagem.send_keys(Keys.SHIFT + Keys.ENTER)
            else:
                self.caixa_de_mensagem.send_keys(msg)
            
            
            time.sleep(2)
            # Seleciona botão enviar
            self.botao_enviar = self.driver.find_element_by_class_name('_1U1xa')
            # Envia msg
            self.botao_enviar.click()
            time.sleep(1)
            
        except Exception as e:
            # Informa o erro caso ocorra
            print("Erro ao enviar msg", e)


    '''
    Respostas às requisições dos usuários.
    Quando integrado com as bases de dados e localização atual do usuário, retornará as distâncias reais aos locais solicitados
    '''
    def saudacao(self):
        # Mensagem enviada quando o usuário se cadastrar
        self.envia_msg(['*BIMO*', 
                        '',
                        'Oi, sou o BIMO, seu mordomo pessoal!',
                        'Use .. no início para falar comigo',
                        'Digite "..ajuda" para ter acesso à lista de comandos'])


    def ajuda(self):
        '''
        Lista de comandos válidos. 
        O comando perigo não retorna nnhuma mensagem por segurança do usuário
        '''
        return ['*BIMO*',
                '',
                'Os comandos válidos são:',
                '..sanitário - distância até o banheiro gratuito mais próximo',
                '..banho - distância ao chuveiro mais próximo',
                '..comida - distancia até o próximo retaurante',
                '..sono - hotel mais próximo',
                '..saude - para saber onde está o posto itinerante',
                '..perigo - enviar sua localização à policia',
                '',
                'O que deseja fazer?']             
    
    def comida(self):
        # Identifica o restaurante mais próximo e promoções nas redondezas
        dist1 = np.random.randint(1, 50)
        dist2 = np.random.randint(1, 50)
        msg = ['*BIMO*',
               '',
               'O restaurante mais próximo é a Tia Xica, a ' + str(dist1) + ' km. O valor do kg é de R$ 28,99',
               '',
               'O Restaurante do Caminhoneiro está em promoção, saindo a R$ 15,49 o kg! É só digir por ' + str(dist1 + dist2) + ' km']
        return msg
    
    def banho(self):
        # Chuveiros pago e gratuito mais próximos 
        dist1 = np.random.randint(1, 50)
        dist2 = np.random.randint(1, 50)
        return ['*BIMO*',
                '',
                'O chuveiro mais próximo está a ' + str(dist1) + ' km, no Posto de Gasolina. É necessário abastecer ou pagar uma taxa de R$ 30,00 para usá-lo',
                'O chuveiro *gratuito* mais próximo está a ' + str(dist1 + dist2) + ' km, no SAU da CCR']
    
    def sanitário(self):
        # Sanitário mais próximo
        dist = np.random.randint(1, 50)
        msg = ['*BIMO*',
               '',
               'O sanitário mais próximo está a ' + str(dist) + ' km, no Posto de Gasolina']
        
        if dist > 30:
            # Mensagem encorajadora caso o banheiro esteja distante
            msg.append('É longe, mas você aguenta!')
        
        return msg
    
    def sono(self):
        # Locais para pouso mais próximos. Informa se a região é segura
        dist = np.random.randint(1, 50)
        return ['*BIMO*',
                '',
                'O repouso mais próximo é o Hotel BIMO a ' + str(dist) + ' km',
                'Cuidado! Foram reportados diversos assaltos na região!']
    
    def saude(self):
        # Local do posto de saúde itinerante, conforme informações coletadas com a concessionária
        dist = np.random.randint(1, 200)
        return ['*BIMO*',
                '',
                'Hoje o posto itinerante está próximo ao trevo de Binópolis a ' + str(dist) + ' km daqui',
                'Quer que a gente chame uma ambulância?']
    
    def nao_encontrado(self):
        # Mensagem de comando não encontrado
        return ['*BIMO*',
                '',
                'Que pena! Esse comando ainda não existe.']
    

    def geo_fence(self):
        # Identifica que o usuário entrou em uma concessão CCR e o informa disso. Envia também o número do SAU, caso necessáro
        self.envia_msg(['*BIMO*',
                        '',
                        'Você acaba de entrar em uma rodovia CCR.',
                        'O número do SAU é 0800-CCR-CCR'])
    
    
    
    

#%% Agregdor de notícias sobre o tema específico

    # def noticias(self):

    #     req = requests.get('https://newsapi.org/v2/top-headlines?sources=globo&pageSize=5&apiKey=f6fdb7cb0f2a497d92dbe719a29b197f')
    #     noticias = json.loads(req.text)

    #     for news in noticias['articles']:
    #         titulo = news['title']
    #         link = news['url']
    #         new = 'BIMO: ' + titulo + ' ' + link + '\n'

    #         self.caixa_de_mensagem.send_keys(new)
    #         time.sleep(1)
    
    
#%% ChatBot com IA
# from chatterbot.trainers import ListTrainer


    # def treina(self,nome_pasta):
    #     for treino in os.listdir(nome_pasta):
    #         conversas = open(nome_pasta+'/'+treino, 'r').readlines()
    #         self.bot.train(conversas)
    
    
    
    # def ultima_msg_conversa(self):
    #     ''' Captura a ultima mensagem da conversa '''
    #     try:
    #         post = self.driver.find_elements_by_class_name('_2hqOq')
    #         ultimo = len(post) - 1
    #         # O texto da ultima mensagem
    #         texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
    #         return texto
    #     except:
    #         pass



    # def aprender(self,ultimo_texto,frase_inicial,frase_final,frase_erro):
    #     self.caixa_de_mensagem = self.driver.find_element_by_class_name('_2S1VP')
    #     self.caixa_de_mensagem.send_keys(frase_inicial)
    #     time.sleep(1)
    #     self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
    #     self.botao_enviar.click()
    #     self.x = True
    #     while self.x == True:
    #         texto = self.escuta()

    #         if texto != ultimo_texto and re.match(r'^::', texto):
    #             if texto.find('?') != -1:
    #                 ultimo_texto = texto
    #                 texto = texto.replace('::', '')
    #                 texto = texto.lower()
    #                 texto = texto.replace('?', '?*')
    #                 texto = texto.split('*')
    #                 novo = []
    #                 for elemento in texto:
    #                     elemento = elemento.strip()
    #                     novo.append(elemento)

    #                 self.bot.train(novo)
    #                 self.caixa_de_mensagem.send_keys(frase_final)
    #                 time.sleep(1)
    #                 self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
    #                 self.botao_enviar.click()
    #                 self.x = False
    #                 return ultimo_texto
    #             else:
    #                 self.caixa_de_mensagem.send_keys(frase_erro)
    #                 time.sleep(1)
    #                 self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
    #                 self.botao_enviar.click()
    #                 self.x = False
    #                 return ultimo_texto
    #         else:
    #             ultimo_texto = texto


    # def responde_ia(self,texto):
    #     response = self.bot.get_response(texto)
    #     # if float(response.confidence) > 0.5:
    #     response = str(response)
    #     response = 'bot: ' + response
    #     self.caixa_de_mensagem = self.driver.find_elements_by_class_name('_3FRCZ')[1]
    #     self.caixa_de_mensagem.send_keys(response)
    #     time.sleep(1)
    #     self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
    #     self.botao_enviar.click()
    
    


    