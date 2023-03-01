from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class FlowerForm(FlaskForm):
    # input text
    SepalLengthCm = StringField('Sepal Length Cm')
    SepalWidthCm = StringField('Sepal Width Cm')
    PetalLengthCm = StringField('Petal Length Cm')
    PetalWidthCm = StringField('Petal Width Cm')

    # submit boton que llama la función make_prediction
    submit = SubmitField("Predict")