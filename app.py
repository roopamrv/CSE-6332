from flask import Flask, render_template, request, redirect, url_for, session
import pyodbc
import re
import os
from werkzeug.utils import secure_filename
import blob_access

app = Flask(__name__)
app.config['UPLOAD_PATH'] = "uploads"
app.secret_key = 'your secret key'

server = 'mysqlserver-rv.database.windows.net'
username = 'azureuser'
password = 'Mavbgl@656'
database = 'demodb'
driver= '{ODBC Driver 18 for SQL Server}'
#Driver={ODBC Driver 18 for SQL Server};Server=tcp:mysqlserver-rv.database.windows.net,1433;Database=demodb;Uid=azureuser;Pwd={your_password_here};
conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+',1433;DATABASE='+database+';UID='+username+';PWD='+ password+ ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = conn.cursor()

@app.route('/')
@app.route('/people', methods=['GET', 'POST'])
def users():
    cursor.execute('SELECT * FROM people')
    people = cursor.fetchall()
    return render_template('people.html', people=people)

@app.route('/addrecord', methods=['GET', 'POST'])
def addrecord():
    msg=''
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        state = request.form['state']
        salary = request.form['salary']
        grade = request.form['grade']
        room = request.form['room']
        image = request.files['image']
        keywords = request.form['keywords']
        filename = filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        upload_status = blob_access.upload_blob(filename)
        print(upload_status)
        if upload_status[0] == 'Success':
            temp_filename = upload_status[1]
            print("TEMPPPPPP",temp_filename)
            picture_url = 'https://cse6332store.blob.core.windows.net/mycontainer' + temp_filename
        else:
            msg = 'Failed to upload file!!'
            return render_template('addrecord.html', msg=msg)
        sql = ('''
        SELECT * FROM people WHERE phone=?
        ''')
        cursor.execute(sql, (phone))
        account = cursor.fetchone()
        if account:
            msg = 'Person already exists'
        elif not name or not phone or not state or not salary or not grade or not room or not keywords:
            msg = 'Please fill all details'
        else:
            cursor.execute('''INSERT INTO people (name,state,phone,salary,grade,room,picture_url,keywords) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
                         , (name, state, phone, salary, grade, room, picture_url, keywords))
            cursor.commit()
            msg = 'You have successfully added !'
            return render_template('addrecord.html', msg=msg)
    # elif request.method == 'POST':
    #     msg = 'Please fill out the form !'
    return render_template('addrecord.html', msg=msg)

@app.route('/updaterecord/<id>', methods=['GET', 'POST'])
def updaterecord(id):
    msg=''
    cursor.execute('''SELECT * FROM people where id=?''', (id))
    record = cursor.fetchone()
    return render_template('updaterecord.html', person=record)

@app.route('/rupdate', methods=['GET', 'POST'])
def rupdate():
    msg='Failed to update'
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        state = request.form['state']
        salary = request.form['salary']
        grade = request.form['grade']
        room = request.form['room']
        keywords = request.form['keywords']
        if request.files['image']:
            print('IN')
            image = request.files['image']
            filename = filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            upload_status = blob_access.upload_blob(filename)
            print(upload_status)
            if upload_status[0] == 'Success':
                temp_filename = upload_status[1]
                picture_url = 'https://cse6332store.blob.core.windows.net/mycontainer/' + temp_filename
                cursor.execute('''UPDATE people SET picture_url=? WHERE id=?''',(picture_url, id))

        cursor.execute("UPDATE people SET name='{}', state='{}', phone='{}', keywords='{}', salary='{}', grade='{}', room='{}' "
                     "where id={}".format(name,state, phone, keywords, salary, grade, room, id))
        cursor.commit()
        msg = 'Record successfully updated !'
        return redirect('/')
    return render_template('updaterecord.html', msg=msg)


@app.route('/deleterecord/<id>', methods=['GET', 'POST'])
def deleterecord(id):
    msg=''
    cursor.execute("DELETE FROM people where id={}".format(id))
    cursor.commit()
    msg = 'Record successfully deleted !'
    return redirect('/')


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=6601, threaded=True,debug=True)