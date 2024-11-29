from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ruta principal para mostrar el formulario de búsqueda
@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        weather = get_weather(city)
    return render_template("index.html", weather=weather)

# Ruta para mostrar tu hoja de vida
@app.route("/cv.html")
def cv():
    return render_template("cv.html")

# Función para obtener el clima de la ciudad
def get_weather(city):
    api_key = "e3d3e5f099cfac32b5c0989104e77043"  # Clave API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and "main" in data:
        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"]
        }
        return weather
    else:
        return {"error": "Ciudad no encontrada"}

if __name__ == "__main__":
    app.run(debug=True)
