'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask, render_template, request, jsonify
from application import db
from application.models import Juice
from application.forms import JuiceDBInfo

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
        data_entered = Juice(juice_index=formjuice.dbJuiceIndex.data,juice_name=formjuice.dbJuiceName.data,nicotine=formjuice.dbJuiceNicotine.data,type=formjuice.dbJuiceType.data)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', juice=formjuice.dbJuiceName.data)

    return render_template('index.html', formjuice = formjuice)

@application.route('/juices', methods=['GET', 'POST'])
def fetchJuices():
    try:
        query_db = Juice.query.order_by(Juice.juice_index.desc())
        for q in query_db:
            print(q.notes)
        db.session.close()
    except:
        db.session.rollback()
    return render_template('results.html', results=query_db)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
