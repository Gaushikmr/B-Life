#!/usr/bin/python3
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template("index.html")

# def donation():
   

#       return render_template("donation.html")

@app.route('/index')
def mainPage():
    return render_template('index.html', **templateData)

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
    name =  request.form['name']
    print(name)
    Dob = request.form['Dob']
    print(Dob)
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


@app.route('/register',methods=['POST'])
def do_register():
    return render_template('donation.html')

@app.route('/postRegister',methods=['POST'])
def save_register():
    username = request.form['username'] 
    password = request.form['password']
    confirmpassword = request.form['confirmpassword']

   


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=1)
#     app.secret_key = os.urandom(12)
    
    



# @app.route('/AARTestrev', methods=['POST'])
# def AARTestrev():
# 	try:
# 		GPIO.setup(17,GPIO.HIGH)
# 		time.sleep(10)#FWD
# 		GPIO.setup(17,GPIO.LOW)
# 		flash ('AAR Test Completed')
# 	except:
# 		flash("Error Testing")
# 	return redirect(url_for('mainPage'))

# @app.route('/update', methods=['POST'])
# def update():
#     try:
#         path='/home/pi/OceanNet/AAR/ConfigPage/'
#         os.chdir(path)
#         cmd="git pull"
#         os.system(cmd)
#         flash ('Update Completed')
#     except:
#         flash("Error Software Updation")
#     return redirect(url_for('mainPage'))

# @app.route('/reboot', methods=['POST'])
# def reboot():
    
#     cmd="reboot"
#     os.system(cmd)
    
#     return redirect(url_for('mainPage'))

# @app.route('/LEDTest1', methods=['POST'])#status
# def LEDTest1():
#     try:
#         cmd="/home/pi/OceanNet/AAR/ConfigPage/LEDtest.py"
#         os.system(cmd)
#         flash ('LED Test Completed')
#     except:
#         flash("Error Testing Notification LED")
#     return redirect(url_for('mainPage'))

# # app.route('/LEDTest2', methods=['POST'])#rssi1
# # def LEDTest2():
# # 	try:
# # 		GPIO.setup(19,GPIO.HIGH)
# # 		time.sleep(2)#FWD
# # 		GPIO.setup(19,GPIO.LOW)
# # 		flash ('RSSI1 Test Completed')
# # 	except:
# # 		flash("Error Testing Notification LED")
# # 	return redirect(url_for('mainPage'))
# # @app.route('/LEDTest3', methods=['POST'])#rssi2
# # def LEDTest3():
# # 	try:
# # 		GPIO.setup(13,GPIO.HIGH)
# # 		time.sleep(2)#FWD
# # 		GPIO.setup(13,GPIO.LOW)
# # 		flash ('RSSI2 Test Completed')
# # 	except:
# # 		flash("Error Testing Notification LED")
# # 	return redirect(url_for('mainPage'))
# # @app.route('/LEDTest4', methods=['POST'])#rssi3
# # def LEDTest4():
# # 	try:
# # 		GPIO.setup(6,GPIO.HIGH)
# # 		time.sleep(2)#FWD
# # 		GPIO.setup(6,GPIO.LOW)
# # 		flash ('RSSI3 Test Completed')
# # 	except:
# # 		flash("Error Testing Notification LED")
# # 	return redirect(url_for('mainPage'))
# # @app.route('/LEDTest5', methods=['POST'])#rssi4
# # def LEDTest5():
# # # 	try:
# # 	GPIO.setup(5,GPIO.HIGH)
# # 	time.sleep(2)#FWD
# # 	GPIO.setup(5,GPIO.LOW)
# # 	flash ('RSSI1 Test Completed')
# # 	except:
# # 		flash("Error Testing Notification LED")
#     return redirect(url_for('mainPage'))
# app.run(debug=False,host="0.0.0.0",port="1000", threaded=True)
