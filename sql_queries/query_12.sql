SELECT g.id AS number_group,
       g.group_name,
       s.student_name,
       s2.subject_title,
       g2.grade,
       g2.created_at AS last_lesson_date
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades g2 ON g2.student_id = s.id
JOIN subjects s2 ON g2.subject_id = s2.id
WHERE g2.created_at = (
    SELECT MAX(g3.created_at)
    FROM grades g3
    JOIN students s3 ON s3.id = g3.student_id
    WHERE s3.group_id = g.id AND g3.subject_id = s2.id
) AND s2.subject_title=? AND g.group_name=?;