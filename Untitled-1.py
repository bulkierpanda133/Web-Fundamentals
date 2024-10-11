
import requests
from bs4 import BeautifulSoup
import json



def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    return response.json()

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = []


for name in pokemon_names:
    data = fetch_pokemon_data(name)
    pokemon_info = {
        'name': data['name'],
        'abilities': [ability['ability']['name'] for ability in data['abilities']],
        'weight': data['weight']
    }
    pokemon_data.append(pokemon_info)


for pokemon in pokemon_data:
    print(f"Name: {pokemon['name']}")
    print(f"Abilities: {', '.join(pokemon['abilities'])}")
    print()


average_weight = calculate_average_weight(pokemon_data)
print(f"Average Weight: {average_weight}")



response = requests.get('https://www.codingtemple.com/')
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title.text)


# Fetch Planet Data
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_data = []

    # Process each planet's info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if planet['mass'] else 'N/A'
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else 'N/A'
            planet_data.append({
                'name': name,
                'mass': mass,
                'orbit_period': orbit_period
            })
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

    return planet_data

planets = fetch_planet_data()


# Find the heaviest planet
def find_heaviest_planet(planets):
    # Filter out planets with no mass data
    planets_with_mass = [planet for planet in planets if planet['mass'] != 'N/A']
    
    # Find the planet with the maximum mass
    heaviest_planet = max(planets_with_mass, key=lambda p: p['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']

# Find the planet with the longest orbit period
def find_longest_orbit_period(planets):
    # Filter out planets with no orbit period data
    planets_with_orbit = [planet for planet in planets if planet['orbit_period'] != 'N/A']
    
    # Find the planet with the maximum orbit period
    longest_orbit_planet = max(planets_with_orbit, key=lambda p: p['orbit_period'])
    return longest_orbit_planet['name'], longest_orbit_planet['orbit_period']

# Get the heaviest planet
heaviest_name, heaviest_mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {heaviest_name} with a mass of {heaviest_mass} kg.")

# Get the planet with the longest orbit period
longest_orbit_name, longest_orbit_period = find_longest_orbit_period(planets)
print(f"The planet with the longest orbit period is {longest_orbit_name} with an orbit period of {longest_orbit_period} days.")
