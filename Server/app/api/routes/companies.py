from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.models.company import Company
from app.models.user import User
from app.api.dependencies import get_current_active_user
from app.db.database import db

router = APIRouter()

@router.post("/", response_model=Company)
def create_company(company: Company, current_user: User = Depends(get_current_active_user)):
    company.user_id = current_user.id
    inserted_id = db.companies.insert_one(company.dict(by_alias=True)).inserted_id
    new_company = db.companies.find_one({"_id": inserted_id})
    return new_company

@router.get("/", response_model=list[Company])
def get_companies(current_user: User = Depends(get_current_active_user)):
    companies = list(db.companies.find({"user_id": current_user.id}))
    return companies

@router.get("/{company_id}", response_model=Company)
def get_company(company_id: str, current_user: User = Depends(get_current_active_user)):
    company = db.companies.find_one({"_id": ObjectId(company_id), "user_id": current_user.id})
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.put("/{company_id}", response_model=Company)
def update_company(company_id: str, company_update: Company, current_user: User = Depends(get_current_active_user)):
    existing_company = db.companies.find_one({"_id": ObjectId(company_id), "user_id": current_user.id})
    if existing_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    
    db.companies.update_one(
        {"_id": ObjectId(company_id)},
        {"$set": company_update.dict(exclude_unset=True, by_alias=True)}
    )
    updated_company = db.companies.find_one({"_id": ObjectId(company_id)})
    return updated_company

@router.delete("/{company_id}")
def delete_company(company_id: str, current_user: User = Depends(get_current_active_user)):
    result = db.companies.delete_one({"_id": ObjectId(company_id), "user_id": current_user.id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Company not found")
    # Also delete associated articles
    db.articles.delete_many({"company_id": company_id})
    return {"message": "Company and associated articles deleted successfully"}
