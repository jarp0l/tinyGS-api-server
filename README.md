# tinyGS-api-server

## Configuration
Copy `.env.example` to `.env` and fill all the values:
```sh
cp .env.example .env`
```

Additionally, you can also look at `app/utils/config.py` and make necessary overwrites.


## Setting up the server
Make sure you have `poetry` installed:
```py
python3 -m pip install pipx
pipx install poetry

# or just
pip install poetry
```

Then create a virtual environment and install all the required packages, which `poetry` will automatically do:
```py
poetry install
```

Now from the root of the project start the server:
```py
poetry run python app/main.py
```

Example output:
```sh
$ poetry run python app/main.py 
INFO:     Will watch for changes in these directories: ['/<stripped>/tinyGS-api-server']
INFO:     Uvicorn running on http://0.0.0.0:8081 (Press CTRL+C to quit)
INFO:     Started reloader process [29763] using WatchFiles
INFO:     Started server process [29771]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Docs
Go to http://127.0.0.1:8081/docs for the API docs generated using SwaggerUI.

For the API docs generated using Redoc, go to http://127.0.0.1:8081/redoc.