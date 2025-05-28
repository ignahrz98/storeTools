def setTool():
	print("\n* Peso digital *")

	while True:
		try:
			priceKg = float(input("\nIngrese el precio (Kg): "))
			break
		except:
			input("\nIngrese un valor numérico.")

	priceG = priceKg / 1000;

	while True:
		print("\n* Información del producto *")
		print(f"\n| Precio (Kg): {priceKg:.2f} | Precio (g): {priceG:.2f} |")

		while True:
			try:
				productGrames = int(input("\nIngrese peso en gramos (g): "))
				break
			except:
				input("\nIngrese peso en números.")

		finalPrice = productGrames * priceG

		print(f"\n| Peso (g): {productGrames}g | Precio: {finalPrice:.2f}")

		flagNotExit = True

		while flagNotExit:
			optionWeight = input("\nPesar otra vez. (Y / n): ")

			if optionWeight == "y":
				print("\nVolver a pesar.")
				break
			elif optionWeight == "n":
				print("\nNo volver a pesar.")
				flagNotExit = False	
			else:
				print("\nIngrese una respuesta válida.")

		if flagNotExit == False:
			break