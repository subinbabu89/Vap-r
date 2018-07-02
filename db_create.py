from application import db
from application.models import Juice,Flavor,Job,User
# from application.models import Job
# from application.models import Juice
# from application.models import Flavor
# from application.models import User

db.create_all()

print("DB created.")
