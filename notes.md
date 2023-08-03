# Introduction to SQLAlchemy

## SWABATs
* ... use SQLAlchemy to create a schema for databases
* ... perform all CRUD operations using an illustration class/table.
* ... learn and use example methods provided by SQLAlchemy

## Lecture Objectives
* See numbered comments in `sqlalchemy_sandbox.py`

## Vocabulary
* Schema - the blueprint of a database 
* Persist - save a schema to the database
* Engine - a Python object that translates SQL to Python and vice versa
* Session - a Python object that uses the enginer to allow us to programatically interact with the database
* Transaction - A strategy for executing database statements such that the group succeeds or fails as a unit

## Notes
* The `declarative_base` combines a container for table metadata as well as a group of methods that act as mappers between Python and our SQL database. Inheritance from `Base`, a declarative_base object, allows us to avoid rewriting code.

## Related Lessons
* [ORM Lecture 1 (2023 July 28)](https://vimeo.com/849572769/4a8bc8ec71?share=copy) | [ORM Lecture 2 (2023 31 July)](https://vimeo.com/850302899/973dc63a3c?share=copy)
* [Intro to SQLAlchemy](https://my.learn.co/courses/653/modules/items/83761)
* [Defining a Schema with SQLAlchemy ORM](https://my.learn.co/courses/653/modules/items/95432)
* [Create, Read, Update, and Delete with SQLAlchemy](https://my.learn.co/courses/653/pages/create-read-update-and-delete-with-sqlalchemy?module_item_id=83763)

## Related Methods or imports
  * sessionmaker 
  * create_engine
  * \_\_repr\_\_() - control output format, e.g. during print()
  * session.add(); session.commit()
  * session.bulk_save_objects([albert_einstein, alan_turing]); session.commit() - won't save the values of the input objects to persisted values
  * session.query() is the method called underneat other queries. Example of all
  * session.query(Student).all()
  * session.query().order_by(Student.name).all()
    * order_by(desc(Student.grade)).limit(1).all
    * order_by.first()
  * func, which is distinct from similar methods in Python core. 
  * query.filter(Student.name.like('%Alan%'))
  * Updating:
  * call the object, change the value, session.commit()
  *  session.query(Student).update({
        Student.grade: Student.grade + 1
    })
*    session.delete(albert_einstein)
    session.commit()
    * session.delete(found value); session.commit()
    * query = query_result; query.delete()
  
## Resources
* [SQLAlchemy 1.4 Documentation](https://docs.sqlalchemy.org/en/14/core/tutorial.html)
* [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/intro.html)
* [Example Postgres implementation](https://coderpad.io/blog/development/sqlalchemy-with-postgresql/)