from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/pokemon-image/<name>')
def get_pokemon_image(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Pokémon not found'}), 404

    data = response.json()
    image_url = data['sprites']['other']['official-artwork']['front_default']

    return jsonify({
        'name': name,
        'image_url': image_url
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
