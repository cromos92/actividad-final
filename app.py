""" importacion librerias necesarias"""
from flask import Flask, request, redirect,Response,render_template
app = Flask(__name__)
@app.route("/",methods=["GET"])
def index():
    """ ruta index"""
    return render_template("prepara_pedido.html")
@app.route("/pizza",methods=["GET","POST"])
def mostrar_ruta():
    """ obtiene campos para viajar a otro html"""
    name = request.form.get("nombreCliente")
    surname = request.form.get("apellidosCliente")
    print(name,surname)
    return render_template( "solicita_pedido.html")
@app.route("/checksize",methods=['POST'])
def checksize():
    """Comprueba disponibilidad de un tamaño de pizza."""
    data = request.json
    print(data['size'])
    if data['size']=="S":
        mensaje = "tamaño pizza no disponible"
        return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})    
    else:
        mensaje = "tamaño pizza  disponible"
        return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})    

if __name__ == '__main__':
    """ ruta inicial """
    app.run(debug=True)
 