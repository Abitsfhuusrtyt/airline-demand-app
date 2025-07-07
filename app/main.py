from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.data import get_real_data
from app.ai import analyze_data_with_gpt
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = get_real_data()
    insights = analyze_data_with_gpt(data)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "data": data,
        "insights": insights
    })

@app.post("/filter", response_class=HTMLResponse)
async def filter_data(
    request: Request,
    source: str = Form(""),
    destination: str = Form(""),
    class_: str = Form("")
):
    data = get_real_data()

    # Apply filters
    filtered_data = [
        route for route in data
        if (not source or route['origin'] == source) and
           (not destination or route['destination'] == destination)
        # Note: class_ is not used because get_real_data() doesn't generate "class"
    ]

    # Analyze the filtered data using GPT
    insights = analyze_data_with_gpt(filtered_data)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "data": filtered_data,
        "insights": insights
    })

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
