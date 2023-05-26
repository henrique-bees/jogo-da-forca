# jogo da forca
import random
palavras = ['bicicleta', 'guitarra', 'skate', 'laranja', 'python', 'chapeu',
            'australopitecus', 'mamifero', 'henrique', 'orangutango', 'uva',
            'codigo', 'acento', 'empresa']
letras_input = []
palavra = random.choice(palavras)
tentativas = 6
resultado = False
while True:
    for letra in palavra:
        if letra.lower() in letras_input:
            print(letra, end=(' '))
        else:
            print('_', end=(' '))
    print()
    letras_adicionais = input('digite a letra: ')
    letras_input.append(letras_adicionais.lower())
    if letras_adicionais.lower() not in palavra.lower():
        tentativas -= 1
    print()
    print(f'você ainda tem {tentativas} oportunidades para errar!')
    resultado = True
    for letra in palavra:
        if letra.lower() not in letras_input:
            resultado = False
    if tentativas == 0 or resultado:
        break
if resultado:
    print(f'Parabens, voce descobriu a palavra {palavra}')
else:
    print(f'Que pena, você perdeu, a palavra era {palavra}')
