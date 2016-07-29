# python_mysql_handle
对爬取的数据整理到mySQL数据库
database:mycolor
chart:product
字段：id name hex style
id为自增
其他对应爬取的数值

command
#创建数据库、表、字段
step1: CREATE DATABSE 'mycolor'
step2: CREATE TABLE 'mycolor'.'product'(
'id' INT NOT NULL AUTO_INCREMENT,
'name'  VARCHAR(30) NOT NULL,
'hex' VARCHAR(30) NOT NULL,
'style' VARCHAR(250) NOT NULL,
PRIMARY KEY('id')
) DEFAULT CHARSET = utf8;
#命令创建用户
CREATE USER 'xuan'@'localhost' IDENTIFIED BY '123456';
#授权
GRANT privileges ON mycolor.product(databasename.tablename) TO 'xuan'@'localhost';
#设置和更改密码
SET PASSWORD FOR 'xuan'@'localhost'= PASSWORD("456789")
#撤销用户权限
REVOKE privilege ON mycolor.product FROM 'xuan'@'localhost';
#删除用户
DROP USER 'xuan'@'localhost';


