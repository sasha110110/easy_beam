from mail_imap_test import check_email
from flask import Flask,render_template,request,redirect,url_for,flash, session
#import sqlite3 as sql
import os
from random import randint
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,EqualTo, ValidationError#Email
from werkzeug.utils import secure_filename

##from flask_dropzone import Dropzone
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message, Mail
from time import time
import jwt
import json
from sqlalchemy.exc import IntegrityError
from itsdangerous import BadSignature, SignatureExpired
from flask import g, request
####from flask.ext.admin import Admin
###from flask.ext.admin.contrib.sqlamodel import ModelView

passw=os.environ.get("passw")
print(passw)


app = Flask(__name__, static_folder="./static")
app.config['SECRET_KEY'] = os.environ.get("flask_secret")

#UPLOAD_FOLDER=r'C:\Users\Sasha\Desktop\M\receipts'
#dropzone = Dropzone(app)
MAIL_USERNAME="beamtestit@gmail.com"
MAIL_PASSWORD="gnlfrctoacfybudd"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'#'mysql://root:''@localhost/mydb'#'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "beamtestit@gmail.com" ####HIDE THEN
app.config['MAIL_PASSWORD'] = "gnlfrctoacfybudd" # "easybeam8" ### HIDE THEN
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['SECURITY_PASSWORD_SALT'] = 'my_secret'

mail = Mail(app)



global data
#global email
#global account_amont



@app.route('/')
def index():
    session["operation_id"]=""

    email=None
    account_amount=0
    if "email" in session.keys():
        email=session["email"]
        account_amount=session.get("account_amount", 0)
    
    if request.method=="POST" and "SupportInputSubmit" in request.form:
        print(account_amount)
        if account_amount==0:
            flash("Your generosity will return to you!")
            print("ACCOUNT_AMOUNT", account_amount)
            return redirect(rl_for("prepare_to_pay"))
             
        
    
    
##    if request.method=="POST" and request.form["submit"]=="?????????????????? ?????? ????????????":
##    #if request.method=="POST" and "??????????????????" in request.form:
##        print(reqest.forms)
##        res=request.forms #jsonify(request.form)

             #reqest.args.get
 
    return render_template('index.html', email=email,
                           account_amount=account_amount)
 

 
@app.route('/temp/' , methods = ['GET', 'POST'])
def prepare_to_pay():
    
    #TO DO - CHECK SESSION
    #operational_id=None
    operation_id=441361714955017004#randint(100, 678899)
    print(operation_id)
    session["operation_id"]=operation_id
          
    if request.method=="POST":
        #operational_id=randint(100, 678899)
        #print("OPERATIONAL OS", operational_id)
        return redirect(url_for("check_payment"))    
                
    return render_template("temp.html", operational_id=operation_id)


@app.route('/webhook' , methods = ['POST', 'GET'])
def check_payment_webhook():
 
    if request.method == 'POST':
        
        data = b64decode(request.data)
        
        if not data:
            data = b64decode(list(request.form.keys())[0])
        special_mimetype = request.mimetype
        return(special_mimetype + '\n' + data)
    return str(data)
    
        

@app.route('/webhook2')
def webhook2():
    info=list(request.form.keys())
    payment_info=json.dumps(info)
    #payment_info=session.get("payment_info", "")
    
  
    
    return render_template("webhook2.html", payment_info=payment_info)

        
 
   


@app.route('/check_payment', methods = ['GET', 'POST'])  
def check_payment():
    print(session.keys())
    account_amount=0
    session["account_amount"]=0
    email=""
   
    if request.method=="POST":
        if "emailsubmit" in request.form:
            flash("?????????? ?????? ???????? ???????????? ?????????????? ?????????????????? ")
                
            email=request.form.get("emailinput")
            print("EMAIL", email)
            

            session["email"]=email
         
    got_operation_id, amount=check_email() ###########################################    email check
    #if "payment_info" in session.keys():
        #payment_info=session["payment_info"]
    print("GOT", got_operation_id, amount)
        #TO DO operation id, email check with given email
    if session["operation_id"]==got_operation_id:
        session["account_amount"]+=amount
            
                
        print(session["account_amount"])
        

    return render_template("payment_processing.html", email=email,
                           account_amount=session["account_amount"])
    


##@app.route('/get_payment_info', methods = ['POST','GET'])
##def get_payment_info():
##
##     headers = {
##            'Authorization': 'Bearer ' + str(access_token),
##            'Content-Type': 'application/x-www-form-urlencoded'
##        }
##    request.headers=headers
##    #response = requests.request("POST", url, headers=headers)
##    if request.method == 'POST':
##        responce=requestjson
##        
##      
##    if "notification_type = card-incoming" in response:
##        amoumt=responce["amount"]
##        user=UserShort.filter_by(email=session["email"])
##        user.account_amount=amoumt
##        db.session.commit()
    




@app.route('/view_all_inputs')  
def view_all_inputs():
    data=""
    
    data = request.args.get('passed_data')
    print(data)
    
    return render_template("view_all.html", all_data=data)


@app.route('/send_email_with_data' , methods = ['GET', 'POST'])
def send_email_with_data(user_email):
    if not "email" in session.keys():
        flash("??????????????, ????????????????????, ??????????")
        
    
    msg = Message(
        'EASYBEAM - ?????????????? ???????????? ??????????????',
        sender=("Admin", "beamtestit@gmail.com"),
        recipients=[user_email]
    )
    msg.html=html
    mail.send(msg)








@app.route('/thankyou', methods = ['POST','GET'])
def thank():
  return render_template("thankyou.html")



      
     
      ##return redirect(url_for('download_file', name=filename))
      #with open(os.path.join(app.config['UPLOAD_FOLDER'], receipt)) as f:
          #return f.read()

      



#if __name__ == '__main__':
   # app.run('0.0.0.0', 5000,  debug = True) #ssl_context='adhoc')
