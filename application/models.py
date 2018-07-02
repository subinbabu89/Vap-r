from application import db

class Flavor(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    flavor_index = db.Column(db.Integer,index=True,unique=True)
    flavor_name = db.Column(db.String(255),index=True,unique=True)
    nicotine = db.Column(db.Integer)
    type = db.Column(db.String(255),index=True,unique=False)

    def __init__(self,flavor_index,flavor_name,nicotine,type):
        self.flavor_index = flavor_index
        self.flavor_name = flavor_name
        self.nicotine = nicotine
        self.type = type

    def __repr__(self):
        return '<Flavor %i %r %i %r>' % (self.flavor_index,self.flavor_name,self.nicotine,self.type)

class Juice(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),index=True,unique=True)
    description = db.Column(db.String(255),index=True)
    rating = db.Column(db.String(255),index=True)
    pgvg_rating = db.Column(db.String(255),index=True)
    type = db.Column(db.String(255),index=True)
    nicotine = db.Column(db.String(255),index=True)
    ingredients = db.Column(db.String(255),index=True)

    def __init__(self,name,description,rating,pgvg_rating,type,nicotine,ingredients):
        self.name = name
        self.description = description
        self.rating = rating
        self.pgvg_rating = pgvg_rating
        self.type = type
        self.nicotine = nicotine
        self.ingredients = ingredients

    def __repr__(self):
        return '<Juice %r %r %r %r>' % (self.name,self.description,self.nicotine,self.type)

class Job(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    job_name = db.Column(db.String(255),index=True,unique=True)
    started_by = db.Column(db.String(255),index=True,unique=True)
    time_to_complete = db.Column(db.Integer)

    def __init__(self,job_name,started_by,time_to_complete):
        self.job_name = job_name
        self.started_by = started_by
        self.time_to_complete = time_to_complete

    def __repr__(self):
        return '<Job %r %r %i>' % (self.job_name,self.started_by,self.time_to_complete)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index=True,unique=True)
    fname = db.Column(db.String(255),index=True)
    lname = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),index=True,unique=True)
    password = db.Column(db.String(255),index=True)

    def __init__(self,username,fname,lname,email,password):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r %r %r>' % (self.username,self.email,self.fname)