pdl = int(input("Digite o seu PdL para saber qual é o seu rank:  "))

if pdl <= 999:

    print("O seu rank é Ferro!")

elif 1000 < pdl <= 1999:

    print("O seu rank é Bronze!")

elif 2000 < pdl <= 2999:

    print("O seu rank é Prata!")

elif 3000 < pdl <= 3999:

    print("O seu rank é Ouro!")

elif 4000 < pdl <= 4999:

    print("O seu rank é Platina!")

elif 5000 < pdl <= 5999:

    print("O seu rank é Diamante!")

elif 6000 < pdl <= 6999:

    print("O seu rank é Mestre!")

elif 7000 < pdl <= 7999:

    print("O seu rank é Grão-Mestre!")

elif pdl > 8000:

    print("O seu rank é Desafiante!")