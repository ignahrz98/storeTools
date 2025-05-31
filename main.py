import json
from menu_app import main_menu_app
from menu_app import currency_converter_menu
from currency_converter import currency_converter_tool
from calculate_earning import calculate_earning_tool
from digital_weight import digital_weight_tool
from dolar_value import dolar_value_tool

# Get the dolar_value from the file.
try:
	with open("data/dolar_value.json", "r") as file_dolar_value:
		data = json.load(file_dolar_value)
		dolar_value = data["dolar_value"]

		print("Valor del dólar cargado desde el archivo.")
except:
	data = {
		"dolar_value": 0.0
	}

	# Create file for dolar_value
	with open("data/dolar_value.json", "w") as file_dolar_value:
		json.dump(data, file_dolar_value, indent=4)
		print("El archivo para valor del dólar ha sido creado")

	dolar_value = data["dolar_value"]

# Show the main menu.
while True:
	option = main_menu_app.get_menu(dolar_value)

	if option == 1:
		option_currency_converter_menu = currency_converter_menu.get_menu()

		if option_currency_converter_menu == 1:
			currency_converter_tool.set_tool(dolar_value,1)
		elif option_currency_converter_menu == 2:
			currency_converter_tool.set_tool(dolar_value,2)
	elif option == 2:
		calculate_earning_tool.set_tool(dolar_value)
	elif option == 3:
		digital_weight_tool.set_tool()
	elif option == 4:
		dolar_value = dolar_value_tool.set_tool(dolar_value)
	elif option == 5:
		break