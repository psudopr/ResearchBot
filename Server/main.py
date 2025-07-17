from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.routes import companies, articles, auth, prompt, stocks
from app.services.scheduler import schedule_jobs
from app.db.database import db
from app.core.exceptions import CrawlingError, SummarizationError

app = FastAPI(title="ResearchBot API")

@app.exception_handler(CrawlingError)
async def crawling_exception_handler(request: Request, exc: CrawlingError):
    return JSONResponse(
        status_code=500,
        content={"message": f"Failed to crawl {exc.url}: {exc.message}"},
    )

@app.exception_handler(SummarizationError)
async def summarization_exception_handler(request: Request, exc: SummarizationError):
    return JSONResponse(
        status_code=500,
        content={"message": f"Failed to summarize content: {exc.message}"},
    )

@app.on_event("startup")
def startup_event():
    schedule_jobs(db)

app.include_router(auth.router, tags=["Authentication & Users"])
app.include_router(prompt.router, prefix="/users", tags=["User Settings"])
app.include_router(companies.router, prefix="/companies", tags=["Companies"])
app.include_router(articles.router, prefix="/articles", tags=["Articles"])
app.include_router(stocks.router, prefix="/data", tags=["Market Data"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the ResearchBot API"}
