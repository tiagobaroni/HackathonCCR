# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 06:49:35 2020

@author: berna
"""

import sys
sys.path.insert(0, r'C:\Users\berna\Desktop\Hackathon CCR')

import re
from selenium_bot import wppbot


# Inicializa o bot
bot = wppbot('BIMO')
       


while True:
    # Últimas mensagens das conversas
    conversas = bot.acompanhar_conversas()
    
    for auth, msg in conversas.items():
        # Se encontrar algum comando
        if re.match(r'\.\.', msg):
            # Abre a conversa em que o comando ocorreu
            bot.abre_conversa(auth)
            
            # Ajusta o texto do comando
            texto = msg.replace('..', '')
            texto = texto.lower().strip()
            
            # Executa o comando correspondente
            if texto == 'ajuda':
                bot.envia_msg(bot.ajuda())
                
            elif texto == 'banho':
                 bot.envia_msg(bot.banho())
            
            elif texto == 'banheiro':
                 bot.envia_msg(bot.sanitário())
            
            elif texto == 'comida':
                bot.envia_msg(bot.comida())
            
            elif texto == 'sono':
                bot.envia_msg(bot.sono())
            
            elif texto == 'saude':
                bot.envia_msg(bot.saude())
            
            elif texto == 'perigo':
                pass
                
            else:
                # Em caso de grafia errada ou comando inexistente 
                bot.envia_msg(bot.nao_encontrado())
                bot.envia_msg(bot.ajuda())

            