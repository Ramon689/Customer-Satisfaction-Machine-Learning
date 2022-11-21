from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
app = Flask(__name__)
filename = 'customer_sat.pkl'
model = pickle.load(open(filename, 'rb'))
model = joblib.load(filename) 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])  # The user input is processed here
def predict():
    Gender = request.form['Gender']
    Customer_Type = request.form['Customer_Type']
    Age = request.form['Age']
    Type_of_Travel = request.form['Type_of_Travel']
    Class = request.form['Class']
    Ease_of_Online_booking = request.form['Ease_of_Online_booking']
    Food_and_drink = request.form['Food_and_drink']
    Seat_comfort = request.form['Seat_comfort']
    Inflight_entertainment = request.form['Inflight_entertainment']
    Onboard_service = request.form['On-board_service']
    Checkin_service = request.form['Checkin_service']
    Inflight_service = request.form['Inflight_service']
    Cleanliness = request.form['Cleanliness']
    Departure_Delay_in_Minutes = request.form['Departure_Delay_in_Minutes']
    Arrival_Delay_in_Minutes = request.form['Arrival_Delay_in_Minutes']
    pred = model.predict(np.array([[Gender, Customer_Type, Age, Type_of_Travel, Class, Ease_of_Online_booking, Food_and_drink, Seat_comfort, Inflight_entertainment, On_board_service, Checkin_service, Inflight_service, Cleanliness, Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes]]))
    #print(pred)
    return render_template('index.html', predict=str(pred))
if __name__ == '__main__':
    # app.run(debug=True)
 app.run(host='0.0.0.0', port= 8080)