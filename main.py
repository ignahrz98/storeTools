import json
from menuApp import mainMenuApp
from menuApp import currencyConverterMenu
from currencyConverter import currencyConverterTool
from calcularPorcentajes import calcularPorcentajesTool
from digitalWeight import digitalWeightTool
from dolarValue import dolarValueTool

# Get the dolarValue from the file.
try:
	with open("data/dolar_value.json", "r") as file_dolar_value:
		datos = json.load(file_dolar_value)
		dolarValue = datos["dolar_value"]

		print("Valor del dólar cargado desde el archivo.")
except:
	datos = {
		"dolar_value": 0.0
	}

	# Create file for dolar_value
	with open("data/dolar_value.json", "w") as file_dolar_value:
		json.dump(datos, file_dolar_value, indent=4)
		print("El archivo para valor del dólar ha sido creado")

	dolarValue = datos["dolar_value"]

# Show the main menu.
while True:
	option = mainMenuApp.getMenu(dolarValue)

	if option == 1:
		optionCurrencyConverterMenu = currencyConverterMenu.getMenu()

		if optionCurrencyConverterMenu == 1:
			currencyConverterTool.setTool(dolarValue,1)
		elif optionCurrencyConverterMenu == 2:
			currencyConverterTool.setTool(dolarValue,2)
	elif option == 2:
		calcularPorcentajesTool.setTool(dolarValue)
	elif option == 3:
		digitalWeightTool.setTool()
	elif option == 4:
		dolarValue = dolarValueTool.setTool(dolarValue)
	elif option == 5:
		break