def imprimir_nomes():
    nomes = ["joão", "maria", "fulano", "ciclano"]
    print("1 -", nomes[0])
    print("2 -", nomes[1])
    print("3 -", nomes[2])
    print("4 -", nomes[3])

imprimir_nomes()    



def imprimir_primeiro_ultimo_nome ():
    nome = ["João", "Maria", "fulano", "ciclano"]
    print("1 -", nome[0])
    print("4 -", nome[3])

imprimir_primeiro_ultimo_nome()


def imprimir_segundo_terceiro_nome ():
    nome = ["João", "Maria", "fulano", "ciclano"]
    print("2 -", nome[1])
    print("3 -", nome[2])

imprimir_segundo_terceiro_nome()



def substituir_alimentos():
    alimentos = ["macarrão", "pepino", "batata"]

    alimentos[0] = input("digite o primeiro alimento: ")
    alimentos[1] = input("digite o segundo alimento: ")
    alimentos[2] = input("digite o terceiro alimento: ")
    
    print("1 -", alimentos[0])
    print("2 -", alimentos[1])
    print("3 -", alimentos[2])
substituir_alimentos()