# Guess The Country

A small interactive Python game that asks players to identify countries on a continent map (currently Africa). The game shows a map image and players type country names. Correct guesses are written onto the map.

## How to play

1. Run the game (instructions below).
2. A map window opens. Type the name of a country when prompted.
3. Correct guesses are placed at the country coordinates and counted.
4. Continue until you stop or until all countries are guessed.
5. Type 'exit' or 'Exit' once you are done with guessing.

## Files and resources

- scripts/
  - main.py — game loop that prompts for guesses and draws names.
  - setup.py — helper to add new country coordinates by clicking on the map.
  - classes/country.py — Turtle subclass that renders a country name on the map.
- resources/
  - africa-map.gif — map image used by the game.
  - countries.csv — CSV of saved country names and coordinates (columns: index,country,x,y).
- README.md — this file

Notes on data format (resources/countries.csv)

- CSV columns: index, country, x, y
- Example row: 0,South Africa,69.0,-227.0

## How to create a dataset for your own continent

1. Copy `resources/africa-map.gif` to a new map image for your continent (e.g., `resources/europe-map.gif`).
2. Create a new empty CSV at `resources/countries_<continent>.csv` with the same header structure (index,country,x,y) or let `scripts/setup.py` create it.
3. Update the image path in `scripts/main.py` and `scripts/setup.py` to point to your new GIF and the new CSV filename.
4. Run `scripts/setup.py` and click on each country on the map window; enter the country name when prompted. The script saves coordinates to the CSV.
5. After collecting coordinates, run `scripts/main.py` to play using the new map and CSV.

## Requirements

- Python 3.8+
- pandas (`pip install pandas`)

## How to run everything (macOS)

1. Open Terminal and change to the project root:
   cd /guess_the_country
2. Install pandas if needed:
   pip3 install pandas
3. Create or update the CSV by running the setup script (click country on map to add the countries):
   python scripts/setup.py
4. Run the game:
   python scripts/main.py

Tips

- Ensure the GIF path and CSV path in both scripts match your filenames.
- The scripts use relative paths (e.g., `../resources/...`) from the `scripts/` directory.
- If the Turtle window closes unexpectedly, re-run the script from the Terminal to see errors.
- Use a virtual environment
