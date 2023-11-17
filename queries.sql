-- name: get_users
-- Get all users from the database 
select id, name, email 
from Users;


-- name: get_user_by_name^
-- Get a user from the database using a named parameter
select id, name, email
from Users
where name = :name;



