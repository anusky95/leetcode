/*
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  
  SET N=N-1;
  RETURN (
      SELECT DISTINCT salary FROM employee ORDER BY salary DESC LIMIT N,1
  );
END


/* 

NOTES

Limit 3 offset 18 means start at record number 19 and give 3 records 
Limit 3 offset 18 means  = LIMIT 18,3 {Notice that its reversed}
https://www.w3schools.com/php/php_mysql_select_limit.asp

SYNTAX:
CREATE FUNCTION funcname(varname vartype) 
RETURNS vartype
BEGIN
...........
...........
END




*/
