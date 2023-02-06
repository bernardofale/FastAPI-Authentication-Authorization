from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.crud.crud_ops import insert_user, get_user, authenticate_user
from app.resp_models.model import Token, UserInDB
from datetime import datetime, timedelta
from decouple import config
from app.auth.gen_tokens import create_access_token

router = APIRouter(
    prefix = "/auth",
    tags = ["auth"]
)
JWT_EXPIRY = config("expiry")

@router.post("/", response_model=Token)
async def login(response : Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(JWT_EXPIRY))
    token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response.set_cookie(key="access_token", value = token.access_token, httponly=True, secure=True)
    return token

@router.post("/register", )
def register(user : UserInDB):
    return insert_user(user)