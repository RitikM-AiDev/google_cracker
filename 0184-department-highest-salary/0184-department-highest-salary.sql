# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as salary 
from Employee as e join department as d on d.id = e.departmentId where e.salary = (
    select MAX(e2.salary) from Employee e2 where e2.departmentId = e.departmentId
)
