def get_menu(dolar_value):
	while True:
		print("\n** MENU PRINCIPAL **")
		print(f"\nValor del dolar ($1): {dolar_value:.2f}")
		print("\n1. Conversor de moneda.")
		print("2. Calcular ganancia.")
		print("3. Peso digital.")
		print("4. Cambiar valor del dolar.")
		print("5. Salir.")

		while True:
			try:
				option = int(input("\nIngrese su opción: "))
				break
			except:
				input("\nDebe ingresar un número.\n")

		if option >= 1 and option <= 5:
			break
		else:
			input("\nOpción incorrecta.\n")

	return option