import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from tkinter import *

app = Tk()
app.configure(background='gray')
app.geometry('600x390')
app.resizable(0,0)
app.title('Phone Number Locator App')

country = StringVar(value='Country:')
provider = StringVar(value='Provider:')
time_zone = StringVar(value='Time Zone:')

heading_text = Label(app, text='Internet speed evaluator App', font='Arial 16 bold', fg='yellow', bg='black')
heading_text.grid(row=0, column=1, pady=30)

type_label = Label(app, text='Type a phone number with the country code:', font='Arial 12 bold', fg='white', bg='green')
type_label.place(x=0, y=68)

phone_entry = Entry(app, width=15, font='Arial 11 bold')
phone_entry.place(x=430, y=68)

country_label = Label(app, textvariable=country, font='Arial 11 bold', fg='white', bg='gray')
country_label.place(x=20, y=120)

provider_label = Label(app, textvariable=provider, font='Arial 11 bold', fg='white', bg='gray')
provider_label.place(x=20, y=180)

tz_label = Label(app, textvariable=time_zone, font='Arial 11 bold', fg='white', bg='gray')
tz_label.place(x=20, y=240)

def locate_phone():
    phone_number = phonenumbers.parse(phone_entry.get())
    country_val =  geocoder.description_for_number(phone_number, 'en')
    country.set(f"Country: {country_val}")
    provider_val = carrier.name_for_number(phone_number, 'en')
    provider.set(f"Provider: {provider_val}")    
    t_zone = timezone.time_zones_for_number(phone_number)
    time_zone.set(f"Time Zone: {t_zone}")

btn = Button(app, text='Locate Number', font='Arial 14 bold', fg='white', bg='green', border=5, command=locate_phone)
btn.place(x=20, y=290)

app.mainloop()

# phone = input('Enter phone number with the country code: ')
# phone_number = phonenumbers.parse(phone)

# country_name = geocoder.description_for_number(phone_number, 'en')

# service_provider = carrier.name_for_number(phone_number, 'en')

# time_zone = timezone.time_zones_for_number(phone_number)

# print(country_name)
# print(service_provider)
# print(time_zone)