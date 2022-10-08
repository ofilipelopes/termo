from random import choice


def usert(lst):  # Tentativas do usuario
    ver = False
    while not ver:
        ver = True
        usertry = input('Sua tentativa: ').strip()
        if len(usertry) != 5:
            print('São aceitas apenas palavras com 5 letras!')
            ver = False
            continue
        if usertry + '\n' not in lst:   # Se a palavra não tá na lista
            # (o + '\n' é porque a lista é um txt que tem quebra de linha)
            print('Palavra não reconhecida')
            ver = False
    return usertry


def verify(word, userword):   # Verifica se acertou e se acabou as chances
    # se os dois forem negativos, continua o jogo, senão acaba
    global chance
    if word == userword:
        print('DENTRO! Você acertou!')
        return False
    elif chance == 6:
        print('Acabou suas chances')
        return False
    else:
        return True


def colorprint(word, userword):
    for i, u in enumerate(userword):
        if u in word:
            if userword[i] == word[i]:
                print('\033[32m', end='')
            else:
                print('\033[33m', end='')
        print(u + '\033[m', end='')


def dics(word, dic):  # Cria um dicionario com as letras da palavra como keys e a quantidade como valor
    for l in word:
        if l in dic.keys():
            dic[l] += 1
        else:
            dic[l] = 1


lista = open('palav5.txt', 'rt')                        # Abro o arquivo de texto com as palavras
palavra = choice(lista.readlines()).strip().lower()     # Sorteia uma palavra
lista.close()                                           # fecha o arquivo
print(palavra)
worddict = dict()                                       # dicionario com a palavra sorteada
dics(palavra, worddict)
chance = 1

while True:
    lista = open('palav5.txt', 'rt')  # Reabre o arquivo para pegar a lista de palavra e usar para verificação do input
    lista1 = lista.readlines()
    lista.close()
    user = usert(lista1)
    userdict = dict()                 # dicionario com a palavra que o usuario digitou
    dics(user, userdict)
    colorprint(palavra, user)
    print()
    verif = verify(palavra, user)
    if not verif:
        break
    chance += 1
