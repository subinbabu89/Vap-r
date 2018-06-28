from application import db

class Juice(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    juice_index = db.Column(db.Integer,index=True,unique=True)
    juice_name = db.Column(db.String(255),index=True,unique=True)
    nicotine = db.Column(db.Integer)
    type = db.Column(db.String(255),index=True,unique=False)

    def __init__(self,juice_index,juice_name,nicotine,type):
        self.juice_index = juice_index
        self.juice_name = juice_name
        self.nicotine = nicotine
        self.type = type

    def __repr__(self):
        return '<Juice %i %r %i %r>' % (self.juice_index,self.juice_name,self.nicotine,self.type)