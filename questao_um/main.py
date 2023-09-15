def fibonacci(n):
    penultimate_number = 0
    last_number = 1
    result = [penultimate_number, last_number]
    for number in range(2, n + 1):
        penultimate_number, last_number = last_number, penultimate_number + last_number
        result.append(last_number)
    return result, result[-1]


valid = False
while not valid:
    try:
        n = int(
            input(
                "Digite um número inteiro, que deseja ver na sequência de Fibonacci: "
            )
        )
        valid = True
        result, final_result = fibonacci(n)
        print(f"O {n}-ésimo termo da sequência de Fibonacci é {final_result}")
        print(f"Sequência são: {result}")
    except ValueError:
        print("Você digitou um número que não é inteiro!")
