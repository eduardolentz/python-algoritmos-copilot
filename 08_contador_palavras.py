# Conta quantas palavras há em um texto fornecido pelo usuário
def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

entrada = input("Digite um texto: ")
quantidade = contar_palavras(entrada)
print("Número de palavras:", quantidade)
