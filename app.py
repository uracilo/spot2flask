from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route('/')
def home():
    df = pd.read_json("https://82n0gj3j74.execute-api.us-east-1.amazonaws.com/pizza_distance_spot")
    temp = df.to_dict('records')
    columnNames = df.columns.values
    return render_template('home.html', records=temp, colnames=columnNames)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')