""" importacion librerias necesarias"""
from flask import Flask, request, redirect,Response
app = Flask(__name__)
@app.route("/",methods=["GET"])
def index():
    """ ruta index"""
    return redirect("http://localhost/prepara_pedido.html", code=302)
@app.route("/pizza",methods=["GET","POST"])
def mostrar_ruta():
    """ obtiene campos para viajar a otro html"""
    name = request.form.get("nombreCliente")
    surname = request.form.get("apellidosCliente")
    print(name,surname)
    return redirect( "http://localhost/solicita_pedido.html", code=302)
@app.route("/checksize",methods=['POST'])
def checksize():
    """Comprueba disponibilidad de un tamaño de pizza."""
    size_pizza = request.form.post("size")
    if size_pizza=="S":
        mensaje = "tamaño pizza no disponible"
        return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})    
    

if __name__ == '__main__':
    """ ruta inicial """
    app.run()
 