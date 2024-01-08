# Um programa basico que compara a idade para conduzir
idade = 20
possui_carteira = True

if (idade > 18) and possui_carteira:
    print("Voce pode dirigir.")
elif possui_carteira:
    print("Voce apenas possui a carteira. Espere a idade.")
else:
    print("Voce não pode dirigir.")