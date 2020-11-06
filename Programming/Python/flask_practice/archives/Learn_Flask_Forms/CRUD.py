from app import db, Task_Model
import datetime
#  CREATE
task1 = Task_Model('Hello', 'task1_desc', datetime.datetime.now())
task2 = Task_Model('TASK1', 'task1_desc', datetime.datetime.now())
db.session.add(task1)
db.session.add(task2)
db.session.commit()

# READ
# ==============================================

#  select all
all_tasks = Task_Model.query.all()
print(all_tasks)

# select by id
task_one = Task_Model.query.get(1)
print(task_one)


# filters
trash_task = Task_Model.query.filter_by(title='Hello')
#  gives a list of results
print(trash_task.all())

# UPDATE
# ==============================================
print("updating")
update_first_task = Task_Model.query.get(1)
update_first_task.title = 'Task1'
db.session.add(update_first_task)
db.session.commit()

task_one = Task_Model.query.get(1)
print(task_one)

# DELETE
# ==============================================

print("deleting")
task_two= Task_Model.query.get(5)
db.session.delete(task_two)
print(task_two)
db.session.commit()
