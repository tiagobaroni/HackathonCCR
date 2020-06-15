# Hackathon CCR

O presente diretório/projeto foi criado como entrega para o Hackathon CCR, ocorrido entre 12 e 14 de junho de 2020, servindo como entrega dos códigos fontes desenvolvidos no decorrer do *hackathon*. 

A postagem do *commit* final, que deve ocorrer antes das 23h59 do dia 14 de junho não significa que o projeto está permanentemente finalizado e/ou que não haverá continuidade. Imediatamente após a entrega os trabalhos continuarão no intuito de que haja um aplicativo viável e adequado para ser levado a público em breve.

Esperamos fazer isso com a chancela de *ganhador* ou *um dos ganhadores* deste *hackathon*, mas isso não é limitante para continuarmos nosso trabalho. 

Esse README.md está dividido nos seguintes tópicos:

 * [Time](#time)
 * [Projeto](#projeto)
 * [Persona](#persona)
 * [BIMO](#bimo)
 * [Chatbot](#chatbot)
 * [To-Do](#to-do)



Essas seções apresentam a visão geral de cada um desses itens, demonstrando o que foi produzido durante o *hackathon* e aquilo que está na rota de produção para o aplicativo. 


<div id="time"></div>

## Time

O time 131, envolvido na criação desse projeto contou com:

* [Priscila Hoehr Mostardeiro](https://www.linkedin.com/in/priscila-hoehr/);
* [Thiago Caetano Ferraz Costa](https://www.linkedin.com/in/thiagocaetanogeo/), e;
* [Tiago Henrique França Baroni](https://www.linkedin.com/in/tiago-baroni/). 

## Projeto

O projeto caracteriza-se como uma ferramenta de geração de valor através da comunicação, em quatro pilares principais:

* Ferramenta de ATIS (*Advanced Traveller Information System*) embarcada, permitindo que a concessionária, através de notificações *push* possa manter o caminhoneiro informado;
* Assistente pessoal de deslocamento;
* Facilitador de comunicação com a CCR;
* Ferramenta de segurança/anti-pânico.

Essas características podem ser melhor observadas no *pitch* e na apresentação encaminhadas como parte do envio final do *Hackathon CCR*.

<div id="persona"></div>

## Persona

Para compor a solução e compreender em quais dimensões o aplicativo seria útil, foram analisadas horas de entrevistas disponíveis na internet e em revistas especializadas, das quais coletamos dois "perfis médios" para compor as personas de interesse do projeto. 

### PERSONA I

**Nome:** Sebastião, conhecido no trecho como “Seba”.

**Idade:** 38 anos.

Casado, teve 4 filhos, porém uma faleceu.

Trabalha como caminhoneiro desde os 20 anos de idade, mas desde peque trabalho carregando caminhão, até que em algum momento um amigo com experiência o transformou em aprendiz. 

Seba já viajou o país inteiro e afirma que apesar da saudade constante da família, a solidão e o medo inerente à vida nas estradas, a paixão pela profissão acaba sendo mais forte. Estar na estrada não só é seu sustento, como é seu combustível de vida. 

Ele também diz que descobriu o melhor pastel do país em um pequeno casebre em uma rodovia do interior de São Paulo.

Tentando melhorar sua renda, Seba financiou um caminhão há alguns anos, porém tem visto suas condições de trabalho se tornarem cada vez piores, seus custos cada vez maiores e as parcelas do seu bruto vencendo e sendo pagas com dificuldade.

Mesmo com todas as dificuldades, Seba sabe que sempre pode contar com companheiros de estrada, e que sempre terá um amigo para conversar onde quer que ele vá.


### PERSONA II

**Nome:** Thaís, conhecida pelo codinome “Super Bela”.

**Idade:** 28 anos.

Casada, tem duas filhas pequenas.

Bela trabalha a 5 anos pilotando uma carreta lotada de soja, mas cresceu na boleia do caminhão do pai. Com seus singelos 1,47m de altura, ela já cansou de ouvir piadas relacionadas a sua altura e ao seu caminhão, porém no volante, deixa claro para qualquer um que tente fazer piada o tanto que é capaz. 

Em sua boleia, bela tem um espaço para levar as filhas quando pode. Partir sem elas é sempre a parte mais dolorida. Quando está na estrada, Bela nunca tem hora para dormir, pois tenta usufruir ao máximo do tempo para voltar o mais rápido para as filhas.

Bela possui um coração enorme e sabe da importância de compartilhar. Sempre que está no trecho, carrega alimentos e brinquedos para distribuir àquelas famílias carentes nos trechos por onde passa. Ela sonha em conquistar cada vez mais para que possa ajudar cada vez mais.

No trecho Bela sente medo constantemente, principalmente na hora de dormir. Ela sabe que todos os sacrifícios são pelo bem de sua família. Ela sonha em um dia poder comprar seu próprio caminhão.

Pontos em comum:
* Eles sacrificam o próprio conforto pelo bem da família;
* Ambos dizem que não gostariam de ter outra profissão, mesmo já tendo pensado em desistir;
* Eles se sentem muito solitários;
* Eles estão sempre lutando contra o relógio;
* Eles acreditam que perdem muito tempo esperando (burocracias, carregamentos etc.);
* Ambos preferem fazer suas paradas em locais seguros e movimentados, para segurança própria e da carga;
* Conhecem muito bem os detalhes dos trechos que fazem com frequência.

## BIMO

(...)


<div id="chatbot"></div>

## Chatbot

O Chatbot tem o objetivo de interagir com o caminhoneiro. Como grande parte desse público se comunica via *WhatsApp*, o bot foi desenvolvido mirando a interação com essa rede social. 

Inicialmente foi escolhida uma implementação em *python* com o uso do *Selenium*. O Chatbot responde apenas aos comandos previamente configurados, sem avaliação quanto a possíveis erros de digitação. Os dados de distância estão sendo gerados de forma randomizada, uma vez que ainda não se tem a posição real do interlocutor.

Após a liberação ao público o *APP* seguirá evoluindo. A as novas funcionalidades a serem implementadas são, em ordem:

1. Integração com o PX, informando ao usuário a posição dos amigos nas redondezas;
2. Implementação de função para formar comboios;
3. Implementação de Inteligência Artificial capaz de entender e responder a necessidades mais complexas;

<div id="to-do"></div>

## To-Do

Neste item, temos as alterações planejadas para o projeto BIMO:

### Aplicativo

1. Aquisição da API Key para uso do Google Maps para integração de localização de POIs;
2. Implementação do cadastro utilizando a API do Facebook e Google (aguardando liberação da API Key);
3. Finalização da implementação do background, onde o aplicativo deve rodar para coletar as informações de localização do condutor, permitindo atitude de *butler*: informar a entrada da via de maneira ativa, sem ação do caminhoneiro;
4. Verificação com a CCR a melhor maneira para recepção dos chamados de socorro e de pânico (*infelizmente não conseguimos mentoria com nenhum funcionário da CCR para coletar essa informação*);
5. Implementação do *buffer* usando SQLite para redução do tráfego de dados e otimização do consumo de bateria (*já está ocorrendo - em fase de testes*);
6. Melhoria da integração com o *chatbot* quando este for passado para API do WhatsApp;
7. Implementação dos comandos de voz. 

### Chatbot
1. Integração com a posição atual do usuário;
2. Implementação da funcionalidade *perigo*, fazendo a conexão diretamente com a polícia;
3. Migração para uma *Application for Programming Interface - API*;
3. Integração com o Banco de Dados de localidades (sanitários, chuveiros, restaurantes, etc);
6. Implementação de código capaz de entender o comando mesmo com pequenos erros de digitação;
7. Integração com comandos por voz.
