from flask.ext.wtf import Form
from wtforms import TextField, validators

class JuiceDBInfo(Form):
    dbJuiceIndex = TextField(label='Index for the Juice', description="db_enter", validators=[validators.required(), validators.Regexp('^\d{1}$',message=u'Enter a number between 1 and 10')])
    dbJuiceName = TextField(label='Name for the juice', description="db_enter", validators=[validators.required(), validators.Length(min=0, max=255, message=u'Enter 128 characters or less')])
    dbJuiceNicotine = TextField(label='Nicotine Level of the juice', description="db_enter", validators=[validators.required(), validators.Regexp('^\d{1}$',message=u'Enter a number between 1 and 10')])
    dbJuiceType = TextField(label='Type of the juice', description="db_enter", validators=[validators.required(), validators.Length(min=0, max=255, message=u'Enter 128 characters or less')])

class RetrieveDBInfo(Form):
    numRetrieve = TextField(label='Number of DB Items to Get', description="db_get", validators=[validators.required(), validators.Regexp('^\d{1}$',message=u'Enter a number between 1 and 10')])
