import json
import requests
from menu_app import main_menu_app
from menu_app import currency_converter_menu
from currency_converter import currency_converter_tool
from calculate_earning import calculate_earning_tool
from digital_weight import digital_weight_tool
from dolar_value import dolar_value_tool
from tkcalendar import DateEntry

import tkinter as tk
from tkinter import messagebox

def history_exchange_rate():
	date = cal.get()
	url = f"https://ve.dolarapi.com/v1/historicos/dolares/oficial/{date}"

	response = requests.get(url)
	data = response.json()

	print(f"({date}): {data.get('promedio')} bs")
	label_history_date.config(text=f"({date}): {data.get('promedio')} bs")


window = tk.Tk()
window.title("Store tools")
window.geometry("400x300")
window.resizable(False, False)

top_menu = tk.Menu(window)
window.config(menu=top_menu)

tools_menu = tk.Menu(top_menu, tearoff=0)
top_menu.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Calculate earning", command=lambda: calculate_earning_tool.toplevel_calculate_earning_tool(window))
tools_menu.add_command(label="Currency converter", command=lambda: currency_converter_tool.toplevel_currency_converter(window, data.get('promedio')))
tools_menu.add_command(label="Digital weight", command=lambda: digital_weight_tool.toplevel_digital_weight_tool(window))

config_menu = tk.Menu(top_menu, tearoff=0)
top_menu.add_cascade(label="Config", menu=config_menu)
config_menu.add_command(label="Update dollar value", command=lambda: dolar_value_tool.toplevel_dolar_value(window, text_variable_dolar_value))

# Get the dolar_value from the file.
try:
	with open("data/dolar_value.json", "r") as file_dolar_value:
		data = json.load(file_dolar_value)
		dolar_value = data["dolar_value"]

		print("Dolar value loaded from file") 
except:
	data = {
		"dolar_value": 0.0
	}

	# Create file for dolar_value
	with open("data/dolar_value.json", "w") as file_dolar_value:
		json.dump(data, file_dolar_value, indent=4)
		print("File for dolar value have been created")

	dolar_value = data["dolar_value"]

text_variable_dolar_value = tk.StringVar(value=f"{dolar_value}")
"""
label_dolar_value = tk.Label(textvariable=text_variable_dolar_value)
label_dolar_value.pack()
"""
try:
	url = "https://ve.dolarapi.com/v1/dolares/oficial"
	response = requests.get(url)
	data = response.json()
	print("Dollar value loaded from API")
	messagebox.showinfo(message="Official Exchange Rate updated")
except:
	print("Error loading dollar from API")
	messagebox.showerror(message="Official Exchange Rate can't be updated")

label_title_exchange_rate = tk.Label(window, text="Dollar - Exchange Rate", font=("TkDefaultFont",16, "bold"))
label_title_exchange_rate.pack(pady=(0,10))

frame_exchange_rates = tk.Frame(window, relief=tk.RAISED, borderwidth=4)
frame_exchange_rates.pack()
label_title_custom_exchange_rate = tk.Label(frame_exchange_rates, text="Custom", font=("TkDefaultFont",10, "bold"))
label_title_custom_exchange_rate.grid(row=0, column=0, padx=60)
custom_exchange_rate = tk.Label(frame_exchange_rates, textvariable=text_variable_dolar_value, font=(14))
custom_exchange_rate.grid(row=1, column=0)
label_title_official_exchange_rate = tk.Label(frame_exchange_rates, text="Official", font=("TkDefaultFont",10, "bold"))
label_title_official_exchange_rate.grid(row=0, column=1)
official_exchange_rate = tk.Label(frame_exchange_rates, text=f"{data.get('promedio')}", font=(14))
official_exchange_rate.grid(row=1, column=1)
official_exchange_rate_date = tk.Label(frame_exchange_rates, text=f"{data.get('fechaActualizacion')}")
official_exchange_rate_date.grid(row=2, column=1)

label_history = tk.Label(window, text="Introduce date of exchange rate", font=("TkDefaultFont",16, "bold"))
label_history.pack()

cal = DateEntry(
	window,
	width=12,
	borderwidth=2,
	date_pattern='yyyy/mm/dd'
)
cal.pack()

btn_history = tk.Button(window, command=history_exchange_rate, text="Date")
btn_history.pack(pady=(10,0))

label_history_date = tk.Label(window, font=(14))
label_history_date.pack(pady=10)

# Show the main menu.
"""
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
"""
window.mainloop()