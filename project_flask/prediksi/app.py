import flask  
import numpy as np
import pickle 

app = flask.Flask(__name__, template_folder='templates')

random_forest = pickle.load(open('model/model_classifier.pkl','rb'))

@app.route('/')
def index():
    return(flask.render_template('main.html'))

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(val) for val in flask.request.form.values()]
    features = [np.array(int_features)]
    y_pred = random_forest.predict(features)
    hasil = {0:'Tidak ditempatkan', 1: 'Di tempatkan'}
    return flask.render_template('main.html',prediction_text=hasil[y_pred[0]])
    