from flask import Flask, jsonify, send_file
import pandas as pd

app = Flask(__name__)

# Simulated data (replace with actual data loading logic)
electricity_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar','Avr','Mai','Juin','Juil','Aout','Sept','Oct','NoV','Dec'],'Consumption': [127000,124000,123000,122000,169000,229000,224000,225000,226000,187000,125000,129000]})
gas_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar','Avr','Mai','Juin','Juil','Aout','Sept','Oct','NoV','Dec'],'Consumption': [483470,482500,483400,445000,425000,317000,315000,314000,370000,475000,485000,480000]})
water_data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar','Avr','Mai','Juin','Juil','Aout','Sept','Oct','NoV','Dec'],'Consumption': [75,75,77,78,77,80,82,85,82,81,86,75]})

# Define unit costs
unit_cost = {'electricity': 0.27, 'gas': 0.0913, 'water': 4.34}

@app.route("/",methods=['GET'])
def get_default():
    return jsonify({'result': "App Running..."})

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