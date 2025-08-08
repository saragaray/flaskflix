from flask import Flask, render_template

# Inicializar la aplicación Flask
app = Flask(__name__)

# Datos de los videos (simulando una base de datos)
# Puedes cambiar estos videos por los que prefieras.
# Solo necesitas el ID del video de YouTube.
videos = [
    {
        'id': 'Vff5vxQfstA',
        'titulo': 'Entrada Triunfal de RORO',
        'canal': 'SENIOR AM'
    },
    {
        'id': 'R_h-fdb83gA',
        'titulo': '¿Qué es una API? La explicación más sencilla',
        'canal': 'Nate Gentile'
    },
    {
        'id': '8j_m_h2215s',
        'titulo': 'El video 4K más IMPRESIONANTE del espacio',
        'canal': 'Melodysheep'
    },
    {
        'id': 'l-ASH2y2Qp4',
        'titulo': '15 Trucos de Visual Studio Code',
        'canal': 'MoureDev by Brais Moure'
    }
]

# Definir la ruta principal de la aplicación
@app.route('/')
def index():
    # 'render_template' buscará 'index.html' en la carpeta 'templates'
    # y le pasará la lista de videos para que la pueda usar.
    return render_template('index.html', videos=videos)

# Esto es necesario para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)