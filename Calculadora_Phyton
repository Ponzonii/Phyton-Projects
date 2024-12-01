def calculadora():
    print("Bem-vindo à Calculadora em Python!")

    # interface inicial
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        # Escolher a operação
        escolha = input("Digite o número da operação desejada (1/2/3/4): ")

        # Verificar se a entrada é válida
        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira valores numéricos válidos.")
                continue

            if escolha == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif escolha == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Escolha inválida. Tente novamente.")

        # Perguntar se o usuário deseja continuar
        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por usar a calculadora. Até mais!")
            break

# Chamar a função calculadora
calculadora()
