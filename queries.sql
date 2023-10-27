-- name: get_users
-- Get all users from the database 
select id, name, email 
from User;


-- name: get_user_by_name^
-- Get a user from the database using a named parameter
select id, name, email
from User
where name = :name;



