from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon/<id_or_name>')
def pokemon(id_or_name):
	try:
		int(id_or_name)
		return "You found a " + requests.get('https://pokeapi.co/api/v2/pokemon/' + id_or_name).json()['name'] + "!"
	except ValueError:
		return "The ID number is: "+ str(requests.get('https://pokeapi.co/api/v2/pokemon/' + id_or_name).json()['id'])

if __name__ == '__main__':
    app.run()
