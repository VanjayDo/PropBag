import json
from flask_cors import CORS
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# from db_tables import metadata

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

# 数据库连接参数
db_user_name = 'sa'
db_user_passwd = 'testDocker4Fang'
db_server_ip = 'localhost'
db_name = 'practice_sql'
db_port = '1433'
# 连接数据库
db_connection_url = 'mssql+pymssql://' + db_user_name + ':' + db_user_passwd + '@' + \
                    db_server_ip + ':' + db_port + '/' + db_name
db_engine = create_engine(db_connection_url)

# 直接通过sqlalchemy创建数据表
# metadata.create_all(db_engine)

# 创建执行sql的session
session = scoped_session(sessionmaker(bind=db_engine))
sess = session()


# edu functions

@app.route('/api/edu/create', methods=['POST'])
def create_edu():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    major = requests['major']
    school = requests['school']
    degree = requests['degree']
    graduation_year = requests['graduation_year']
    try:
        sess.execute(
            "insert into education_experience(employee_id, major, school, degree,graduation_year) values(:employee_id,:major,:school,:degree,:graduation_year)",
            {'employee_id': employee_id, 'major': major, 'school': school, 'graduation_year': graduation_year,
             'degree': degree})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '创建失败, 请检查员工id是否存在'
    return '创建成功'


