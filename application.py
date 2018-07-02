'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask, render_template, request, jsonify, Response
from application import db
from application.models import Juice,Flavor,Job
from application.forms import JuiceDBInfo

import simplejson
from sqlobject import *


# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'   


# Root / Home page
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

# View flavors page
@application.route('/flavors', methods=['GET', 'POST'])
def fetchFlavors():
    try:
        query_db = Flavor.query.order_by(Flavor.flavor_index.desc())
        for q in query_db:
            print(q.flavor_name)
        db.session.close()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message
        db.session.rollback()
    return render_template('results_flavors.html', results=query_db)

# View Juices page
@application.route('/juices', methods=['GET', 'POST'])
def fetchJuices():
    try:
        query_db = Juice.query.order_by(Juice.id.desc())
        for q in query_db:
            print(q.name)
        db.session.close()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message
        db.session.rollback()
    return render_template('results_juices.html', results=query_db)

# Fetch Flavor API
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

# Fetch Juice API
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

# Insert Juice API
@application.route('/putJuice', methods = ['POST'])
def insertJuice():
    juice = request.json
    data_entered = Juice(juice['juices'],juice['description'],juice['rating'],juice['pgvg_rating'],juice['flavors'],juice['nicotine'],juice['ingredients'])
    try:
        db.session.add(data_entered)
        db.session.commit()
        db.session.close()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message
        db.session.rollback()
        errorresponse={
            'type':type(ex).__name__,
            'args':ex.args
        }
        resp = Response(simplejson.dumps(errorresponse), status=200, mimetype='application/json')
        return resp
    return "Success"

# Fetch Jobs API
@application.route('/jobjson',methods=['GET','POST'])
def fetchJobJson():
    try:
        query_db = Job.query.order_by(Job.id.desc())
        jobs_as_dict =[]

        for q in query_db:
            job_as_dict = {
                'job_name' : q.job_name,
                'started_by' : q.started_by,
                'time_to_complete' : q.time_to_complete
            }
            jobs_as_dict.append(job_as_dict)
        db.session.close()
    except:
        db.session.rollback()
    resp = Response(simplejson.dumps(jobs_as_dict),status=200,mimetype='application/json')
    return resp

# Insert Job API
@application.route('/putJob', methods = ['POST'])
def insertJob():
    job = request.json
    data_entered = Job(job['job_name'],job['started_by'],job['time_to_complete'])
    try:
        db.session.add(data_entered)
        db.session.commit()
        db.session.close()
    except:
        db.session.rollback()
    return "Success"

# Bulk import juice API
@application.route('/bulkputJuice', methods = ['POST'])
def insertBulkJuice():
    juices = request.json
    try:
        for juice in juices:
            print juice
            data_entered = Juice(juice['juices'],juice['description'],juice['rating'],juice['pgvg_rating'],juice['flavors'],juice['nicotine'],juice['ingredients'])
            db.session.add(data_entered)
            db.session.commit()
        print "SUCCESSFUL INSERT"
        db.session.close()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message
        db.session.rollback()
    return "Success"

    
if __name__ == '__main__':
    application.run(host='0.0.0.0')
