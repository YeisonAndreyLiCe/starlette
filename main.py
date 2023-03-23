from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse, JSONResponse, RedirectResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from queries import get_all_students
import queries

templates=Jinja2Templates(directory="templates")

async def index(request: Request):
    student_id = request.path_params.get("student_id") or 0
    student_name = request.query_params.get("student_name") or "world"
    return PlainTextResponse(content=f"Hello, {student_name} {student_id}!")

async def json_endpoint(request: Request):
    return JSONResponse(content={"message": "Hello, world!"})

async def html_endpoint(request: Request):
    students = get_all_students()
    context = {"request": request, "students": students}
    return templates.TemplateResponse("index.html", context)

async def create_student(request: Request):
    if request.method == "POST":
        data = await request.form()
        queries.create_student(data)
        return RedirectResponse(request.url_for("html_endpoint"), status_code=303)
    context = {"request": request}
    return templates.TemplateResponse("create_student.html", context)

async def update_student(request: Request):
    student_id = request.path_params.get("student_id")
    student = queries.get_student_by_id(student_id)
    context = {"request": request, "student": student}
    if request.method == "POST":
        data = await request.form()
        queries.update_student(student_id, data)
        return RedirectResponse(request.url_for("html_endpoint"), status_code=303)
    return templates.TemplateResponse("update_student.html",context)

async def delete_student(request: Request):
    student_id = request.path_params.get("student_id")
    queries.delete_student(student_id)
    return RedirectResponse(request.url_for("html_endpoint"), status_code=303)

routes = [
    #Route("/{student_id:int}/", endpoint=index),
    Route("/json", endpoint=json_endpoint),
    Route("/", endpoint=html_endpoint),
    Route("/create_student", endpoint=create_student, methods=["GET", "POST"]),
    Route("/update_student/{student_id}", endpoint=update_student, methods=["GET", "POST"]),
    Route("/delete_student/{student_id}", endpoint=delete_student, methods=["GET", "POST"]),
]

app = Starlette(debug=True, routes=routes)