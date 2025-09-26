from flask import Flask, request, render_template

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)

# set 'app' to the WSGI callable name gunicorn/EB expects
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    # use uppercase HTTP method names
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Only pick allowed input keys; ignore unexpected ones like 'charges'
        allowed_keys = {'age', 'sex', 'bmi', 'children', 'smoker', 'region'}
        form_data = {k: request.form.get(k) for k in allowed_keys}

        data = CustomData(**form_data)

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])


if __name__ == "__main__":
    app.run(debug=True)


