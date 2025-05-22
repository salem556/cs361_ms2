cat <<EOF > README.md
# Pokémon Image Microservice

This microservice was developed for CS361 Assignment 8: "Microservice A" Implementation (Milestone #2). It retrieves official Pokémon artwork based on the Pokémon name using the PokéAPI. The service is intended to be integrated into a Joshua's main application as part of a larger microservices-based system.

## How the Microservice Works

- Runs locally on http://localhost:5000
- Accepts a GET request with a Pokémon name
- Responds with JSON containing the Pokémon name and official image URL

## Endpoint

GET /pokemon-image/<pokemon_name>

Example:
GET http://localhost:5000/pokemon-image/Squirtle

## Success Response

{
  "name": "Squirtle",
  "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png"
}

## Failure Response

{
  "error": "Pokémon not found"
}

## Test Script Example (Python)

import requests

pokemon = "Squirtle"
url = f"http://localhost:5000/pokemon-image/{pokemon}"
response = requests.get(url)

try:
    data = response.json()
    if response.status_code == 200:
        print(f"Name: {data['name']}")
        print(f"Image URL: {data['image_url']}")
    else:
        print("Error:", data.get('error', 'Unknown error'))
except Exception as e:
    print("Failed to parse response:", response.text)
    print("Error details:", e)

## Setup Instructions

1. Clone or download this repository.
2. Install dependencies:
   pip3 install flask requests
3. Run the microservice:
   python3 microservice_a.py
4. In a separate terminal, run your test program.

## Communication Contract

- Endpoint: GET /pokemon-image/<pokemon_name>
- No authentication is required
- Input is case-insensitive
- pls do not edit the microservice code 

## UML Diagram

A UML sequence diagram showing the interaction between the requesting program, this microservice, and the PokéAPI is included in this repository as uml_sequence.png.

## Notes

- You must run the microservice locally
- Requires internet connection to access PokéAPI
- Works only with valid Pokémon names

## Status

Microservice implemented, tested, and ready for integration
EOF