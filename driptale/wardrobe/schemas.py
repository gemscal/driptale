from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class WardrobeCreate(BaseModel):
    """User only provides these fields"""

    name: str = Field(..., description="Name of the wardrobe")
    description: Optional[str] = Field(None, description="Description of the wardrobe")
    image_url: Optional[str] = Field(None, description="Image URL of the wardrobe")


class WardrobeUpdate(BaseModel):
    """User only provides fields to update"""

    name: Optional[str] = Field(None, description="Name of the wardrobe")
    description: Optional[str] = Field(None, description="Description of the wardrobe")
    image_url: Optional[str] = Field(None, description="Image URL of the wardrobe")


class WardrobeResponse(BaseModel):
    """Response includes everything, including what the service added"""

    id: str = Field(..., description="Wardrobe document ID")
    name: str = Field(..., description="Name of the wardrobe")
    description: Optional[str] = Field(None, description="Description of the wardrobe")
    image_url: Optional[str] = Field(None, description="Image URL of the wardrobe")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
