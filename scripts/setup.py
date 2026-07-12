"""This is the setup file for the coutries.csv"""

import turtle
import pandas

screen = turtle.Screen()

image = "../resources/africa-map.gif"
screen.title("Africa")
screen.addshape(image)

turtle.shape(image)


def map_country(x, y):
    """Updates the 'countries' csv"""

    country = {
        "country": [],
        "x": [],
        "y": []
    }

    country_name = screen.textinput(
        "Country Mapper", prompt="What is this country").title()
    country["country"].append(country_name)
    country["x"].append(x)
    country["y"].append(y)

    data = pandas.DataFrame(country)
    data.to_csv("../resources/countries.csv", mode='a',
                header=False, index=False)  # append to csv file
    
    t = turtle.Turtle(visible=False)
    t.penup()
    t.goto((x, y))
    t.write(country_name)
    
# Create csv file
countries_dict = {
    "country": [],
    "x": [],
    "y": []
}
countries = pandas.DataFrame(countries_dict)
countries.to_csv("../resources/countries.csv")


turtle.onscreenclick(map_country)


turtle.mainloop()
