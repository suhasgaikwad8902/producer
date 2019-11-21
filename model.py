from producer_consumer.producer.appconfig import app,db
class Employee(db.Model):
    __tablename__= "Employee"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float(), nullable=False)
    is_active = db.Column(db.String(10),default="Y")

#import os
#os.system(exit(0))
if __name__=="__main__":
    e1 = Employee(name="chunky",city="Pune", salary=2000)
    db.session.add(e1)
    db.session.commit()
    print("ggg")
