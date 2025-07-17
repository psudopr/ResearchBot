from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.models.article import Article
from app.models.user import User
from app.api.routes.auth import get_current_active_user
from app.db.database import db

router = APIRouter()

@router.get("/{company_id}", response_model=list[Article])
def get_articles_for_company(company_id: str, current_user: User = Depends(get_current_active_user)):
    # First, verify the user has access to this company
    company = db.companies.find_one({"_id": ObjectId(company_id), "user_id": current_user.id})
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    
    articles = list(db.articles.find({"company_id": company_id}))
    return articles

@router.put("/{article_id}/read")
def mark_article_as_read(article_id: str, current_user: User = Depends(get_current_active_user)):
    # To ensure security, we should verify that the article belongs to a company owned by the user.
    # This requires a more complex query.
    article = db.articles.find_one({"_id": ObjectId(article_id)})
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    company = db.companies.find_one({"_id": ObjectId(article['company_id']), "user_id": current_user.id})
    if company is None:
        raise HTTPException(status_code=403, detail="User does not have access to this article")

    db.articles.update_one(
        {"_id": ObjectId(article_id)},
        {"$set": {"is_read": True}}
    )
    return {"message": "Article marked as read"}
