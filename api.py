import aiosql, sqlite3
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from starlette.applications import Starlette

# Define the GraphQL schema using SDL
type_defs = """
type Query {
  users: [User!]!
  hello: String!
  bye: String!
}

type User {
  id: String!
  name: String!
  email: String!
}
"""

# Define the resolvers for the schema using Aiosql
queries = aiosql.from_path("queries.sql", "sqlite3")
query = QueryType()


conn = sqlite3.connect("User.db") 

#@query.field("users")
#async def resolve_users(*_):
#    return await queries.get_users(conn)
	
@query.field("users")
def resolve_users(*_):
     rows = queries.get_users(conn)
     json = {'id':0,'name':0,'email':0}
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

@query.field("bye")
def resolve_hello(*_):
    return "Bye world!"
	
# Create a Starlette application and mount the GraphQL route using Ariadne
schema = make_executable_schema(type_defs, query)
app = Starlette()
app.mount("/graphql", GraphQL(schema))

# Start the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
