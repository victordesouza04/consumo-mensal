aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts: "))
tempo = float(input("Digite o tempo de uso diário em horas: "))
consumomensal = (potencia * tempo * 30) / 1000
gastomensal = consumomensal * 0.75
print(f"Aparelho: {aparelho}")
print(f"Consumo mensal: {consumomensal:.2f} kWh")
print(f"Gasto mensal estimado: R$ {gastomensal:.2f}")