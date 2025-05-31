import json

def setTool(dolar_value):
	print("\n* Cambiar valor del dólar *")
	print(f"\n| Valor actual | $1.00 | {dolar_value:.2f} |")

	while True:
		try:
			new_dolar_value = float(input("\nIngrese nuevo valor para dólar: "))
			break
		except:
			input("\nIngrese un valor númerico.")

	print(f"\nEl valor del dólar será actualizado de {dolar_value:.2f} al nuevo valor {new_dolar_value:.2f}")
	input("\nPresione para continuar.")

	# Save dolar_value to the file.
	datos = {
		"dolar_value": new_dolar_value
	}

	with open("data/dolar_value.json", "w") as file_dolar_value:
		json.dump(datos, file_dolar_value, indent=4)
		print("\nEl nuevo valor del dólar fue actualizado en el archivo.")

	return new_dolar_value