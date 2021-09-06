from flask import Flask, render_template, request
import requests

app=Flask(__name__, template_folder='templates')

@app.route('/',methods =["POST"])
def get_capital():
    # https://restcountries.eu/
    country = request.form.get("country")
    url = "https://restcountries.eu/rest/v2/name/" + country + "?fullText=true"
    response = requests.get(url)
    if response: 
        answer = response.json()[0]['capital']
    else:
        answer = "PLEASE INPUT A CORRECT COUNTRY NAME"
    return render_template("index.html", name=country, capital=answer)

if __name__ == '__main__':
    app.run(debug=True)