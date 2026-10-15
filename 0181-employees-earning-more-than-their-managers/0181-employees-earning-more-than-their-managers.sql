# Write your MySQL query statement below
SELECT e.name as Employee from Employee as e
WHERE salary > (
    SELECT salary from Employee WHERE id = e.managerId
)