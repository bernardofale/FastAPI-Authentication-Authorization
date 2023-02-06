from app.resp_models.model import Token, User
from fastapi import APIRouter, Depends
from ..auth.gen_tokens import get_current_active_user

router = APIRouter(
    prefix = "/users",
    tags = ["users"],
    dependencies = [Depends(get_current_active_user)]
)

@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]