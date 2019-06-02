# Write your MySQL query statement below
select 
IFNULL(
       (SELECT DISTINCT Salary
       from Employee
       Order by Salary DESC
       LIMIT 1 OFFSET 1),NULL) AS SecondHighestSalary;
