from flask import Flask, request, render_template
import pandas as pd
import base64
from io import BytesIO
import utils

from matplotlib.figure import Figure

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world'

# cols = ['pcclass' , 'age' ,'sex']
# df[cols]

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        df.dropna(how='any', axis=0, inplace=True)
        table = df.to_html(index=False)
        return render_template('upload.html', 
                            shape = df.shape,
                            table = table)
    return render_template('upload.html')

@app.route("/data_analysis")
def hello():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

if __name__ == '__main__':
    app.run(debug = True)