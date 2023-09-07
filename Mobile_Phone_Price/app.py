from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('mobile_phone_price.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Storage = float(request.form['Storage'])
        RAM = float(request.form['RAM'])
        Screen = float(request.form['Screen'])
        Battery = float(request.form['Battery'])
        CamPixels = float(request.form['CamPixels'])
        codeBrand = int(request.form['codeBrand'])
        
        # Make a prediction using the loaded model
        input_features = [[Storage, RAM, Screen, Battery, CamPixels, codeBrand]]
        price_prediction = model.predict(input_features)

        return render_template('index.html', prediction=price_prediction[0])
    
if __name__ == '__main__':
    app.run(debug=True)
