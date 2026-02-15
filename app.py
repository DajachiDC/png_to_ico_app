from flask import Flask, render_template, request, send_file
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convertir", methods=["POST"])
def convertir():
    archivo = request.files["imagen"]

    if archivo.filename == "":
        return "No seleccionaste archivo"

    ruta_png = os.path.join(UPLOAD_FOLDER, archivo.filename)
    archivo.save(ruta_png)

    img = Image.open(ruta_png)

    ruta_ico = ruta_png.replace(".png", ".ico")
    img.save(ruta_ico, format="ICO", sizes=[(256, 256)])

    return send_file(ruta_ico, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
