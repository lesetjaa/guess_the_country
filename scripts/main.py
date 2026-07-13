import turtle
import pandas
from classes.country import Country

screen = turtle.Screen()
image = "../resources/africa-map.gif"
screen.title("Map the Continent")
screen.addshape(image)
screen.tracer(0)

turtle.shape(image)

data = pandas.read_csv("../resources/countries.csv")


def find_country(country_name):
    return data[data.country == country_name]


guessed_countries = []

while len(guessed_countries) < 50:
    screen.update()
    no_correct_guesses = len(guessed_countries)

    try:
        answer = screen.textinput(
            title=f"{no_correct_guesses}/54 Countries Guessed!", prompt="Guess the Country").title() # type: ignore
    except:
        answer = "no guess"

    if answer == "Exit":
        print("Countries To Learn: \n")
        countries = data.country.items()
        for _, country in countries:
            if country not in guessed_countries:
                print(country)
        break


    try:
        country = find_country(answer)
        country_coord = (country.x.item(), country.y.item())
        country = Country(answer.title(), (country_coord))
        guessed_countries.append(answer)
    except:
        pass