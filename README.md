# Uvicorn, Starlette and Ray

> What about serving a moderate amount of requests from a Python server? Isn’t Python single-threaded? Yes, it is and this is a problem. Fortunately this problem has a few possible solutions. [Vaklev N](medium.com/codex/async-and-distributed-python-server-with-uvicorn-starlette-and-ray-185828ad2555)

Here is a simple async Uvicorn server example:

```python
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.requests import Request


async def json_endpoint(request: Request):
    return JSONResponse(content={"message": "Hello, world!"})

async def html_endpoint(request: Request):
    students = get_all_students()
    context = {"request": request, "students": students}
    return templates.TemplateResponse("index.html", context)


routes = [
    Route("/json", endpoint=json_endpoint),
    Route("/", endpoint=html_endpoint)
]

app = Starlette(debug=True, routes=routes)
```

## Ray.io for distributed computing

Ray fills in an important gap, namely the ability to orchestrate multiple python processes in a cluster.

And here is a simple Ray server example:

```python
import ray
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse, JSONResponse
from starlette.requests import Request


@ray.remote
def json_endpoint(request: Request):
    return JSONResponse(content={"message": "Hello, world!"})

@ray.remote
def html_endpoint(request: Request):
    students = get_all_students()
    context = {"request": request, "students": students}
    return templates.TemplateResponse("index.html", context)


routes = [
    Route("/json", endpoint=json_endpoint),
    Route("/", endpoint=html_endpoint)
]

app = Starlette(debug=True, routes=routes)
```
