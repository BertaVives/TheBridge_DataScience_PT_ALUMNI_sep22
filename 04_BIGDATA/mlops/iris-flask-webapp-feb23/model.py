#######################
#--- Get Data ---#
#######################
'''
comentario largo o descripción de la operación a realizar

'''
# Importar librerías
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import joblib

# Importamos los datos
df = pd.read_csv("data/raw/iris.csv", header=None)
print(df.head(10))


#######################
#--- DataWrangling ---#
#######################

# Matriz de features 
X = df.iloc[:, :-1].values

# variable target
y = df.iloc[:, -1]
print("--- Paso X-y executed ---")

# Creamos la instancia de LabelEncoder
encoder = LabelEncoder()
y = encoder.fit_transform(y)
print("--- LabelEncoder executed ---")

joblib.dump(encoder, "saved_models/iris_label_encoder.pkl")


#######################
#---    Modeling   ---#
#######################

X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    test_size=0.3, 
                                                    random_state=17)

print("--- Train and Test executed ---")


# Train Model
classifier = KNeighborsClassifier(n_neighbors=4,
                                  metric='minkowski', p=2)
classifier.fit(X_train, y_train)
print("--- Training executed ---")

# Prediction
y_pred = classifier.predict(X_test)
print("--- Prediction executed ---")

# Scoring
accuracy = accuracy_score(y_true = y_test, y_pred = y_pred)
print(f"Accuracy Score: {round(accuracy*100,4)}")


# Serialización del modelo
joblib.dump(classifier, "saved_models/knn_iris.pkl")

#######################
#---    Testing   ---#
#######################

# classifier_loaded = joblib.load("saved_models/knn_iris.pkl")
# encoder_loaded = joblib.load("saved_models/iris_label_encoder.pkl")

# # Prediction en real-time
# X_manual_test = [[20.1, 20, 100, 100]]
# print("X_manual_test", X_manual_test)

# prediction_raw = classifier_loaded.predict(X_manual_test)
# print("Prediction_raw", prediction_raw)

# # Transformar - decoder de la clase
# prediction_real = encoder_loaded.inverse_transform(
#     classifier.predict(X_manual_test)
# )
# print("Prediction_real", prediction_real)