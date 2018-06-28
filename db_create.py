from application import db
from application.models import Juice

db.create_all()

print("DB created.")
