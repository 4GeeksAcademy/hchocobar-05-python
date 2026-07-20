from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status

from app.database import (
    ProfileQuery,
    UserQuery,
    get_user_by_email,
    get_user_by_id,
    profiles_table,
    users_table,
)
from app.dependencies import get_current_user
from app.schemas import UserCreate, UserOut, UserUpdate
from app.security import hash_password


router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> UserOut:
    existing_user = get_user_by_email(payload.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    user_id = str(uuid4())
    now = datetime.now(timezone.utc)

    user = {
        "id": user_id,
        "email": payload.email,
        "hashed_password": hash_password(payload.password),
        "is_active": True,
        "role": "user",
        "created_at": now.isoformat(),
    }

    profile = {
        "id": str(uuid4()),
        "user_id": user_id,
        "name": payload.name,
        "phone": payload.phone,
        "address": payload.address,
    }

    users_table.insert(user)
    profiles_table.insert(profile)

    return UserOut(
        id=user["id"],
        email=user["email"],
        is_active=user["is_active"],
        role=user["role"],
        created_at=datetime.fromisoformat(user["created_at"]),
    )


@router.get("", response_model=list[UserOut])
def list_users(current_user: dict = Depends(get_current_user)) -> list[UserOut]:
    _ = current_user
    users = users_table.all()
    return [
        UserOut(
            id=user["id"],
            email=user["email"],
            is_active=user["is_active"],
            role=user["role"],
            created_at=datetime.fromisoformat(user["created_at"]),
        )
        for user in users
    ]


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: str, current_user: dict = Depends(get_current_user)) -> UserOut:
    _ = current_user
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return UserOut(
        id=user["id"],
        email=user["email"],
        is_active=user["is_active"],
        role=user["role"],
        created_at=datetime.fromisoformat(user["created_at"]),
    )


@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: str,
    payload: UserUpdate,
    current_user: dict = Depends(get_current_user),
) -> UserOut:
    if current_user["id"] != user_id:
        raise HTTPException(status_code=403, detail="No puedes modificar otro usuario")

    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    updates = payload.model_dump(exclude_none=True)
    if "email" in updates:
        email_owner = get_user_by_email(updates["email"])
        if email_owner and email_owner["id"] != user_id:
            raise HTTPException(status_code=400, detail="El email ya está registrado")

    if updates:
        users_table.update(updates, UserQuery.id == user_id)

    updated_user = get_user_by_id(user_id)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return UserOut(
        id=updated_user["id"],
        email=updated_user["email"],
        is_active=updated_user["is_active"],
        role=updated_user["role"],
        created_at=datetime.fromisoformat(updated_user["created_at"]),
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, current_user: dict = Depends(get_current_user)) -> None:
    if current_user["id"] != user_id:
        raise HTTPException(status_code=403, detail="No puedes eliminar otro usuario")

    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    users_table.remove(UserQuery.id == user_id)
    profiles_table.remove(ProfileQuery.user_id == user_id)
