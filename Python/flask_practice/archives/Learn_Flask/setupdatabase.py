from app import db, Task_Model

# creates all the  models into db tables
db.create_all()


# task1 = Task_Model('Task1', 'task1_desc', '23122')
# task2 = Task_Model('Task2', 'task2_desc', '223122')

# print(task1.id)
# print(task2.id)

# # add all as list of objects
# db.session.add_all([task1, task2])

# # one at a time
# # db.session.add(task1)
# # db.session.add(task2)

# # save changes
# db.session.commit()

# print(task1.id)
# print(task2.id)
