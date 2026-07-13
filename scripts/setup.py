"""This is the setup file for the coutries.csv"""

import turtle
import pandas
from classes.country import Country

screen = turtle.Screen()

image = "../resources/africa-map.gif"
screen.title("Africa")
screen.addshape(image)

turtle.shape(image)

countries_template = {
    "country": [],
    "x": [],
    "y": []
}

try:
    with open("../resources/countries.csv") as file:
        data = file.readlines()
        if data[1:] == '':
            pass

        for country in data[1:]:
            country_info = country.split(",")

            get_country = country_info[1]
            get_x = float(country_info[2])
            get_y = float(country_info[3].replace("\n", ''))

            countries_template["country"].append(get_country)
            countries_template["x"].append(get_x)
            countries_template["y"].append(get_y)

            t_country = Country(get_country, (get_x, get_y))
except:
    print("A new csv file will be created!")


def add_to_dict(country, x_coord, y_coord):
    countries_template["country"].append(country)
    countries_template["x"].append(x_coord)
    countries_template["y"].append(y_coord)


countries_turtles = []


def event_handler(x, y):
    try:
        response = screen.textinput(
            title="Enter the country", prompt="What is the name of the country?").title() # type: ignore
    except:
        response = "no guess"

    country = Country(response, (x, y))
    countries_turtles.append(country)
    add_to_dict(response, x, y)


turtle.onscreenclick(event_handler)
turtle.mainloop()

countries_data = pandas.DataFrame(countries_template)
countries_data.to_csv("../resources/countries.csv")
