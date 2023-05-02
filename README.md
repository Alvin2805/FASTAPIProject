### fastapi-indomobil-citroen

# python requirement

python 3.10.0 or above

# running program

**for developement uses :**

```bash
uvicorn main:app --reload --port 8080
```

where **main** is the file name of the main app that include the **"app = FastAPI()"**
and **app** is the name of the variable of the **"FastAPI()"** used

# default project structure

parent
--[configs]
--[controllers]
--[cruds]
--[database]
--[models]
--[repositories]
--[schemas]
--main.py
--env
--alembic.ini

# make sure to install alembic then run alembic init alembic to generate the migration tools

New project structure
--[controllers]
--[cruds]
--[database]
--[models]
--[schemas]
--[alembic]
--main.py

# upgrade database migration

alembic upgrade head --> execution the funtion to migrate the models to table

# creation revision

alembic revision -m "nama table" --> to create new function to migrate the new models to table
