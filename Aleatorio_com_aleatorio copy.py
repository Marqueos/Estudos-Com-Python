import gmpy2
import secrets

def realizar_testes(dates, qtd_repeticao):
    dados = list(range(dates))
    soma_contadores = 0

    for _ in range(qtd_repeticao):
        data = dados.copy()  # Evitar a modificação da lista original
        contador = 0

        while True:
            numero1 = gmpy2.mpz(secrets.choice(data))
            numero2 = gmpy2.mpz(secrets.choice(data))
            contador += 1

            print(f"Tentativa {contador}: {numero1} - {numero2}")

            if numero1 == numero2:
                print(f"Números iguais! Levou {contador} tentativas.")
                soma_contadores += contador
                break

    return soma_contadores / qtd_repeticao

# Solicitar dados de entrada
dates = int(input("Digite um número inteiro: "))
qtd_repeticao = int(input("Qual a quantidade de vezes que deseja repetir essa estrutura de código?"))

# Chamar a função
media_contadores = realizar_testes(dates, qtd_repeticao)

print(f"Média dos contadores: {media_contadores}")
