from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from .config import settings
from .routers import user
from .models import user as user_model
from .utils.auth import get_password_hash

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router, prefix="/api/v1", tags=["users"])

# Create initial superuser if not exists
@app.on_event("startup")
async def create_superuser():
    db = next(get_db())
    
    # Check if any user exists
    user_exists = db.query(user_model.User).first()
    
    if not user_exists:
        # Create superuser
        superuser = user_model.User(
            username="admin",
            email="admin@example.com",
            hashed_password=get_password_hash("adminpassword"),
            first_name="Admin",
            last_name="User",
            is_active=True,
            is_superuser=True,
        )
        
        db.add(superuser)
        db.commit()

@app.get("/", tags=["root"])
async def root():
    return {
        "message": "Welcome to the User Management API",
        "documentation": "/docs",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
