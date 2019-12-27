## Examples of simple Python endpoints using [Tornado](https://www.tornadoweb.org/en/stable/) as a web framework

### How to use:
- Fork this repo
- In the command line:
  - Make sure you're in the Python-Tornado directory
  - Run `./basic-endpoints.py` to start the server locally

### Endpoints
- Visit `localhost:8882` on your browser

|Type | Endpoint | Address | Example |
|--- | :---: | :---: | :---: |
Simple request handler | basicRequestHandler | `localhost:8882/` | 
Render HTML | listRequestHandler | `localhost:8882/animals` | 
Query Parameter | queryParamRequestHandler | localhost:8882/isEven?num=__[ANY NUMBER]__ | `localhost:8882/isEven?num=3`
Resource Parameter | resourceParamRequestHandler | localhost:8882/students/__[ANY NAME]__/__[ANY NUMBER]__ | `localhost:8882/students/francesca/123`
