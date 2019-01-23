# Interpolação de dados de precipitação de chuva em Pernambuco

Repositório contendo os scripts utilizados para o estudo da interpolação de dados de precipitação de chuva nas 7 estações no estado de Pernmabuco contidas no dados abertos do INMET, para a disciplina Linguagens de Programação do curso de Bacharelado em Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE) no período de 2018.2.


## Pré-requisitos

- Linguagem
    - Python v3.x

## Guia de instalação

Para executar os comandos abaixo é necessário que você possua instalado em seu computador a linguagem de programação Python v3.x para acima. Você pode fazer o download do Python [aqui](https://www.python.org/downloads/). Também é necessário que o Python seja uma variável do ambiente no seu sistema. Caso seu sistema operacional seja Windows, [aqui](https://python.org.br/instalacao-windows/) segue um exemplo de como transformar o Python em uma variável do ambiente. Veja [aqui](http://pythonclub.com.br/instalacao-python-django-windows.html) também outro tutorial.

### PIP

O pip é gerenciador de pacotes do Python. Ele tem como finalidade facilitar o seu desenvolvimento. Para download do pip, basta baixar este arquivo [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Caso o downloado não seja feito de imediato ao clicar no link, você pode baixar o arquivo abrindo-o pelo link e clicando no botão direito do mouse e escolhendo a opção "salvar como". Você deverá salvar o arquivo no diretório Scripts, que fica no diretório onde o Python está salvo no seu computador.
Feito o download, abra um terminal de linha de comando (tecla windows + r, digite cmd e depois aperte enter) e mova o cursor até o diretório Scripts onde se encontra o arquivo get-pip.py. Após isso execute o comando:

```
python get-pip.py
```

Após o pip instalado com sucesso você deve instalar as dependências:

```
pip install -r requirements.txt 

``` 


## Download do projeto

O projeto pode ser baixado em arquivo zipado através do github do projeto, ou então sendo clonado através do link:

```
https://github.com/Airtonmartins/lp-data-analytics.git
```

## Execução do projeto

Após os pré-requisitos instalados e o projeto baixado/clonado, abra o diretório onde o projeto está localizado e inicie naquele diretório um terminal de linha de comando (tecla windows + R, e digite cmd e aperte OK). Caso não consiga mover a localização do seu terminal para o diretório do projeto, tente digitar o comando:

```
cd /caminho do seu diretório no explorer
```

Após localizar o seu diretório no terminal, você deverá executar o seguinte comando:

```
jupyter notebook
```

Depois de digitado o comando, tecle enter e aguarde o comando ser executado, então será aberta uma janela/guia do seu navegador executando o projeto no localhost:8888. Pronto agora você já pode utlizar o projeto! Para encerrar o jupyter notebook, pasta você ir no terminal de linhas de comando aberto e apertar a tecla Ctrl + C e isso encerrará a execução. Bom, vai o alertar que o jupyter notebook consome bastante do hardware do seu computador, então caso tenha um computador que não seja tão potente, você pode baixar o projeto e utilizar ele em ferramentas/máquinas na nuvem, como por exemplo o [cocalc](https://cocalc.com).


## Contato e dúvidas

Para mais informações ou dúvidas entrar em contato através do e-mail:  
airton.neris@gmail.com