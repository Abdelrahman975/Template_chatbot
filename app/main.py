from fastapi import FastAPI
from app.config.settings import settings

# Create FastAPI instance
app = FastAPI(
    title=settings.APP_NAME,
    description="Clean FastAPI Project Structure",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to FastAPI Clean Architecture"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    ) 