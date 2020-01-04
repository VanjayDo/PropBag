-- 创建数据库，设置collate以识别中文，不会乱码
CREATE DATABASE practice_sql COLLATE Chinese_PRC_CS_AI_WS;
go
-- 使用数据库
use practice_sql;
go

-- 创建数据表，
create table department
(
    id           int identity
        primary key,
    name         varchar(80),
    employee_num int
)
create table position
(
    id           int identity
        primary key,
    name         varchar(80),
    employee_num int
)
create table title
(
    id           int identity
        primary key,
    name         varchar(80),
    employee_num int
)
create table employee
(
    id          int identity
        primary key,
    employee_id int
        unique,
    name        varchar(80),
    gender      varchar(10),
    phone_num   varchar(20),
    dept_id     int
        references department
            on delete cascade,
    title_id    int
        references title
            on delete cascade,
    position_id int
        references position
            on delete cascade
)
create table education_experience
(
    id              int identity
        primary key,
    employee_id     int
        references employee (employee_id)
            on delete cascade,
    school          varchar(80),
    major           varchar(80),
    degree          varchar(80),
    graduation_year varchar(10)
)
create table work_experience
(
    id               int identity
        primary key,
    employee_id      int
        references employee (employee_id)
            on delete cascade,
    employer         varchar(80),
    position         varchar(80),
    resignation_date varchar(50)
)
create table family_info
(
    id           int identity
        primary key,
    name         varchar(80),
    employee_id  int
        references employee (employee_id)
            on delete cascade,
    relationship varchar(80),
    phone_num    varchar(20)
)
create table reward_and_punishment
(
    id          int identity
        primary key,
    employee_id int
        references employee (employee_id)
            on delete cascade,
    statement   varchar(1000),
    date        varchar(50),
    location    varchar(200)
)
go

-- 插入一些的部门，职位职称信息，因为employee表以它们这些表为外键，所以这些数据必须有相关的信息，employee才能插入
insert into department values ('algo develop', 0)
insert into department values ('network security', 0)
insert into title values ('senior engineer', 0)
insert into title values ('junior engineer', 0)
insert into position values ('manager', 0)
insert into position values ('leader', 0)
go

-- 创建存储过程，视图，触发器
-- 创建视图
create view query_employee_info
as
select e.employee_id, e.name "employee_name", d.name 'dept', p.name 'title', t.name 'position'
from employee e
         left join department d on e.dept_id = d.id
         left join position p on e.position_id = p.id
         left join title t on e.title_id = t.id
go

-- 执行如下进行从视图查询
select *
from query_employee_info;
go

-- 创建存储过程
-- 因为上面创建的query_employee_info视图已经包含了聚合了所有需要的信息，所以这里直接从该视图取数据进行处理即可
-- 创建存储过程查询各个部门,各种职称的职工数量
create procedure query_employee_nums_in_diff_dept_with_diff_title
as
begin
    select dept, title, count(title) 'num' from query_employee_info group by dept, title;
end
go
-- 执行以下命令来执行存储过程
exec query_employee_nums_in_diff_dept_with_diff_title
go
-- 创建触发器
-- 新增员工后自动更新员工数量
create trigger update_employee_num_for_insert_employee
    on employee
    for insert
    as
begin
    update department set employee_num = employee_num + 1 where id = (select dept_id from inserted)
    update position set employee_num = employee_num + 1 where id = (select position_id from inserted)
    update title set employee_num = employee_num + 1 where id = (select title_id from inserted)
end
go

-- 更新员工信息后自动更新员工数量
create trigger update_employee_num_for_update_employee
    on employee
    for update
    as
begin
    if (select dept_id from deleted) <> (select dept_id from inserted)
        update department set employee_num = employee_num + 1 where id = (select dept_id from inserted)
        update department set employee_num = employee_num - 1 where id = (select dept_id from deleted)
    if (select position_id from deleted) <> (select position_id from inserted)
        update position set employee_num = employee_num + 1 where id = (select position_id from inserted)
        update position set employee_num = employee_num - 1 where id = (select position_id from inserted)
    if (select title_id from deleted) <> (select title_id from inserted)
        update title set employee_num = employee_num + 1 where id = (select title_id from inserted)
        update title set employee_num = employee_num - 1 where id = (select title_id from inserted)
end
go

-- 删除员工后自动更新员工数量
create trigger update_employee_num_for_delete_employee
    on employee
    for delete
    as
begin
    update department set employee_num = employee_num - 1 where id = (select dept_id from deleted)
    update position set employee_num = employee_num - 1 where id = (select position_id from deleted)
    update title set employee_num = employee_num - 1 where id = (select title_id from deleted)
end
go