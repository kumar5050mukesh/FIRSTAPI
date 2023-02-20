from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def result():
    if(request.method=='POST'):
        fat = request.form['option']
        dat = request.form['num']

        if fat == 'square':
            result = int(dat) ** 2
        elif fat == 'cube':
            result = int(dat) ** 3
    

    return  render_template('result.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)
