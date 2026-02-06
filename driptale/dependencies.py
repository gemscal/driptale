from driptale.account.service import AccountService, account
from driptale.wardrobe.service import WardrobeService, wardrobe


def get_account_service() -> AccountService:
    """Get the account service."""
    return account


def get_wardrobe_service() -> WardrobeService:
    """Get the wardrobe service."""
    return wardrobe
