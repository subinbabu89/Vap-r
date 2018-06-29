from application import db
from application.models import Juice,Flavor,Job
# from application.models import Job
# from application.models import Juice
# from application.models import Flavor

db.create_all()

print("DB created.")
