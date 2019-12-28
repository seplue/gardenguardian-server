from server import db
from datetime import datetime


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    measurement_time = db.Column(db.DateTime)
    measurement_type = db.Column(db.String(100))
    measurement_value = db.Column(db.Float)
    bed_name = db.Column(db.String(100))
    garden_name = db.Column(db.String(100))

    def __repr__(self):
        return "Measurement({} {} {} {} {} {})".format(
            self.id, self.measurement_time, self.measurement_type,
            self.measurement_value, self.bed_name, self.garden_name)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
           'id':                self.id,
           "measurement_time":  self.measurement_time,
           "measurement_type":  self.measurement_type,
           "measurement_value": self.measurement_value,
           "bed_name":          self.bed_name,
           "garden_name":       self.garden_name
        }
