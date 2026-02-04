"""FastAPI web application for password generation."""
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from password import generate_password

app = FastAPI(
    title="Random Password Generator",
    description="A simple API to generate secure random passwords",
    version="1.0.0"
)


class PasswordRequest(BaseModel):
    """Request model for password generation."""
    length: int = 12
    lowercase: bool = True
    uppercase: bool = False
    numbers: bool = False
    symbols: bool = False


class PasswordResponse(BaseModel):
    """Response model containing the generated password."""
    password: str
    length: int


@app.post("/api/generate", response_model=PasswordResponse)
async def generate(request: PasswordRequest):
    """Generate a random password based on the provided options."""
    password = generate_password(
        length=request.length,
        lowercase=request.lowercase,
        uppercase=request.uppercase,
        numbers=request.numbers,
        symbols=request.symbols
    )
    return PasswordResponse(password=password, length=len(password))


@app.get("/api/generate", response_model=PasswordResponse)
async def generate_get(
    length: int = Query(default=12, ge=1, le=128, description="Password length"),
    lowercase: bool = Query(default=True, description="Include lowercase letters"),
    uppercase: bool = Query(default=False, description="Include uppercase letters"),
    numbers: bool = Query(default=False, description="Include numbers"),
    symbols: bool = Query(default=False, description="Include symbols")
):
    """Generate a random password (GET method for simple requests)."""
    password = generate_password(
        length=length,
        lowercase=lowercase,
        uppercase=uppercase,
        numbers=numbers,
        symbols=symbols
    )
    return PasswordResponse(password=password, length=len(password))


# Mount static files and serve index.html at root
app.mount("/static", StaticFiles(directory="../static"), name="static")


@app.get("/")
async def root():
    """Serve the main web interface."""
    return FileResponse("../static/index.html")
