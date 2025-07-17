from fastapi import APIRouter, Depends, HTTPException
from app.models.user import User
from app.api.routes.auth import get_current_active_user
from app.services.stock_service import get_stock_data

router = APIRouter()

@router.get("/stocks/{symbol}")
async def fetch_stock_data(symbol: str, current_user: User = Depends(get_current_active_user)):
    data = get_stock_data(symbol)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to fetch stock data.")
    return data
