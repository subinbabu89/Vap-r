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
    description = db.Column(db.String(255),index=True,unique=True)
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
        return '<Juice %i %r %i %r>' % (self.name,self.description,self.nicotine,self.type)