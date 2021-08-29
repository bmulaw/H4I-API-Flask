from flask import Flask, render_template, request
import requests, config

app=Flask(__name__, template_folder='templates')

@app.route('/',methods =["GET", "POST"])
def from_html():
    # https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/
    if request.method == "POST":
        company = request.form.get("company")
        return get_company(company)
    return render_template("index.html")

@app.route('/<company>', methods=["GET"])
def get_company(company):
    # https://rapidapi.com/apidojo/api/yahoo-finance1/
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
    querystring = {"symbol":company,"region":"US"}
    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': config.api_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    price =  "$" + str(round(response.json()['price']['regularMarketOpen']['raw'], 2))
    name = str(response.json()['price']['longName'])
    answer = name + "  \n  " + price
    return render_template('index.html', output=answer)

if __name__ == '__main__':
    app.run(debug=True)