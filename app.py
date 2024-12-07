from flask import Flask, render_template, request, jsonify
from Ahorcado import Ahorcado

app = Flask(__name__)

# Instancia global del juego
juego = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    global juego
    data = request.get_json()
    palabra = data.get('palabra', '').upper()
    if palabra:
        juego = Ahorcado(palabra)
        return jsonify({'message': 'Juego iniciado', 'palabra': ' '.join(juego.getPalabraEscondida())})
    return jsonify({'message': 'Error: No se ingresó una palabra'}), 400

@app.route('/guess_letter', methods=['POST'])
def guess_letter():
    global juego
    data = request.get_json()
    letra = data.get('letra', '').upper()
    if juego and letra:
        mensaje = juego.pruebaLetra(letra)
        return jsonify({
            'message': mensaje,
            'palabra': ' '.join(juego.getPalabraEscondida()),
            'vidas': juego.getVidas(),
            'letrasUsadas': juego.getLetrasUsadas()
        })
    return jsonify({'message': 'Error: Letra no válida'}), 400

@app.route('/guess_word', methods=['POST'])
def guess_word():
    global juego
    data = request.get_json()
    palabra = data.get('palabra', '').upper()
    if juego and palabra:
        mensaje = juego.verificarPalabra(palabra)
        return jsonify({'message': mensaje})
    return jsonify({'message': 'Error: Palabra no válida'}), 400

@app.route('/reset', methods=['POST'])
def reset_game():
    global juego
    if juego:
        juego.reset()
        return jsonify({'message': 'Juego reiniciado'})
    return jsonify({'message': 'No hay juego activo para reiniciar'}), 400

if __name__ == '__main__':
    app.run(debug=True)
