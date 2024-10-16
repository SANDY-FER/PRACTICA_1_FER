from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/contactos")
def contac_route():
    coordenadas = (40.7128, -78.0060)
    return render_template("contactos.html", coordenadas=coordenadas)

@app.route("/formulario")
def form_route():
    return render_template("formulario.html")

@app.route("/proceso", methods=['POST'])
def proceso():
    nombre = request.form.get('name')
    email = request.form.get('email')
    mensaje = request.form.get('message')
    return render_template("salida.html", nombre=nombre, email=email, mensaje=mensaje)

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/ubicacion")
def ubicacion():
    return render_template("ubicacion.html")

@app.route("/habilidades")
def habilidades():
    return render_template("habilidades.html")

if __name__ == "__main__":
    app.run(debug=True, port=5017)
