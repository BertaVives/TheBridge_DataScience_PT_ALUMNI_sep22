from flask import Flask, request, jsonify, session, url_for, redirect, render_template
import joblib
import os

# importar el formulario custom
from flower_form import FlowerForm

# Importar los ficheros serializados
classifier_loaded = joblib.load("saved_models/knn_iris.pkl")
encoder_loaded = joblib.load("saved_models/iris_label_encoder.pkl")

# Creamos la función de prediccion
def make_prediction(model, encoder, sample_json):

    # recoger los valores del formulario
    SepalLengthCm = sample_json['SepalLengthCm']
    SepalWidthCm = sample_json['SepalWidthCm']
    PetalLengthCm = sample_json['PetalLengthCm']
    PetalWidthCm = sample_json['PetalWidthCm']

    # Creamos un vector de input
    flower = [[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]]

    # Realizamos la prediccion
    prediction_raw = model.predict(flower)

    # Convertimos los valores raw en clase
    prediction_real = encoder.inverse_transform(prediction_raw)

    return prediction_real[0]

# Definición de la Web App 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Definimos la plantilla de homepage /
@app.route("/", methods=['GET','POST'])

# Creamos el formulario
def index():
    # estructuramos el formulario
    form = FlowerForm()

    if form.validate_on_submit():
        session['SepalLengthCm'] = form.SepalLengthCm.data
        session['SepalWidthCm'] = form.SepalWidthCm.data
        session['PetalLengthCm'] = form.PetalLengthCm.data
        session['PetalWidthCm'] = form.PetalWidthCm.data

        return redirect(url_for('prediction'))
    return render_template('home.html', form=form)

# Creamos la plantilla de la página prediction
@app.route('/prediction')
def prediction():
    content = {'SepalLengthCm': float(session['SepalLengthCm']), 'SepalWidthCm': float(session['SepalWidthCm']),
               'PetalLengthCm': float(session['PetalLengthCm']), 'PetalWidthCm': float(session['PetalWidthCm'])}

    results = make_prediction(classifier_loaded, encoder_loaded, content)

    return render_template('prediction.html', results=results)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    # app.run(host='127.0.0.1', port=8080)
    # app.run()
