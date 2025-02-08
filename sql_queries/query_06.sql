SELECT g.id as group_id ,g.group_name , s.student_name
FROM groups g
JOIN students s ON g.id=s.group_id
WHERE g.group_name=?