def setTool(dolarValue):
	print("\n* Calcular porcentajes *")
	while True:
		try:
			startAmount = float(input("\nIngrese monto: "))
			break
		except:
			input("\nDebe ingresar un valor númerico.")

	while True:
		try:
			ivaPercentage = float(input("\nIngrese porcentaje de IVA: "))
			break
		except:
			input("\nDebe ingresar un valor númerico.")

	while True:
		try:
			earningPercentage = float(input("\nIngrese porcentaje de ganancia: "))
			break
		except:
			input("\nDebe ingresar un valor númerico.")

	amountMoreIVA = ((ivaPercentage / 100) * startAmount) + startAmount
	earningAmount = ((earningPercentage / 100) * amountMoreIVA) + amountMoreIVA

	print("\n* Resultado de la suma de los porcentajes *")
	print(f"\n| Monto inicial: {startAmount:.2f} | Monto con IVA: {amountMoreIVA:.2f} | Monto con ganancia: {earningAmount:.2f} |");
	print("\n* Resultado expresado en dolares *");
	print(f"\n| Monto inicial: ${startAmount / dolarValue :.2f} | Monto con IVA: ${amountMoreIVA / dolarValue :.2f} | Monto con ganancia: ${earningAmount / dolarValue :.2f} |");
	input("\nPresione para continuar.");