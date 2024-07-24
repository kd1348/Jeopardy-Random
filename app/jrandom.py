# app/jrandom.py
import requests
from flask import render_template, Blueprint, request, redirect, url_for

jrandom = Blueprint('jrandom', __name__)

@jrandom.route('/')
def index():
    return render_template('index.html')

@jrandom.route('/choose_difficulty', methods=['POST'])
def choose_difficulty():
    num = int(request.form.get('difficulty'))
    if num == 0:
        dif = ''
    elif 1 <= num <= 5:
        dif = f'?difficulty={num}'
    else:
        return "Invalid Entry", 400

    random_clue = get_random_clue(dif)
    if random_clue:
        return render_template('clue.html', category=random_clue['category'], clue=random_clue['clue'], response =random_clue['response'])
    else:
        return "Unable to fetch a random clue.", 500

def get_random_clue(dif):
    url = f'http://cluebase.lukelav.in/clues/random{dif}'
    response = requests.get(url)
   
    if response.status_code == 200:
        clues_data = response.json().get('data', [])
        if clues_data:
            return clues_data[0]
    return None