@app.route('/api/edu/update_by_id', methods=['POST'])
def update_edu_by_employee_id_degree():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    employee_id = requests['employee_id']
    major = requests['major']
    school = requests['school']
    degree = requests['degree']
    graduation_year = requests['graduation_year']
    try:
        sess.execute(
            'update education_experience set employee_id=:employee_id,school=:school,major=:major,graduation_year=:graduation_year,degree=:degree where id=:data_id',
            {'employee_id': employee_id, 'school': school, 'major': major, 'degree': degree,
             'graduation_year': graduation_year, 'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '更新失败，请检查数据id是否存在'
    return '更新成功'


@app.route('/api/edu/find_by_employee_id', methods=['POST'])
def find_edu_by_employee_id():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    results = sess.execute('select * from education_experience where employee_id=:employee_id ',
                           {'employee_id': employee_id})
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/edu/findall', methods=['POST'])
def findall_edu():
    results = sess.execute('select * from education_experience')
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/edu/delete_by_employee_id', methods=['POST'])
def delete_edu():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    try:
        sess.execute('delete from education_experience where employee_id=:employee_id', {'employee_id': employee_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '删除失败，请检查员工id是否存在'
    return '删除成功'


# work funcitons

@app.route('/api/work/create', methods=['POST'])
def create_work():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    employer = requests['employer']
    resignation_date = requests['resignation_date']
    try:
        sess.execute(
            "insert into work_experience(employee_id, employer,resignation_date) values(:employee_id,:employer,convert(varchar,convert(datetime,:resignation_date),23))",
            {'employee_id': employee_id, 'employer': employer, 'resignation_date': resignation_date})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '创建失败，请检查员工id是否存在'
    return '创建成功'


@app.route('/api/work/update_by_id', methods=['POST'])
def update_work_by_id():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    employee_id = requests['employee_id']
    employer = requests['employer']
    resignation_date = requests['resignation_date']
    position = requests['position']
    try:
        sess.execute(
            'update work_experience set employee_id=:employee_id,resignation_date=convert(varchar,convert(datetime,:resignation_date),23),employer=:employer,position=:position where id=:data_id ',
            {'employer': employer, 'resignation_date': resignation_date, 'employee_id': employee_id,
             'position': position, 'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '更新失败，请检查数据id是否存在'
    return '更新成功'


@app.route('/api/work/find_by_employee_id', methods=['POST'])
def find_work_by_employee_id():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    results = sess.execute('select * from work_experience where employee_id=:employee_id ',
                           {'employee_id': employee_id})
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/work/findall', methods=['POST'])
def findall_work():
    results = sess.execute('select * from work_experience')
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/work/delete_by_employee_id', methods=['POST'])
def delete_work():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    try:
        sess.execute('delete from work_experience where employee_id=:employee_id', {'employee_id': employee_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '删除失败, 请检查员工id是否存在'
    return '删除成功'


# employee functions

@app.route('/api/employee/create', methods=['POST'])
def create_employee():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    name = requests['name']
    gender = requests['gender']
    phone_num = requests['phone_num']
    dept_id = int(requests['dept_id'])
    title_id = int(requests['title_id'])
    position_id = int(requests['position_id'])
    try:
        sess.execute(
            "insert into employee(employee_id,name,gender,phone_num,dept_id,title_id,position_id) values(:employee_id,:name,:gender,:phone_num,:dept_id,:title_id,:position_id)",
            {'employee_id': employee_id, 'name': name, 'gender': gender, 'phone_num': phone_num,
             'dept_id': dept_id, 'title_id': title_id, 'position_id': position_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '创建失败，请检查员工id是否重复，以及各编号在表中是否存在'
    return '创建成功'


@app.route('/api/employee/update_by_employee_id', methods=['POST'])
def update_employee_by_employee_id():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    name = requests['name']
    gender = requests['gender']
    phone_num = requests['phone_num']
    dept_id = int(requests['dept_id'])
    title_id = int(requests['title_id'])
    position_id = int(requests['position_id'])
    try:
        sess.execute('update employee set name=:name, gender=:gender, phone_num=:phone_num,'
                     'dept_id=:dept_id,title_id=:title_id,position_id=:position_id where employee_id=:employee_id',
                     {'employee_id': employee_id, 'name': name, 'gender': gender, 'phone_num': phone_num,
                      'dept_id': dept_id, 'title_id': title_id, 'position_id': position_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '更新失败, 请检查员工id是否存在'
    return '更新成功'


@app.route('/api/employee/find_by_name', methods=['POST'])
def find_employee_by_name():
    requests = json.loads(request.get_data())
    name = requests['name']
    results = sess.execute('select * from employee where name=:name ', {'name': name})
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/employee/findall', methods=['POST'])
def findall_employee():
    results = sess.execute('select * from employee')
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/employee/delete_by_employee_id', methods=['POST'])
def delete_employee():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    try:
        sess.execute('delete from employee where employee_id=:employee_id', {'employee_id': employee_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '删除失败, 请检查员工id是否存在'
    return '删除成功'


# family_relationship functions

@app.route('/api/family_relationship/create', methods=['POST'])
def create_relationship():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    name = requests['name']
    relationship = requests['relationship']
    phone_num = requests['phone_num']
    try:
        sess.execute(
            "insert into family_info(employee_id,name,phone_num,relationship) values(:employee_id,:name,:phone_num,:relationship)",
            {'employee_id': employee_id, 'name': name, 'phone_num': phone_num, 'relationship': relationship})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '创建失败, 请检查员工id是否存在'
    return '创建成功'


@app.route('/api/family_relationship/update_by_id', methods=['POST'])
def update_relationship_by_employee_id_relationship():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    employee_id = requests['employee_id']
    name = requests['name']
    relationship = requests['relationship']
    phone_num = requests['phone_num']
    try:
        sess.execute(
            'update family_info set name=:name, phone_num=:phone_num ,employee_id=:employee_id , relationship=:relationship where id=:data_id',
            {'employee_id': employee_id, 'name': name, 'phone_num': phone_num, 'relationship': relationship,
             'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '更新失败，请检查信息'
    return '更新成功'


@app.route('/api/family_relationship/find_by_employee_id', methods=['POST'])
def find_relationship_by_employee_id():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    results = sess.execute('select * from family_info where employee_id=:employee_id ', {'employee_id': employee_id})
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/family_relationship/findall', methods=['POST'])
def findall_relationship():
    results = sess.execute('select * from family_info')
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/family_relationship/delete_by_id', methods=['POST'])
def delete_relationship():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    try:
        sess.execute('delete from family_info where id=:data_id', {'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '删除失败, 请检查数据id是否存在'
    return '删除失败'


# reward_and_punishment functions

@app.route('/api/reward_and_punishment/create', methods=['POST'])
def create_reward_and_punishment():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    statement = requests['statement']
    date = requests['date']
    location = requests['location']
    try:
        sess.execute(
            "insert into reward_and_punishment(employee_id,statement,date,location) values(:employee_id,:statement,convert(varchar,convert(datetime,:date),23),:location)",
            {'employee_id': employee_id, 'statement': statement, 'date': date, 'location': location})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '创建失败'
    return '创建成功'


@app.route('/api/reward_and_punishment/update_by_id', methods=['POST'])
def update_reward_and_punishment_by_id():
    requests = json.loads(request.get_data())
    id = requests['id']
    employee_id = requests['employee_id']
    statement = requests['statement']
    date = requests['date']
    location = requests['location']
    try:
        sess.execute(
            'update reward_and_punishment set employee_id=:employee_id, statement=:statement,date=convert(varchar,convert(datetime,:date),23),location=:location where id=:id',
            {'employee_id': employee_id, 'statement': statement, 'date': date, 'location': location, 'id': id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '更新失败, 请检查数据id是否存在'
    return '更新成功'


@app.route('/api/reward_and_punishment/find_by_employee_id', methods=['POST'])
def find_reward_and_punishment_by_employee_id():
    requests = json.loads(request.get_data())
    employee_id = requests['employee_id']
    results = sess.execute('select * from reward_and_punishment where employee_id=:employee_id ',
                           {'employee_id': employee_id})
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/reward_and_punishment/findall', methods=['POST'])
def findall_reward_and_punishment():
    results = sess.execute('select * from reward_and_punishment')
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/reward_and_punishment/delete_by_id', methods=['POST'])
def delete_reward_and_punishment():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    try:
        sess.execute('delete from reward_and_punishment where id=:data_id', {'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '删除失败，请检查数据id是否存在'
    return '删除成功'


# department functions
@app.route('/api/department/create', methods=['POST'])
def create_department():
    requests = json.loads(request.get_data())
    name = requests['name']
    try:
        sess.execute(
            "insert into department(name,employee_num) values(:name,0)", {'name': name})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '创建失败'
    return '创建成功'


@app.route('/api/department/update_by_id', methods=['POST'])
def update_department_by_id():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    name = requests['name']
    try:
        sess.execute('update department set name=:name where id=:data_id', {'name': name, 'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return 'update failed'
    return 'update succeed'


@app.route('/api/department/findall', methods=['POST'])
def findall_department():
    results = sess.execute('select * from department')
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/department/delete_by_id', methods=['POST'])
def delete_department():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    try:
        sess.execute('delete from department where id=:data_id', {'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '删除失败，请检查数据id是否存在'
    return '删除成功'


# position functions

@app.route('/api/position/create', methods=['POST'])
def create_position():
    requests = json.loads(request.get_data())
    name = requests['name']
    try:
        sess.execute(
            "insert into position(name,employee_num) values(:name,0)", {'name': name})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '创建失败'
    return '创建成功'


@app.route('/api/position/update_by_id', methods=['POST'])
def update_position_by_id():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    name = requests['name']
    try:
        sess.execute('update position set name=:name where id=:data_id', {'name': name, 'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '更新失败'
    return '更新成功'


@app.route('/api/position/findall', methods=['POST'])
def findall_position():
    results = sess.execute('select * from position')
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/position/delete_by_id', methods=['POST'])
def delete_position():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    try:
        sess.execute('delete from position where id=:data_id', {'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '删除失败，请检查数据id是否存在'
    return '删除成功'


# title functions

@app.route('/api/title/create', methods=['POST'])
def create_title():
    requests = json.loads(request.get_data())
    name = requests['name']
    try:
        sess.execute(
            "insert into title(name,employee_num) values(:name,0)", {'name': name})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '创建失败'
    return '创建成功'


@app.route('/api/title/update_by_id', methods=['POST'])
def update_title_by_id():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    name = requests['name']
    try:
        sess.execute('update title set name=:name where id=:data_id', {'name': name, 'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '更新失败'
    return '更新成功'


@app.route('/api/title/findall', methods=['POST'])
def findall_title():
    results = sess.execute('select * from title')
    results = results.fetchall()
    r = []
    for i in results:
        r.append(list(i))
    return jsonify(r)


@app.route('/api/title/delete_by_id', methods=['POST'])
def delete_title():
    requests = json.loads(request.get_data())
    data_id = requests['id']
    try:
        sess.execute('delete from title where id=:data_id', {'data_id': data_id})
        sess.commit()
    except Exception as e:
        sess.rollback()
        print(e)
        return '删除失败，请检查数据id是否存在'
    return '删除成功'


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='5000')
