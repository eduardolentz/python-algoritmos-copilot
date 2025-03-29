# Calcula o fatorial de um número inteiro usando recursão
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("Fatorial não definido para números negativos.")
else:
    print(f"Fatorial de {numero} é {fatorial(numero)}")
