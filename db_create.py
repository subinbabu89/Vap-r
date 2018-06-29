from application import db
from application.models import Juice,Flavor

db.create_all()

print("DB created.")
