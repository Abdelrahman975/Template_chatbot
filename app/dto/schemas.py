from pydantic import BaseModel, Field
from typing import Optional

class MessageResponse(BaseModel):
    """Generic message response schema"""
    message: str = Field(..., description="Response message")

class ErrorResponse(BaseModel):
    """Error response schema"""
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Error details") 