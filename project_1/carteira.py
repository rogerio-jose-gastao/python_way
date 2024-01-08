# Um programa basico que compara a idade para conduzir

def idade_conducao(nome, possui_carteira, idade = 20):
    if (idade > 18) and possui_carteira:
        print("{nome} pode dirigir.")
    elif possui_carteira:
        print("{nome} apenas possui a carteira. Espere a idade.")
    else:
        print("{nome} não pode dirigir.")

idade_conducao("Aurora", idade=18)
idade_conducao("Nando", idade=10)
idade_conducao("Rin", False)