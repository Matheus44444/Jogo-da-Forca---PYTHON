import unicodedata
import re

def formatar_texto(texto):
    texto = texto.strip()

    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')

    texto = re.sub(r'\d+', '', texto)

    texto = texto.lower()

    return texto

palavra = input("Digite a palavra secreta: ")
palavra = formatar_texto(palavra)

# Limpa a tela simulando várias linhas
print("\n" * 50)

letras_descobertas = ["_" for _ in palavra]
letras_usadas = []
vidas = 6

print("=== JOGO DA FORCA ===")

while vidas > 0 and "_" in letras_descobertas:

    print("\nPalavra:", " ".join(letras_descobertas))
    print("Vidas restantes:", vidas)
    print("Letras usadas:", ", ".join(letras_usadas))

    tentativa = input("Digite uma letra: ")
    tentativa = formatar_texto(tentativa)

    if tentativa == "":
        print("Digite uma letra válida.")
        continue

    tentativa = tentativa[0]

    if tentativa in letras_usadas:
        print("Você já tentou essa letra.")
        continue

    letras_usadas.append(tentativa)

    if tentativa in palavra:
        print("Acertou!")
        for i in range(len(palavra)):
            if palavra[i] == tentativa:
                letras_descobertas[i] = tentativa
    else:
        print("Errou!")
        vidas -= 1

if "_" not in letras_descobertas:
    print("\nParabéns! Você ganhou!")
    print("A palavra era:", palavra)
else:
    print("\nVocê perdeu!")
    print("A palavra correta era:", palavra)
