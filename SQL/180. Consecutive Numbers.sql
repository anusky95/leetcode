# Write your MySQL query statement below
/*
https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-lag-function/
LEAD() - Compares currnt row with next one
LAG() - Compares current row with previous one


SQL Schema
Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+


*/


select distinct Num as "ConsecutiveNums"
from (
SELECT Num,
LEAD(Num,1) over(order by Id) as 'Lead',
LAG(Num,1) over(order by Id) as 'Lag'
from Logs
) as t
where t.num=t.Lead and t.num=t.Lag
