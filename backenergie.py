from flask import Flask, jsonify, request,send_file
import pandas as pd

app = Flask(__name__)

# Simulated data (replace with actual data loading logic)
electricity_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar','Avr','Mai','Juin','Juil','Aout','Sept','Oct','NoV','Dec'],'Consumption': [100, 120, 110]})
gas_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar','Avr','Mai','Juin','Juil','Aout','Sept','Oct','NoV','Dec'],'Consumption': [50, 60, 55]})
water_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar','Avr','Mai','Juin','Juil','Aout','Sept','Oct','NoV','Dec'],'Consumption': [20, 25, 22]})

@app.route("/",methods=['GET'])
def get_default():
    return jsonify({'result': "App Running..."})

# Renvoie l'image
@app.route('/get_image')
def get_image():
    # Ici, vous pouvez ajouter votre logique pour récupérer l'image à afficher
    image_path = 'C:\\Users\\dgama\Desktop\\testback\\bird.png'  # Changer cela avec le chemin de votre image
    # Renvoie l'image
    return send_file(image_path, mimetype='image/png')


@app.route('/electricity')
def get_electricity_data():
    return jsonify(electricity_data.to_dict(orient='records'))

@app.route('/gas')
def get_gas_data():
    return jsonify(gas_data.to_dict(orient='records'))

@app.route('/water')
def get_water_data():
    return jsonify(water_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
