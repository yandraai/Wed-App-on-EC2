from flask import Flask, render_template, request

def def_factors(number):
    number = int(number)
    return [x for x in range(1, number+1) if number%x==0]

app = Flask(__name__)
app.secret_key = 'thisisunbreakable'

@app.route('/',methods=['GET','POST'])
def index():

    return render_template('my-form.html')


@app.route('/factors',methods=['GET','POST'])
def factors_dis():
    n=request.form['Number']
    return render_template('factors.html',number=n,factors=def_factors(n))



if __name__ =="__main__":
    app.run(debug=True)
