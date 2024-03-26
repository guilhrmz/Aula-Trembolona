print("---------------------")
print("      SCRABBLE       ")
print("---------------------")

def scrabble_score(palavra):
    tabela_letras = {
        'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10
    }

    score = 0
    for letra in palavra.lower():
        if letra in tabela_letras:
            score += tabela_letras[letra]
    
    return score

def main():
    palavra = input("Digite a palavra para calcular o Scrabble Score: ")
    score = scrabble_score(palavra)
    print(f"O Scrabble Score da palavra '{palavra}' é: {score}")

    
main()