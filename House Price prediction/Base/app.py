from flask import Flask, request, render_template
import pandas as pd
from model_factory import ModelFactory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    model_type = request.form['model_type']
    lot_frontage = float(request.form['lot_frontage'])  # Changed from square_feet
    lot_area = float(request.form['lot_area'])          # Changed from bedrooms
    ms_subclass = int(request.form['ms_subclass'])      # Changed from bathrooms

    # Load dataset
    data = pd.read_csv(r'C:\Users\admin\Desktop\House Price prediction\Base\data\target\house-prices-advanced-regression-techniques\train\train.csv')
    print(data.head(5))
    
    # Prepare features
    X = data[['LotFrontage', 'LotArea', 'MSSubClass']]  # Updated feature names
    y = data['SalePrice']                                 # Updated target variable

    # Create and train model
    model = ModelFactory.create_model(model_type)
    model.train(X, y)

    # Prepare input for prediction
    features = [[lot_frontage, lot_area, ms_subclass]]  # Updated input features
    prediction = model.predict(features)

    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
