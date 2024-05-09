#desafio, sistema de senhas

#1- o computador cria uma senha aleatoria
#2- vc digita a senha
#3 verificar se o usuarui pode acessar o sistema

import random 

senha_aleatoria = random.randint(12345,678910)
minha_senha = input('digite aqui sua senha')

if minha_senha == senha_aleatoria:
    print('senha correta', senha_aleatoria)
else:
    print('tente novamente', senha_aleatoria) 


    