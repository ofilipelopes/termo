from random import choice


def usert(lst):  # Tentativas do usuario.
    ver = False
    while not ver:
        ver = True
        usertry = input('Sua tentativa: ').strip()
        if len(usertry) != 5:
            print('São aceitas apenas palavras com 5 letras!')
            ver = False
            continue
        if usertry + '\n' not in lst:   # Se a palavra não tá na lista...
            # (o + '\n' é por a lista ser um txt que tem quebra de linha).
            print('Palavra não reconhecida')
            ver = False
    return usertry  # Aqui indica possível erro em algumas IDEs, por teoricamente a variavel pode não ser criada...
    # se não entrar no laço. Mas no caso ela sempre vai ser, pois, sempre o entra no laço.


def verify(word, userword):   # Verifica se acertou e se acabou as chances...
    # se os dois forem negativos, continua o jogo, senão acaba.
    global chance
    if word == userword:
        print('DENTRO! Você acertou!')
        return False
    elif chance == 6:
        print('Acabou suas chances!')
        print('A palavra era:', palavra)
        return False
    else:
        return True


def colorprint(word, userword):
    cprint = ['', '', '', '', '']   # Cria uma lista para preencher com as letras coloridas.
    for i, u in enumerate(userword):
        if u in word:
            if userword[i] == word[i]:  # Se a letra tá no lugar certo, adiciona na lista na cor verde.
                if cprint[i] == '':
                    cprint[i] = ('\033[32m' + u + '\033[m')
                    worddict[u] -= 1
    for i, u in enumerate(userword):    # Tem que repetir o laço, um else no de cima não resolve...
        # pois, se a letra repetir na palavra que o usuario tentou e a primeira tá no lugar errado e a segunda no...
        # certo, a vai printar uma amarela e uma verde, mas isso só pode acontecer se a letra se repetir na palavra...
        # sorteada também.
        if u in word:
            if worddict[u] > 0:  # Se tem na palavra, mas tá no lugar errado, adiciona na cor amarela.
                if cprint[i] == '':
                    cprint[i] = ('\033[33m' + u + '\033[m')
                    worddict[u] -= 1
            else:
                if cprint[i] == '':  # Caso a letra já tá na palavra, mas já foi adicionada na lista ela entra sem cor
                    cprint[i] = u
        else:
            cprint[i] = u   # Esse é para caso não esteja na palavra, também entra sem cor
    for c in cprint:
        print(c, end='')


def dics(word, dic):  # Cria um dicionário com as letras da palavra como keys e a quantidade como valor.
    for l in word:
        if l in dic.keys():
            dic[l] += 1
        else:
            dic[l] = 1


lista = open('palav5.txt', 'rt')                        # Abro o arquivo de texto com as palavras.
palavra = choice(lista.readlines()).strip().lower()     # Sorteia uma palavra.
lista.close()                                           # fecha o arquivo.
chance = 1

while True:
    lista = open('palav5.txt', 'rt')  # Reabre o arquivo para pegar a lista de palavra e usar para verificação do input.
    lista1 = lista.readlines()
    lista.close()
    worddict = dict()  # dicionario com a palavra sorteada.
    dics(palavra, worddict)
    user = usert(lista1)
    colorprint(palavra, user)
    print()
    verif = verify(palavra, user)
    if not verif:
        break
    chance += 1
