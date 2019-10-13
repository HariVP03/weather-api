import tkinter as tk
import requests

def get_format(weather):
	try:
		name=weather['name']
		desc=weather['weather'][0]['description']
		temp=weather['main']['temp']
		lon=weather['coord']['lon']
		lat=weather['coord']['lat']
		pres=weather['main']['pressure']
		hum=weather['main']['humidity']
		tempmin=weather['main']['temp_min']
		tempmax=weather['main']['temp_max']
		windspeed=weather['wind']['speed']
		
		return '\n'+ 'Name Of City: ' + str(name) + '\n' + 'Description Of Weather: ' + str(desc) + '\n' + 'Temperature (F): ' + str(temp) + '\n' + 'Longitude: ' + str(lon) + '\n' + 'Latitude: ' + str(lat) + '\n' + 'Pressure: '+  str(pres) + '\n' + 'Humidity: ' + str(hum) + '\n' + 'Minimum Temp: ' + str(tempmin) + '\n' + 'Max Temp: ' + str(tempmax) + '\n' + 'Wind Speed: ' + str(windspeed)
	except:
		print('Unable To Retrive Information')

def get_weather(city):
	url='https://api.openweathermap.org/data/2.5/weather'
	weather_key=#Hidden
	params={'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response= requests.get(url, params=params)
	weather= response.json()

	text['text'] = get_format(weather)

root = tk.Tk()

canvas=tk.Canvas(root, bg='#85C1E9', width=400, height=500)
canvas.pack()

background_image=tk.PhotoImage(file='background3.png')
background_label=tk.Label(canvas, image=background_image)
background_label.pack()

frame=tk.Frame(root, bg='#85C1E9')
frame.place(relheight=0.069, relwidth=0.5, x=335, y=94.5)

entry=tk.Entry(root, font='SegoeUI', bd=2)
entry.place(relheight=0.05, relwidth=0.45, x=340, y=100)

search_image=tk.PhotoImage(file='SearchButton.png')
button=tk.Button(root, image=search_image, relief='ridge', command=lambda: get_weather(entry.get()))
button.place(x=1000, y=100, relheight=0.05, relwidth=0.035)

frame2=tk.Frame(root, bg='#85C1E9')
frame2.place(relheight=0.525, relwidth=0.72, x=190, y=290)

text=tk.Label(root, font=('SegoeUI', 20), bd=2)
text.place(relheight=0.5, relwidth=0.7, x=200, y=300)

root.mainloop()
