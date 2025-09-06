from flask import Flask, request, render_template_string, send_file
import pandas as pd
import pickle

with open('fd_model.pkl', 'rb') as f:
    model = pickle.load(f)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
        <h2>FD Rate Predictor</h2>
        <form action="/predict" method="post">
            Bank: <input name="bank"><br>
            Tenure: <input name="tenure"><br>
            <input type="submit" value="Predict">
        </form>
        <a href="/download-fd-rates">📥 Download FD Rates CSV</a>
    """)

@app.route("/predict", methods=["POST"])
def predict():
    bank = request.form["bank"]
    tenure = request.form["tenure"]
    # Dummy prediction logic
    return f"<h3>Predicted rate for {bank} ({tenure}): 7.25%</h3><a href='/'>Back</a>"

@app.route("/download-fd-rates")
def download_fd_rates():
    return send_file("fd_rates.csv", as_attachment=True)

@app.route("/refresh-data")
def refresh_data():
    refresh_fd_data()
    return "<h3>FD data refreshed and saved to CSV.</h3><a href='/'>Back</a>"


if __name__ == "__main__":
    app.run(debug=True)

