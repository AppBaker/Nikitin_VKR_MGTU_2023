from flask import Flask, render_template, request
import tensorflow as tf
import requests

app = Flask(__name__)

def mn_predict(params):
    model = tf.keras.models.load_model('static/ml_models/model_mn')
    pred = model.predict([params])
    return pred

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        X_data = []
        parametrs = ("plot", "mupr", "hard_amount", 
                    "smola", "temp", "pov_plot", 
                    "mod_up_rast", "proch_rast",
                    "potr_smol", "corner", "step", 
                    "plotn_nashivki")
        for param in parametrs:
            try:
                cust_num = float(request.form.get(param).replace(',', '.'))
            except:
                return render_template("index.html", text='Введены некорректные данные')
            X_data.append(cust_num)
        result = str(round(mn_predict(X_data)[0][0], 3))
        return render_template("index.html", text=f'Расчетное соотношение матрица-наполнитель = {result}', params=X_data)
    else:
        return render_template("index.html", text="Введите параметры материала для расчета соотношения матрица-наполнитель")



if __name__ == "__main__":
    app.run(debug=False)