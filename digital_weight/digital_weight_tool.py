def set_tool():
	print("\n* Peso digital *")

	while True:
		try:
			price_kg = float(input("\nIngrese el precio (Kg): "))
			break
		except:
			input("\nIngrese un valor numérico.")

	price_g = price_kg / 1000;

	while True:
		print("\n* Información del producto *")
		print(f"\n| Precio (Kg): {price_kg:.2f} | Precio (g): {price_g:.2f} |")

		while True:
			try:
				product_grames = int(input("\nIngrese peso en gramos (g): "))
				break
			except:
				input("\nIngrese peso en números.")

		final_price = product_grames * price_g

		print(f"\n| Peso (g): {product_grames}g | Precio: {final_price:.2f}")

		flag_not_exit = True

		while flag_not_exit:
			option_weight = input("\nPesar otra vez. (Y / n): ")

			if option_weight == "y":
				print("\nVolver a pesar.")
				break
			elif option_weight == "n":
				print("\nNo volver a pesar.")
				flag_not_exit = False	
			else:
				print("\nIngrese una respuesta válida.")

		if flag_not_exit == False:
			break