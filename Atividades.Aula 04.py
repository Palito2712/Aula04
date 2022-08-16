nota1 = float(input("Para saber se você passou por média, digite a sua primeira nota: "))

nota2 = float(input("Agora, digite a sua segunda nota: "))

nota3 = float(input("Digite a sua terceira nota: "))

nota4 = float(input("Por final, digite a sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:

    print("Parabéns, você passou por média!!")

else:

    print("Que pena, você ficou de recuperação!")