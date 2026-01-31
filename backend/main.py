from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import markets, account  # Add account import
import uvicorn

app = FastAPI(title="The Abacus API")

# CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(markets.router, prefix="/api", tags=["markets"])
app.include_router(account.router, prefix="/api/account", tags=["account"])  # Add this line

@app.get("/")
async def root():
    return {"message": "The Abacus - Count Every Edge"}

@app.get("/api/ping")
async def ping():
    return {
        "message": "pong",
        "status": "connected",
        "service": "The Abacus API"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)