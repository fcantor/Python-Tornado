## Examples of simple Python endpoints using [Tornado](https://www.tornadoweb.org/en/stable/) as a web framework

### How to use:

#### Basic Endpoints
This file shows different types of request handlers, from basic endpoints to query and resource paramaters
- Fork this repo
- In the command line:
  - Make sure you're in the Python-Tornado directory
  - Run `./basic-endpoints.py` to start the server locally

#### Examples of RESTful GET and POST
This file shows two simple examples of GET and POST request handlers in one endpoint
- Fork this repo
- In the command line:
  - Make sure you're in the Python-Tornado directory
  - Run `./get-post.py` to start the server locally
- To make a GET request:
  - Open your browser and go to `localhost:8882/characters`
- To make a POST request:
  - Use a service like [Postman](https://www.getpostman.com/)
  - Send a POST request to `localhost:8882/characters?character=[CHARACTER NAME]` (Add a name to append to the existing list.txt)
  - Refresh browser to see the updated list, or open `list.txt` to see the updated list

### Endpoints
- Visit `localhost:8882` on your browser

|Type | Endpoint | Address | Example |
|--- | :---: | :---: | :---: |
Simple request handler | basicRequestHandler | `localhost:8882/` | 
Render HTML | renderHTMLRequestHandler | `localhost:8882/animals` | 
Query Parameter | queryParamRequestHandler | localhost:8882/isEven?num=__[ANY NUMBER]__ | `localhost:8882/isEven?num=3`
Resource Parameter | resourceParamRequestHandler | localhost:8882/students/__[ANY NAME]__/__[ANY NUMBER]__ | `localhost:8882/students/francesca/123`
RESTful GET | listRequestHandler | `localhost:8882/characters` |
RESTful POST | listRequestHandler | localhost:8882/characters?character=__[CHARACTER NAME]__ | `localhost:8882/characters?character=Riker`
