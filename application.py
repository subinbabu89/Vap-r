'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask, render_template, request, jsonify, Response
from application import db
from application.models import Juice,Flavor
from application.forms import JuiceDBInfo

import simplejson
from sqlobject import *


# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'   

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    formjuice = JuiceDBInfo(request.form)

    if request.method == 'POST' and formjuice.validate():
        data_entered = Flavor(flavor_index=formjuice.dbJuiceIndex.data,flavor_name=formjuice.dbJuiceName.data,nicotine=formjuice.dbJuiceNicotine.data,type=formjuice.dbJuiceType.data)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', juice=formjuice.dbJuiceName.data)

    return render_template('index.html', formjuice = formjuice)

@application.route('/flavors', methods=['GET', 'POST'])
def fetchFlavors():
    try:
        query_db = Juice.query.order_by(Juice.juice_index.desc())
        for q in query_db:
            print(q.notes)
        db.session.close()
    except:
        db.session.rollback()
    return render_template('results.html', results=query_db)

@application.route('/flavorjson',methods=['GET','POST'])
def fetchFlavorJson():

    try:
        query_db = Flavor.query.order_by(Flavor.flavor_index.desc())
        flavors_as_dict = []

        for q in query_db:
            flavor_as_dict = {
                'id':q.id,
                'juice_index':q.flavor_index,
                'juice_name':q.flavor_name,
                'nicotine':q.nicotine,
                'type':q.type
            }
            flavors_as_dict.append(flavor_as_dict)
        db.session.close()
    except:
        db.session.rollback()
    resp = Response(simplejson.dumps(flavors_as_dict),status=200,mimetype='application/json')
    return resp

@application.route('/juicejson',methods=['GET','POST'])
def fetchJuiceJson():
    try:
        query_db = Juice.query.order_by(Juice.id.desc())
        juices_as_dict =[]

        for q in query_db:
            juice_as_dict = {
                'id' : q.id,
                'name' : q.name,
                'description' : q.description,
                'rating' : q.rating,
                'pgvg_rating' : q.pgvg_rating,
                'type' : q.type,
                'nicotine' : q.nicotine,
                'ingredients' : q.ingredients
            }
            juices_as_dict.append(juice_as_dict)
        db.session.close()
    except:
        db.session.rollback()
    resp = Response(simplejson.dumps(juices_as_dict),status=200,mimetype='application/json')
    return resp

@application.route('/putJuice', methods = ['POST'])
def insertJuice():
    juice = request.json
    data_entered = Juice(juice['name'],juice['description'],juice['rating'],juice['pgvg_rating'],juice['type'],juice['nicotine'],juice['ingredients'])
    try:
        db.session.add(data_entered)
        db.session.commit()
        db.session.close()
    except:
        db.session.rollback()
    return "Success"

    
if __name__ == '__main__':
    application.run(host='0.0.0.0')
