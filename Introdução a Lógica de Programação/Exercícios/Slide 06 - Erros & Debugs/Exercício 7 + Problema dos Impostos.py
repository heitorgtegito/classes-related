# salario_bruto = float(input("Digite o salário bruto: "))

# inss = salario_bruto * 0.11
# if salario_bruto <= 2000:
#   ir = 0
# elif salario_bruto <= 5000:
#   ir = salario_bruto * 0.15
# else:
#   ir = salario_bruto * 0.275

# salario_liquido = salario_bruto - inss - ir
# print(f"Salário líquido: R$ {salario_liquido:.2f}")


salario_bruto = float(input("Digite o salário bruto: "))

inss = salario_bruto * 0.11
salario_inss = salario_bruto - inss

if salario_bruto <= 2000:
  ir = 0
elif salario_bruto <= 5000:
  ir = salario_inss * 0.15
else:
  ir = salario_inss * 0.275

salario_liquido = salario_inss - ir
print(f"Salário líquido: R$ {salario_liquido:.2f}")
