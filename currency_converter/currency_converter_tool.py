def set_tool(dolar_value, option):
	while True:
		try:
			amount = float(input("\nIngrese monto a convertir: "))
			break
		except:
			input("\nEl monto debe estar expresado en números.")

	if option == 1:
		print(f"\nMonto: ${amount:.2f} | Conversión: {amount * dolar_value :.2f}")
	elif option == 2:
		print(f"\nMonto: {amount:.2f} | Conversión: ${amount / dolar_value :.2f}")

	input("\nPresione para continuar.")