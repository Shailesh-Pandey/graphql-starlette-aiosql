# graphql-starlette-aiosql  

Poetry is used for package depedency and management.  
(for steps to install: https://python-poetry.org/docs/)  

To run (using poetry):  
poetry run uvicorn graphql_starlette_aiosql.api:app  
poetry run pytest .\tests\tests.py  

To run (using the classic way):  
uvicorn graphql_starlette_aiosql.api:app --reload (or  python graphql_starlette_aiosql.api.py)  
pytest .\tests\tests.py  

