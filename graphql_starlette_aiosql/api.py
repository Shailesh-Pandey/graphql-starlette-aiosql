import aiosql, sqlite3
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from starlette.applications import Starlette
import psycopg2

# Define the GraphQL schema using SDL
type_defs = """
type Query {
  users: [Users!]!
  hello: String!
  bye: String!
  experiment(num: Int!): String!
  get_user_by_name(name: String!): Users!
  
}

type Users {
  id: String!
  name: String!
  email: String!
}
"""

# Define the resolvers for the schema using Aiosql
queries = aiosql.from_path("graphql_starlette_aiosql/queries.sql", "sqlite3")
#queries = aiosql.from_path("queries2.sql", "psycopg2")
query = QueryType()


conn = sqlite3.connect("graphql_starlette_aiosql/Users.db", check_same_thread=False)

'''
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="pass123",
    host="localhost",
    port="5432"
)
'''

#@query.field("users")
#async def resolve_users(*_):
#    return await queries.get_users(conn)

@query.field("users")
def resolve_users(*_):
     rows = queries.get_users(conn)
     json = {}
     result = []
     for row in rows:
         json['id']=row[0]
         json['name']=row[1]
         json['email']=row[2]
         result.append(json.copy())
     return result

@query.field("hello")
def resolve_hello(*_):
    return "Hello world!"

@query.field("experiment")
def fun(*_, num):
    return "hello "*num

@query.field("bye")
def resolve_hello(*_):
    return "Bye world!"

@query.field("get_user_by_name")
def get_user_by_name(*_, name):
    row = queries.get_user_by_name(conn,name)
    result = {'id':'Null','name':'Null','email':'Null'}
    if(row!=None):
        result['id']=row[0]
        result['name']=row[1]
        result['email']=row[2]  
    return result

# Create a Starlette application and mount the GraphQL route using Ariadne
schema = make_executable_schema(type_defs, query)
app = Starlette()
app.mount("/graphql", GraphQL(schema))

# Start the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
