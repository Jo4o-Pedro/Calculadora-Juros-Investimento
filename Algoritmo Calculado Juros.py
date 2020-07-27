print("*******************************************************************************************************")
tempo = int(input("Quantos anos pretende investir?  "))
juros = float(input("Quantos '%' de imposto?  "))
aporte = int(input("Aportando quanto?  "))
patrimonio = int(input("Vai começar com quanto?  "))
juros = 1 + juros
while tempo > 0:
    patrimonio += aporte
    patrimonio = patrimonio * juros 
    tempo -= 1

print("Seu patrimonio após investir ", aporte, " por ", tempo, " a ", juros, " mensais/anuais é:", patrimonio)
print("*******************************************************************************************************")
