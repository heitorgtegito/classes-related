# salario_bruto = float(input("Digite o salário bruto: "))

# inss = salario_bruto * 0.11
# salario_pos_inss = salario_bruto - inss

# if salario_bruto <= 2000:
#   ir = 0
# elif salario_bruto <= 5000:
#   ir = salario_pos_inss * 0.10
# else:
#   ir = salario_pos_inss * 0.20

# salario_liquido = salario_pos_inss - ir
# print(f"Salário líquido: R$ {salario_liquido:.2f}")

salario_bruto = float(input("Digite o salário bruto: "))

inss = salario_bruto * 0.11
salario_pos_inss = salario_bruto - inss

if salario_bruto <= 2000:
  ir = 0
elif salario_bruto <= 5000:
  ir = salario_pos_inss * 0.15
else:
  ir = salario_pos_inss * 0.275

salario_liquido = salario_pos_inss - ir
print(f"Salário líquido: R$ {salario_liquido:.2f}")
