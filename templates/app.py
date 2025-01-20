
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

options = ["Taş", "Kağıt", "Makas"]
results = {}

@app.route('/')
def home():
    return '''
<h1>Taş, Kağıt, Makas Oyunu</h1>
<form action="/play" method="post">
    <label for="name">Adınız:</label><br>
    <input type="text" id="name" name="name" required><br><br>
    <label for="choice">Seçiminiz:</label><br>
    <select id="choice" name="choice">
        <option value="Taş">Taş</option>
        <option value="Kağıt">Kağıt</option>
        <option value="Makas">Makas</option>
    </select><br><br>
    <button type="submit">Oyna</button>
</form>
'''

@app.route('/play', methods=['POST'])
def play():
    name = request.form['name']
    player_choice = request.form['choice']

    player_wins, computer_wins = 0, 0
    for _ in range(10):
        computer_choice = random.choice(options)
        if (player_choice == "Taş" and computer_choice == "Makas") or             (player_choice == "Kağıt" and computer_choice == "Taş") or             (player_choice == "Makas" and computer_choice == "Kağıt"):
            player_wins += 1
        elif player_choice != computer_choice:
            computer_wins += 1

    results[name] = {"Player Wins": player_wins, "Computer Wins": computer_wins}
    return f'''
<h2>Oyun Sonuçları:</h2>
<p>{name}, {player_choice} seçti ve {player_wins} kez kazandı!</p>
<p>Bilgisayar ise {computer_wins} kez kazandı!</p>
<p><strong>Sonuçları Barto'dan Öğrenebilirsiniz.</strong></p>
'''

@app.route('/results', methods=['GET'])
def get_results():
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
