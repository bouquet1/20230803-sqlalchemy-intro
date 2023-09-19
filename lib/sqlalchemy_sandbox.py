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
# Tom Tobar ve Albert Einstein (sonra siliyoruz denemek icin ondan listenin son halinde yok) i de ayni sekilde yazdik. we need to add and commit our students to DB.  
#   session.add(thompson_plyler)    =>TO ADD TO DB
#   session.commit()                => TO PERSIST/SAVE
#   print(f"New student ID is {thompson_plyler.id}")


# we can also add multiple as a list e.g
#   session.bulk_save_objects([tom_tobar, alan_turing])    
#   session.commit()                    
#   print(f"New student ID is {alan_turing.id}")  
#   print(f"New student ID is {tom_tobar.id}")
#when we run lib/sqlalchemy_sandbox.py we get more info becasue we used  print(f"New student ID is {alan_turing.id}"). IMPORTANT: in terminal we got New Student ID is None for both tom and alan but the info is committed to the DB because .bulk_save_objects() don't get return the same as .add() it returns none.


# 3. ✅ Query all students (ebery instance of Student class/Student model)   
# ONE WAY
#       students = session.query(Student)   
#       print([student for student in students])   
# => (due to __repr__) Student 1: Albert Einstein Grade: 6, Student 2: Thompson Plyler Grade:8, Student 3: Tom etc... 

#ANOTHER WAY  
#       students = session.query(Student).all()    
#       print(students)

# 4. ✅ Query all students by name.
#       students = session.query(Student.name).all()    
#       print(students)

# 5. ✅ Query all students by name, and order by name. 
#       students = session.query(Student.name).order_by(Student.name).all()    
#       print(students)
#       => [('Alan Turing',), ('Thompson Plyler	',), ('Tom Tobar',)]

# 6. ✅ Query all students by name, order by name, descending.
#       students = session.query(Student.name).order_by(desc(Student.grade)).all()    
#       print(students)

# 7. ✅ Limit student query to 1 result. Oldest person. Sort by bday.
#       oldest_student = session.query(Student.name, Student.birthday).order_by(desc(Student.birthday)).limit(1).all()    
#       print(oldest_student)

#       oldest_student = session.query(Student.name, Student.birthday).order_by(asc(Student.birthday)).limit(1).all()    
#       print(oldest_student)


# 8. ✅ Use the SQLAlchemy func.count function to report how many student entries exist.
#       student_count = session.query(func.count(Student.id)).first()
#       print(student_count)


# 9. ✅ Filter student query results by name
#       query = session.query(Student).filter(Student.name.like("%Thompson"), Student.grade == 7)  
#       print(query)


# 10. ✅ Update the student data for a single column. Let's increase the grades of every student.
# WITH UPDATE  METHOD
#       session.query(Student).update({Student.grade: Student.grade + 1})
#       
#       print([(
#           student.name,
#           student.grade
#       ) for student in session.query(Student)])


# WITHOUT UPDATE  METHOD
#       for student in session.query(Student)
#           student.grade += 1

#           session.commit()
# above we query and updated and committed it

#           print([(student.name, student.grade) for student in session.query(Student)])
# here we retrieve the (read) the uograded results 


# 11. ✅ Delete a student database entry/row. Find the person(entry) to delete and than run delete method on the entry.
#   query = session.query(Student).filter(Student.name.like("%Albert%"))
#   albert_einstein = query.first()
#   print(albert_einstein)
#
#   session.delete(albert_einstein)
#   session.commit()
#
#   albert_einstein = query.first()
#   print("Hopefully is None: ", albert_einstein)
#   => Hopefully is None: None bc we deleted and committed it 



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
            # \n to make a new line so each student in terminal will be written separate lines instead of one line. more readable.

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

# Extra notes from lecture 
    # Index func helping us speed up the searhc. what is your expect to be use a query parameter it is name in this case.
    # email (55) restricting the length of the email to 55
    # def __repr__ (self) comes with every single python class. f""" string interpolation. repr[/reapir/] do: affects when we print this value we gonna get more useful info rather than just print something. useful tool we can trust it is for python not sql specific thing.
    # place it to db, declare an engine, make a session with sessionmaker. Engine is the python obj sits directly on IF with directly with DB.  the thing typing python commands sending them to DB and then retrieving the info is the ENGINE. we pass the engine into a sessionmaker. engine talking directly to DB session we'll pas in that session in.  import sessionmaker don't forget. "from sqlalchemy.orm import sessionmaker"  
    #   engine = create_engine('sqlite:///students.db') => comes from import create_engine. it'll interact with students.db and if it doesn;t exist it will create students.db
    #   Base.metadata.create_all(engine)
    #   Session = sessionmaker(bind=engine) => with sessionmaker() method, we get a func back Session() by declarion a Session. the 'sessionmaker(bind=engine)' here is what's called a factory.
    #   session = Session() => we're calling/invoking Session() we use the session class and create a session object that is instance of a session class. 