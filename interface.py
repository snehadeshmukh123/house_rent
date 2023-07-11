from flask import Flask,request,render_template,jsonify
from utils import HouseRent
import config

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('house_rent.html')



@app.route('/predict_charges',methods =['GET','POST'])
def predict_charges():

    if request.method == 'GET':

        data = request.args.get
        print('Data:',data)
        area = data('area')
        
        obj = HouseRent(area)
        pred_price = obj.get_predicted_price()

        #return jsonify({'Result':f'predicted rent charges {pred_price}'})
        return render_template('house_rent.html',prediction = pred_price)


    elif request.method == 'POST':

        data = request.form
        print('Data:',data)
        area = data['area']
        
        obj = HouseRent(area)
        pred_price = obj.get_predicted_price()

        return jsonify({'Result':f'predicted rent charges {pred_price}'})
        #return render_template('house_rent.html',prediction = pred_price)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = config.PORT_NUMBER)
