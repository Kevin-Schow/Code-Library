from tkinter import *
import requests
import json

root = Tk()
root.title('Air Quality')
root.iconbitmap('c:/Users/haugl/PycharmProjects/TutorialPlayground/Images/icon.ico')
root.geometry('550x100')

# https://docs.airnowapi.org/
# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=92648&distance=5&API_KEY=A0F3D9FF-41C2-47D6-8AA2-2FC1114787FB

# Create Zipcode Lookup function
def zipLookup():
    # zip.get()
    # zipLabel = Label(root, text=zip.get())
    # zipLabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get(
            'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip.get() + '&distance=5&API_KEY=A0F3D9FF-41C2-47D6-8AA2-2FC1114787FB')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if city == 'N Coastal Orange':
            city = 'Huntington Beach'

        if category == 'Good':
            weather_color = '#0c0'
        elif category == 'Moderate':
            weather_color = '#FFFF00'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#ff9900'
        elif category == 'Unhealthy':
            weather_color = '#FF0000'
        elif category == 'Very Unhealthy':
            weather_color = '#990066'
        elif category == 'Hazardous':
            weather_color = '#660000'

        root.configure(background=weather_color)
        myLabel = Label(root, text=city + ' Air Quality ' + str(quality) + ' ' + category,
                        font=('Helvetica', 20), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = 'Error...'

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text='Lookup Zipcode', command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)


root.mainloop()
