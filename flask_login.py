from flask import Flask,render_template,request,redirect,url_for


import  psycopg2


app=Flask(__name__)
try:
    connection=psycopg2.connect('dbname=mydatabase user=postgres password=srinu host=localhost port=5432 ')

    cur=connection.cursor()

    print connection
except Exception as e:
    print  e

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
       return render_template("main.html")



@app.route('/singup',methods=['GET','POST'])
def signup():
    if request.method=='GET':

        return render_template('signup.html')
    elif request.method=='POST':
        name=str(request.form['name'])
        password=str(request.form['password'])
        cur.execute("SELECT name FROM loginpage;")
        register=cur.fetchall()
        for rname in register:
            if rname==name:
                return "<h1> Username Already Exist</h1>"
        else:
            cur.execute("INSERT INTO loginpage VALUES(%s, %s);" ,(name, password))
            connection.commit()

            return render_template('registersuccess.html',name=name)
    else:
        return "<h1> Invalid Access</h1>"



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':

        return render_template('login.html')
    elif request.method == 'POST':
        fname = str(request.form['name'])
        fpassword = str(request.form['password'])
        print(fname,fpassword)
        cur.execute("SELECT name , password FROM loginpage ;")
        results=cur.fetchall()
        for result in results:
            if (fname,fpassword)==result:
                return render_template('correct.html',name=fname)
        else:
            return render_template('incorrect.html')
    else:
        return "<h1> Invalid Access</h1>"




if __name__ == '__main__':
    app.run(debug=True)



