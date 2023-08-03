#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Index, String, create_engine, desc, asc, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# 1. ✅ Develop a student schema: name, email, grade, birthday(year,month,day)
# 2. ✅ Create a new student record and add it to the database
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

