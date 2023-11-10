import random 



while True:
    dados= ['0','1','2','3','4','5','6','7','8','9','10']
    computer= random.choice(dados)
    usuario= input("Escolha seu número de 0 a 10: ")
    if usuario==computer:
        print("Parabens você acertou") 
    else:
        print("Erroou, tente de novo")
        print(f"O número correto era: ", computer)
    
    tentar=input("Deseja tentar de novo? (s/n): ")
    
    if tentar.lower()!= 's':
        break