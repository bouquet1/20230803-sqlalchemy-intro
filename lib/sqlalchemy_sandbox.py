#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Index, String, create_engine, desc, asc, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# 1. ✅ Develop a student schema: name, email, grade, birthday(year,month,day). part that line starts with id = Column()...
# 2. ✅ Create a new student record and add it to the database. Asagidakini yazarak yaotik.
#   thompson_plyler = Student(
#       name = "Thompson Plyler	", 
#       email = "thompson.plyler@flatironschool.com", 
#       grade = 9, 
#       birthday = datetime(
#           year = 1981, 
#           month = 02,    
#           day = 18
#       )
#   )  
# Tom Tobar ve Alan Turingi de ayni sekilde yazdik.

# 3. ✅ Query all students. 
# 4. ✅ Query all students by name.
# 5. ✅ Query all students by name, and order by name. 
# 6. ✅ Query all students by name, order by name, descending.
# 7. ✅ Limit student query to 1 result
# 8. ✅ Use the SQLAlchemy func.count function to report how many student entries exist.
# 9. ✅ Filter student query results by name
# 10. ✅ Update the student data for a single column. 
# 11. ✅ Delete a student database entry/row. 

class Student(Base):
    __tablename__ = 'students'
    Index('index_name', 'name')

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())
    
    def __repr__(self):
        return f"\n Student {self.id}: "\
            + f"{self.name} "\
            + f"Grade: {self.grade}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


query = session.query(Student).filter(Student.name.like("%Albert%"))
albert_einstein = query.first()

session.delete(albert_einstein)
session.commit()

albert_einstein = query.first()
print("Hopefully is None: ", albert_einstein)

# Extra nites from lecture 
    # Index func helping us speed up the searhc. what is your expect to be use a query parameter it is name in this case.
    # email (55) restricting the length of the email to 55
    # def __repr__ (self) comes with every single python class. f""" string interpolation. repr[/reapir/] do: affects when we print this value we gonna get more useful info rather than just print something. useful tool we can trust it is for python not sql specific thing.
    # place it to db, declare an engine, make a session with sessionmaker. Engine is the python obj sits directly on IF with directly with DB.  the thing typing python commands sending them to DB and then retrieving the info is the ENGINE. we pass the engine into a sessionmaker. engine talking directly to DB session we'll pas in that session in.  import sessionmaker don't forget. "from sqlalchemy.orm import sessionmaker"  
    #   engine = create_engine('sqlite:///students.db') => comes from import create_engine. it'll interact with students.db and if it doesn;t exist it will create students.db
    #   Base.metadata.create_all(engine)
    #   Session = sessionmaker(bind=engine) => with sessionmaker() method, we get a func back Session() by declarion a Session. the 'sessionmaker(bind=engine)' here is what's called a factory.
    #   session = Session() => we're calling/invoking Session() we use the session class and create a session object that is instance of a session class. 