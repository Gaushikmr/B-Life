#!/usr/bin/python3
# from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, session
from flask_session.__init__ import Session
# from flask.ext.session import Session

SESSION_TYPE = 'memcache'


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
sess = Session()


@app.route('/')
def index():
    return render_template("index.html")

# def donation():
   

#       return render_template("donation.html")

@app.route('/index', methods=['GET','POST'])
def mainPage():
    return render_template('index.html')


# @app.route('/index', methods=['POST'])
# def mainPageButton():
    
#     return render_template('index.html', **templateData)

@app.route('/donation', methods=['GET'])
def do_admin():
    return render_template('donation.html')


@app.route('/donation', methods=['POST'])
def do_admin_login():
#     name =""
#     Dob=""
#     email=""
#     mob=""
#     occupation=""
#     id_type=""
#     id_num=""
#     authority=""
#     state=""
#     issued=""
#     expiry=""
#     address=""
#     nationality=""
#     st=""
#     district=""
#     block=""
#     ward=""
#     father=""
#     mother=""
#     grand=""
#     spouse=""
#     fatherinlaw=""
#     motherinlaw=""
#     height=""
#     weight=""
#     if request.method == "POST":
    name =  request.form['name']
    print(name)
    Dob = request.form['Dob']
    print(Dob)
    flash('Data Captured')
    return do_admin()
    
    
    
#         email = request.form['email']
#         mob = request.form['mob']
#         occupation = request.form['occupation']
#         id_type= request.form['id_type']
#         id_num= request.form['id_num']
#         authority= request.form['authority']
#         state= request.form['state']
#         issued= request.form['issued']
#         expiry= request.form['expiry']
#         address= request.form['address']
#         nationality= request.form['nationality']
#         st= request.form['st']
#         district= request.form['district']
#         block= request.form['block']
#         ward= request.form['ward']
#         father= request.form['father']
#         mother= request.form['mother']
#         grand= request.form['grand']
#         spouse= request.form['spouse']
#         fatherinlaw= request.form['fatherinlaw']
#         motherinlaw= request.form['motherinlaw']
#         height= request.form['height']
#         weight= request.form['weight']
    


  


if __name__ == "__main__":
#     app.run(host="0.0.0.0",port=5000,debug=1)
#     app.secret_key = os.urandom(12)
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    app.debug = True
    app.run(host="0.0.0.0",port=1000)
