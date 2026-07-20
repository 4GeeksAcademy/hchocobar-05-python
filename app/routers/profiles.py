from fastapi import APIRouter, Depends, HTTPException

from app.database import ProfileQuery, get_profile_by_user_id, profiles_table
from app.dependencies import get_current_user
from app.schemas import ProfileOut, ProfileUpdate


router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/me", response_model=ProfileOut)
def get_my_profile(current_user: dict = Depends(get_current_user)) -> ProfileOut:
    profile = get_profile_by_user_id(current_user["id"])
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return ProfileOut(**profile)


@router.put("/me", response_model=ProfileOut)
def update_my_profile(
    payload: ProfileUpdate,
    current_user: dict = Depends(get_current_user),
) -> ProfileOut:
    profile = get_profile_by_user_id(current_user["id"])
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")

    updates = payload.model_dump(exclude_none=True)
    if updates:
        profiles_table.update(updates, ProfileQuery.user_id == current_user["id"])

    updated_profile = get_profile_by_user_id(current_user["id"])
    if not updated_profile:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")

    return ProfileOut(**updated_profile)
