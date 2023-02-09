from tkinter import *
import requests
import json


if __name__ == '__main__':
    root = Tk()
    root.geometry('173x136+700+260')
    root.title('Weather App')

    Zip = Entry()
    def temp_text1(e):
        Zip.delete(0, "end")
    def temp_text2(e):
        Range.delete(0, "end")
    Zip.insert(0, 'Enter Zip Code')
    Zip.grid(row=1, column=1, padx=5, columnspan=3)
    Zip.bind("<FocusIn>", temp_text1)
    Range = Entry()
    Range.insert(0, 'Enter Range')
    Range.grid(row=2, column=1, padx=5, columnspan=3)
    Range.bind('<FocusIn>', temp_text2)


    def getreport():

        address = 'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+str(Zip.get())+'&distance='+str(Range.get())+'&API_KEY=E00DBB5A-3579-4B4E-A873-E5ADC9DE6676'

        api_request = requests.get(address)
        if api_request != '':

            api = json.loads(api_request.content)

            root.geometry('174x219')
            city = ''
            quality1 = StringVar
            quality2 = StringVar
            quality3 = StringVar
            for data in api:
                if data['ParameterName'] == 'O3':
                    city = data['ReportingArea']
                    quality1 = data['Category']['Name']
                    aqi1 = data['AQI']
                if data['ParameterName'] == 'PM2.5':
                    quality2 = data['Category']['Name']
                    aqi2 = data['AQI']
                if data['ParameterName'] == 'PM10':
                    quality3 = data['Category']['Name']
                    aqi3 = data['AQI']
            City = Label(root, text=city)
            City.grid(row=4, column=1, columnspan=2)

            O3 = Label(root, text='O3', anchor=W, width=5)
            O3.grid(row=5, column=1)
            O3value = Label(root, text=quality1)
            O3value.grid(row=5, column=2)

            PM2 = Label(text='PM2.5', anchor=W, width=5)
            PM2.grid(row=6, column=1)
            PM2value = Label(text=quality2)
            PM2value.grid(row=6, column=2)

            PM10 = Label(text='PM10', anchor=W, width=5)
            PM10.grid(row=7, column=1)
            PM10value = Label(text=quality3)
            PM10value.grid(row=7, column=2)

            global count
            count = 0
            records = [quality1, quality2, quality3]
            quality = ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous',
                       'Unavailable']
            colour = {'Good': '#00FF00', 'Moderate': '#FFFF00', 'Unhealthy for Sensitive Groups': '#FFA500',
                      'Unhealthy': '#FF0000', 'Very Unhealthy': '#A020F0', 'Hazardous': '#800000',
                      'Unavailable': '#FFFFFF'}
            for record in records:
                count += 1
                for q in quality:
                    if record == q:
                        if count == 1:
                            O3value.config(bg=colour.get(record))
                            break
                        if count == 2:
                            PM2value.config(bg=colour.get(record))
                            break
                        if count == 3:
                            PM10value.config(bg=colour.get(record))
                            break

            def details():
                root.geometry('248x270')
                Details.destroy()
                Zip.config(width=29)
                Range.config(width=29)
                Get.config(padx=38)
                Details1 = Button(root, text='More Details', command=details)
                Details1.grid(row=8, column=1, columnspan=3, padx=2, pady=2, ipadx=76)
                Latitude = data['Longitude']
                Longitude = data['Latitude']
                Lat = Label(root, text='Latitude:', anchor=W, width=9)
                Lat.grid(row=9, column=1)
                Lat = Label(root, text='    ' + str(Latitude), anchor=E, width=10)
                Lat.grid(row=9, column=2)

                Long = Label(root, text='Longitude:', anchor=W, width=9)
                Long.grid(row=10, column=1)
                Long = Label(root, text='    ' + str(Longitude), anchor=E, width=10)
                Long.grid(row=10, column=2)

                AQI = Label(root, text='AQI', anchor=W, width=9)
                AQI.grid(row=4, column=3)
                AQI1 = Label(root, text=aqi1, anchor=W, width=9)
                AQI1.grid(row=5, column=3)
                AQI2 = Label(root, text=aqi2, anchor=W, width=9)
                AQI2.grid(row=6, column=3)
                AQI3 = Label(root, text=aqi3, anchor=W, width=9)
                AQI3.grid(row=7, column=3)

            Details = Button(root, text='More Details', command=details)
            Details.grid(row=8, column=1, columnspan=2, padx=2, pady=2, ipadx=39)

        else:
            Error = Label(root, text='Network Error\nPlease try again later!')
            Error.grid(row=4, column=1, colunspan=2)


    Get = Button(root, text='Get Report', command=getreport)
    Get.grid(row=3, column=1, columnspan=5, padx=2, ipadx=44)

    mainloop()
