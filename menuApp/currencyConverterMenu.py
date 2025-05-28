def getMenu():
	while True:
		print("\n* Conversor de moneda *")
		print("\n1. Convertir de dolares a su moneda.")
		print("2. Convertir de su moneda a dolares.")
		print("3. Volver al menú principal.")

		while True:
			try:
				option = int(input("\nIngrese su opción: "))
				break
			except:
				input("\nDebe ingresar un número.")

		if option >= 1 and option <= 3:
			break
		else:
			input("\nOpción incorrecta")

	return option