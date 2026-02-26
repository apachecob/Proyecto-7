from flask import Flask, request, jsonify
import joblib
import pandas as pd
import math

app = Flask(__name__)

# Cargar modelo y columnas
model = joblib.load("modelo_final.pkl")
columns = joblib.load("columnas_modelo.pkl")

@app.route("/")
def home():
    return "API Google Play Success Prediction"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        
        # Crear dataframe vacío con todas las columnas
        input_df = pd.DataFrame(0.0, index=[0], columns=columns)
        
        # Transformaciones numéricas
        installs_log = math.log1p(data["Installs"])
        price_log = math.log1p(data["Price"])
        size_log = math.log1p(data["Size_KB"])
        is_paid = 1 if data["Type"] == "Paid" else 0
        
        input_df.at[0, "Installs_log"] = installs_log
        input_df.at[0, "Price_log"] = price_log
        input_df.at[0, "Size_log"] = size_log
        input_df.at[0, "IsPaid"] = is_paid
        
        # One-hot Category
        category_col = f"Category_{data['Category']}"
        if category_col in input_df.columns:
            input_df.at[0, category_col] = 1
        
        # One-hot Content Rating
        content_col = f"Content Rating_{data['Content_Rating']}"
        if content_col in input_df.columns:
            input_df.at[0, content_col] = 1
        
        # Type_Paid
        if "Type_Paid" in input_df.columns:
            input_df.at[0, "Type_Paid"] = is_paid
        
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]
        
        return jsonify({
        "prediction": int(prediction),
        "probability_success": float(probability)
     })
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)