from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

options = ["Taş", "Kağıt", "Makas"]
results = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    name = request.form['name']
    choice = request.form['choice']
    rounds = []

    for _ in range(10):
        system_choice = random.choice(options)
        if choice == system_choice:
            result = "Beraberlik"
        elif (choice == "Taş" and system_choice == "Makas") or \
             (choice == "Kağıt" and system_choice == "Taş") or \
             (choice == "Makas" and system_choice == "Kağıt"):
            result = "Kazandınız"
        else:
            result = "Kaybettiniz"

        rounds.append({'system': system_choice, 'result': result})

    results[name] = rounds
    return render_template('results.html', name=name, rounds=rounds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
