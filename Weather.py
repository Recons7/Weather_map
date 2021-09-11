import requests
import time, os, pyfiglet


from termcolor import colored

os.system('clear')

print(colored(pyfiglet.figlet_format("Weather"), "green"))
BOLD = '\033[1m'
END = '\033[0m'

print(colored("\n\n"+"="*50, "yellow"))
print(colored(BOLD+'\n\t    WEATHER MAP BY :- SURAJ SHARMA'+END, "blue"))
print(colored("\n"+"="*50, "yellow"))

def weather():
	
	city = input("\n\nEnter your city : ")
	
	r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ff189edaab5a0d9cf74220087f0b69e9')
	
	print("\n")
	print(colored("\n"+"="*50, "yellow"))
	print(colored(f"\n\n'{r.json()['weather'][0]['description']}' at {city}", "magenta"))
	
	print("\n")

	print(colored(f"\nTemeperature : {int(r.json()['main']['temp']-273.15)}°C\n", "yellow"))
	
	print("\n")
	
	print(colored(f"Wind speed : {r.json()['wind']['speed']}", "cyan"))
	
	print(colored("\n\n"+"="*50, "yellow"))
	print("\n")
	
	
	#pprint.pprint(r.json())
	
	weather()
weather()
