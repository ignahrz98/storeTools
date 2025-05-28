from menuApp import mainMenuApp
from menuApp import currencyConverterMenu
from currencyConverter import currencyConverterTool
from calcularPorcentajes import calcularPorcentajesTool
from digitalWeight import digitalWeightTool
from dolarValue import dolarValueTool

print("\nPara iniciar la aplicación, ingrese tasa cambiaria ($1)")

while True:
	try:
		dolarValue = float(input("\nIngrese el valor del dolar en su moneda: "))
		break
	except:
		input("\nEl valor ingresado es inválido. Ingrese solamente números.")

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