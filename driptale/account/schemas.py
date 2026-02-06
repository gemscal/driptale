from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AccountBase(BaseModel):
    """Base account schema with common fields."""

    display_name: Optional[str] = Field(None, description="User's display name")
    email: str = Field(..., description="User's email address")
    avatar_url: Optional[str] = Field(None, description="URL to user's avatar image")
    bio: Optional[str] = Field(None, description="User's bio/description")
    is_active: bool = Field(True, description="Whether the account is active")
    is_onboarded: bool = Field(False, description="Whether the account is onboarded")


class AccountCreate(AccountBase):
    """Schema for creating a new account."""

    firebase_uid: str = Field(..., description="Firebase user ID")
    email: str = Field(..., description="User's email address")


class AccountUpdate(BaseModel):
    """Schema for updating account information."""

    display_name: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    is_active: Optional[bool] = None


class AccountResponse(AccountBase):
    """Schema for account response."""

    id: str = Field(..., description="Account document ID")
    firebase_uid: str = Field(..., description="Firebase user ID")
    stripe_customer_id: Optional[str] = Field(
        None, description="Stripe customer ID for payments"
    )
    subscription_status: Optional[str] = Field(
        None, description="Current subscription status (active, canceled, etc.)"
    )
    subscription_tier: Optional[str] = Field(
        None, description="Subscription tier (free, premium, etc.)"
    )
    character_model_id: Optional[str] = Field(
        None, description="Reference to user's character model"
    )
    wardrobe_size: int = Field(
        0, description="Number of clothing items in user's wardrobe"
    )
    album_count: int = Field(0, description="Number of wishlist albums created")
    preferences: Optional[dict] = Field(
        None,
        description="User preferences (style preferences, sizing, etc.)",
    )
    created_at: datetime = Field(..., description="Account creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    last_login_at: Optional[datetime] = Field(None, description="Last login timestamp")
