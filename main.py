from fastapi import Depends, FastAPI, HTTPException, status, Response
from app.user_routes import users
from app.auth import gen_tokens


app = FastAPI()

app.include_router(users.router)
app.include_router(gen_tokens.router)


@app.get("/")
async def root():
    return "root"