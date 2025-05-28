def setTool(dolarValue):
	print("\n* Cambiar valor del dólar *")
	print(f"\n| Valor actual | $1.00 | {dolarValue:.2f} |")

	while True:
		try:
			newDolarvalue = float(input("\nIngrese nuevo valor para dólar: "))
			break
		except:
			input("\nIngrese un valor númerico.")

	print(f"\nEl valor del dólar será actualizado de {dolarValue:.2f} al nuevo valor {newDolarvalue:.2f}")
	input("\nPresione para continuar.")

	return newDolarvalue