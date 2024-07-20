import math

# Calcular a área do círculo

raio = float(input("Informe o raio do círculo: "))
area = math.pi * raio ** 2
print(f"{area:.2f}")


# Divisão de inteiros
try:
    v1 = int(input("Informe o valor 1: "))
    v2 = int(input("Informe o valor 2: "))
    resultado = v1 // v2
    print(resultado)
except Exception as e:
    print(e)


#Separa o dia, mês e ano de uma data no formato dd/mm/yyyy e imprime
try:
    data = input("Informe uma data (dd/mm/aaaa): ")
    data_separada = data.split("/")
    print("Data separada")
    for dado in data_separada:
        print(dado)
except Exception as e:
    print(e)
