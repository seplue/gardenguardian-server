from server import db
from server.models import Measurement
from datetime import datetime


db.create_all()

m1 = Measurement(
    measurement_time=datetime.utcnow(),
    measurement_type="Pressure",
    measurement_value=966,
    bed_name="mybed",
    garden_name="mygarden"
)
db.session.add(m1)

m2 = Measurement(
    measurement_time=datetime.utcnow(),
    measurement_type="Humidity",
    measurement_value=56,
    bed_name="mybed",
    garden_name="mygarden"
)
db.session.add(m2)

m3 = Measurement(
    measurement_time=datetime.utcnow(),
    measurement_type="Dewpoint",
    measurement_value=966,
    bed_name="mybed",
    garden_name="mygarden"
)
db.session.add(m3)

m4 = Measurement(
    measurement_time=datetime.utcnow(),
    measurement_type="Temperature",
    measurement_value=24,
    bed_name="mybed",
    garden_name="mygarden"
)
db.session.add(m4)

db.session.commit()
