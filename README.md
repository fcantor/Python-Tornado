## Examples of simple Python endpoints using [Tornado](https://www.tornadoweb.org/en/stable/) as a web framework

### How to use:
- Fork this repo
- In the command line:
  - Make sure you're in the Python-Tornado directory
  - Run `./index.py` to start the server locally

### Endpoints
- Visit `localhost:8882` on your browser
Example | Endpoint | Address 
--- | --- | ---
Simple request handler | basicRequestHandler | `localhost:8882/`
List | listRequestHandler | `localhost:8882/animals`
Query Parameter | queryParamRequestHandler | `localhost:8882/isEven?num=__[INSERT NUMBER]__`
Resource Parameter | resourceParamRequestHandler | `localhost:8882/students/__[ANY NAME]__/__[ANY NUMBER]__

