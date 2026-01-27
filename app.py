from flask import Flask, render_template
import mysql.connector
import base64

app = Flask(__name__)

# Configuración de Docker (puerto 3310 -> 3306 interno)
db_config = {
    'host': '127.0.0.1',
    'port': 3310,
    'user': 'root',
    'password': 'root',
    'database': 'main'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Traemos los juegos de la tabla 'games'
    cursor.execute("SELECT * FROM games")
    games_list = cursor.fetchall()
    
    # Convertimos los BLOBs a Base64 para mostrarlos en el HTML
    for game in games_list:
        if game['cover']:
            game['cover_b64'] = base64.b64encode(game['cover']).decode('utf-8')
        if game['creator-pic']:
            game['creator_pic_b64'] = base64.b64encode(game['creator-pic']).decode('utf-8')
            
    cursor.close()
    conn.close()
    
    return render_template('index.html', games=games_list)

if __name__ == '__main__':
    app.run(debug=True)