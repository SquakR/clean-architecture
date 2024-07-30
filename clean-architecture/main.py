from fastapi import FastAPI

from current_approach.router import router as current_approach_router
from new_approach.router import router as new_approach_router

app = FastAPI()
app.include_router(current_approach_router)
app.include_router(new_approach_router)
