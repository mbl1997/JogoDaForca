from random import choice

with open ('palavras.txt') as arquivo:
  linhas = arquivo.read()
lista_de_palavras = linhas.split('\n')
     
palavra = choice(lista_de_palavras).upper()

forca = """
_____
    |
    |
    |
    -"""

vazio = """


"""

cabeca = """
      o
"""

troco = """
       o
       |
"""

braco_esquedo = """
           o
          /|
"""

braco_direto = """
           o
          /|\\
"""

perna_esqueda = """
           o
          /|\\
          /
"""


perna_direita = """
           o
          /|\\
          / \\
"""

chances_do_boneco = [vazio,cabeca,troco,braco_esquedo,braco_direto,perna_esqueda,perna_direita]

acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''

while acertos != len(palavra) and erros != 7:
    mensagem = ''
    for letra in palavra:
      if letra in letras_acertadas:
       mensagem += f'{letra}'
    else:
      mensagem += '_ '
    print(forca + chances_do_boneco[erros])
    print(mensagem)

    
    letra = input('Digite a letra:').upper()
    if letra in letras_acertadas+letras_erradas:
            print('Você já tentou essa letra')
            continue 
    if letra in palavra:
        print('Você acertou a letra')
        letras_acertadas += letra
        acertos += palavra.count(letra)
    else:
        print('Você errou a letra..!')
        letras_erradas += letra
        erros += 1

        