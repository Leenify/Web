from flask import Flask
import random

app = Flask(__name__)

@app.route("/") 
def hello_World(): 
    return '<h1>¡Hola!<br> aquí puedes ver datos</h1> <a href="/facts">¡Ver un dato aleatorio!</a>'     

facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo viendo contenido.",              
              "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
              "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.",
              "El estudio de la adicción tecnológica es una de las áreas más relevantes de la investigación científica moderna."
            ] 
@app.route("/facts") 
def facts(): 
    return f'<p>{random. choice(facts_list)}</p>'
                  
app.run(debug=True)