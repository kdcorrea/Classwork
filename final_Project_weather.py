#Kristy D. Correa
#CIS245: Introduction to Programming
#October 12, 2020
#Final Project
#References: 
	#Python Crash Course (2nd ed.) by Eric Matthes
	#Python Requests Tutorial - How to Call a Weather API by Pretty Printed (https://www.youtube.com/watch?v=sbYXa6HJJ5M)
	#https://openweathermap.org/current
	#Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More by Corey Schafer (https://www.youtube.com/watch?v=tb8gHvYlCFs)
	#Python Exercise: Convert temperatures to and from celsius, fahrenheit by w3resource (https://www.w3resource.com/python-exercises/python-conditional-exercise-2.php)
	#OpenWeatherMap API - Overview by Get Set Python (https://www.youtube.com/watch?v=SXsaB9TUfkk)

#Requests library to import from webservice	
import requests

#Welcome message
print("Welcome to Your Weather Service.")

#p.194-204
try:
	#Ask for zip code.
	zip_code = input("What is your 5 digit zip code? ")
	print("Your zip code is correct.")

	#This checks if connection is successful.
	try:

		#This allows the program to loop.
		while zip_code:

			#This is the main function. (p. 130)
			def main():

				#This allows the user to call the data from OpenWeatherMap with the API id that I signed up for. (p.347; p.361)
				r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zip_code+',us&appid=cd9b312e810a5e958eceb985f427a554')
				data = r.json()

				#This allows us to see if the connection was successful.
				if r:
					print("You are now connected to OpenWeatherMap.org.")
				else:
					print("Unsuccessful connection or incorrect zip code. Please try again.")

				#These variables are assigned json data. Also, I'm converting Kelvin to Fahrenheit.
				get_info = data ["main"]
				get_tempk = get_info["temp"]
				get_temp = int((get_tempk - 273.13) * 9/5 + 32)
				get_pressure = get_info["pressure"]
				get_humidity = get_info['humidity']
				get_mintempk = get_info["temp_min"]
				get_mintemp = int((get_mintempk - 273.13) * 9/5 + 32)
				get_maxtempk = get_info["temp_max"]
				get_maxtemp = int((get_maxtempk - 273.13) * 9/5 + 32)

				#This displays the weather in a readable format.
				print("Temperature: {}°F.".format(get_temp))
				print("Temperature Range: {}°F to {}°F. ".format(get_mintemp, get_maxtemp))
				print("Pressure: {} hpa.".format(get_pressure))
				print("Humidity: {}%.".format(get_humidity))
				return

			#This calls the weather function to ouput the data.
			main()

			user_input = input("Would you like to check a different zip code? ")
			#This allows the user to stay in the program.
			if user_input == "yes" or user_input == "y":
				zip_code = input("What is your 5 digit zip code?")
			#This allows the user to exit.
			elif user_input == "no" or user_input == "n":
				print("Thank you for visiting our website. Please visit us again.")
			#This displays a error message and exits program when the user types anything other than yes, y, no, or n.
			else:
				print("Type Error. Incorrect input. You are now leaving the program. Thank you for visiting our website. Please visit us again")
				#This exits the looping immediately. (p.121)
				break

	except TypeError:
		print("Unsuccessful connection.")
except TypeError:
	print("Incorrect Zip Code. Please try again.")








































