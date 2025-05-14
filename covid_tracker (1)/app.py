from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    global_data = requests.get("https://disease.sh/v3/covid-19/all").json()
    countries_data = requests.get("https://disease.sh/v3/covid-19/countries").json()
    return render_template("index.html", global_data=global_data, countries=countries_data)

@app.route('/country/<name>')
def country(name):
    country_data = requests.get(f"https://disease.sh/v3/covid-19/countries/{name}").json()
    return render_template("country.html", data=country_data)

if __name__ == '__main__':
    app.run(debug=True)
