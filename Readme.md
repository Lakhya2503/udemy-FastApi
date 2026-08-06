# web framework
### many on two types

## WSGI
- web server Gatway Interface
- One request at a time per worker

##### One DP Per Order


## ASGI
- async server Gatway Interface
- many request per worker

##### One DP Picks up multiple order3

#### install steps
#### step.1
- create the venv
```
python3 -m venv venv
```


#### step.2
- activate the venv
- use deactive to deactive
```
source venv/bin/activate
```

#### step.3
- create fastapi in standerd way
```
pip install "fastapi[standard]"
```

#### step.4
- app get upgrade in other new changes
```
pip install --upgrade pip
```

#### step.5
- create simple app
```json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Welcome to Zomato order service", "status": "healthy"}

```

#### step.6
- create the requirement.txt file for all other requirements
```
pip freeze > requirement.txt
```

#### step.7
- run the app
```
uvicorn main:app --reload
```
- you can change the port like using the command like

```
uvicorn main:app --reload --port 8001
```