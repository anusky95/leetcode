/*
Write an SQL query to reformat the table such that there is a department id column and a revenue column for each month.

The query result format is in the following example:

Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

Result table:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+

Note that the result table has 13 columns (1 for the department id + 12 for the months).
*/

# Write your MySQL query statement below
select t.id, 
min(case when t.month='Jan' then t.revenue else null end) as Jan_Revenue,
min(case when t.month='Feb' then t.revenue else null end) as Feb_Revenue,
min(case when t.month='Mar' then t.revenue else null end) as Mar_Revenue,
min(case when t.month='Apr' then t.revenue else null end) as Apr_Revenue,
min(case when t.month='May' then t.revenue else null end) as May_Revenue,
min(case when t.month='Jun' then t.revenue else null end) as Jun_Revenue,
min(case when t.month='Jul' then t.revenue else null end) as Jul_Revenue,
min(case when t.month='Aug' then t.revenue else null end) as Aug_Revenue,
min(case when t.month='Sep' then t.revenue else null end) as Sep_Revenue,
min(case when t.month='Oct' then t.revenue else null end) as Oct_Revenue,
min(case when t.month='Nov' then t.revenue else null end) as Nov_Revenue,
min(case when t.month='Dec' then t.revenue else null end) as Dec_Revenue
from Department t
group by t.id
