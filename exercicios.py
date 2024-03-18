##------VERIFICA IMPAR OU PAR-------

# numero = int(input('Digite um numero inteiro'))

# if numero % 2 == 0:
#     print('Par')
# else:
#     print('Impar')

##----CATEGORIZA IDADE--------

# idade = int(input('Digite Sua idade: '))

# if idade >= 0 and idade <= 12:
#     print('Criança')
# elif idade >= 13 and idade <= 18:
#     print('Adolescente')
# else:
#     print('Adulto')

##-------VERIFICIA CRENCIAIS--------
# userEsperado = 'bruno.gonzalez'
# senhaesperada = 'btorres@1'

# user = input('Digite seu usuario: ')
# senha = input('Digite sua senha: ')

# if user == userEsperado and senha == senhaesperada:
#     print('Login Efetuado com sucesso')
# else: 
#     print('Credenciais incorretas!!')

##----Localiza ponto plano cartesiano-----
# x = float(input('Digite a coordenada X: '))
# y = float(input('Digite a coordenada Y: '))

# if x > 0 and y > 0:
#     print('primeiro')
# elif x < 0 and y > 0:
#     print('segundo')
# elif x < 0 and y < 0:
#     print('terceiro')
# elif x > 0 and y < 0:
#     print('quarto')
# else: 
#     print('eixo de origem')

##------Listas---------

um_a_dez = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['bruno', 'gabriela', 'bianca', 'adrian']
datas = ['08/01/2003', '16/03/2024']

#------imprime só os impares------
for numero in um_a_dez:
    if numero % 2 != 0:
        numeros_somados = ''
        print(numero)


