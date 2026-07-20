from fastapi import APIRouter, Depends, HTTPException, status

from app.database import get_profile_by_user_id, get_user_by_email
from app.dependencies import get_current_user
from app.schemas import AuthMeResponse, LoginRequest, ProfileOut, TokenResponse
from app.security import create_access_token, verify_password


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest) -> TokenResponse:
    user = get_user_by_email(payload.email)
    if not user or not verify_password(payload.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(subject=user["id"])
    return TokenResponse(access_token=token)


@router.get("/me", response_model=AuthMeResponse)
def auth_me(current_user: dict = Depends(get_current_user)) -> AuthMeResponse:
    profile = get_profile_by_user_id(current_user["id"])
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")

    return AuthMeResponse(email=current_user["email"], profile=ProfileOut(**profile))
