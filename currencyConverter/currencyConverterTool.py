def setTool(dolarValue,option):
	while True:
		try:
			monto = float(input("\nIngrese monto a convertir: "))
			break
		except:
			input("\nEl monto debe estar expresado en números.")

	if option == 1:
		print(f"\nMonto: ${monto:.2f} | Conversión: {monto * dolarValue :.2f}")
	elif option == 2:
		print(f"\nMonto: {monto:.2f} | Conversión: ${monto / dolarValue :.2f}")

	input("\nPresione para continuar.")