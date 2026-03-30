nome = str("Nome do aluno: ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
nota4 = float(input("Digite a nota da quarta prova: "))

media = nota1 + nota2 + nota3 + nota4

if media <= 40 and media >= 28:
    print(f"O aluno está aprovado") 

elif media <= 27  and media >= 20:
    print(f"O aluno esta em recuperação!")

else:
    print(f"O aluno esta reprovado")
               