"""Pacific Rim Coin Exchange - core API (starter).

Separate platform from Pacific Rim Auctions. Nothing here connects to the
Auctions platform, its database, or its bank account.

The bank rail is OFF by default. Nothing can move money until the
environment variable BANK_RAIL_ENABLED is set to "true" in Render's dashboard.
Account details are read from environment variables only. They never go in
this code or in GitHub.
"""

import os
from datetime import datetime, timezone

from fastapi import FastAPI

PLATFORM_ID = "pacific-rim-coin-exchange"
VERSION = "0.1.0"


def _env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def _mask(value: str) -> str:
    """Show only the last 4 characters of a sensitive value."""
    if not value:
        return "not set"
    return "*" * max(len(value) - 4, 0) + value[-4:]


def _bank_rail_enabled() -> bool:
    return _env("BANK_RAIL_ENABLED", "false").lower() == "true"


app = FastAPI(
    title="Pacific Rim Coin Exchange - Core API",
    description="Separate platform under the Pacific Rim Auctions umbrella.",
    version=VERSION,
)


@app.get("/")
def root():
    return {
        "platform": PLATFORM_ID,
        "message": "Pacific Rim Coin Exchange is running.",
        "version": VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "platform": PLATFORM_ID,
        "time_utc": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/v1/status")
def status():
    return {
        "platform": PLATFORM_ID,
        "version": VERSION,
        "bank_rail": {
            "enabled": _bank_rail_enabled(),
            "settlement_bank": _env("SETTLEMENT_BANK_NAME", "Kauai Federal Credit Union"),
            "settlement_account": _mask(_env("SETTLEMENT_ACCOUNT_REF")),
        },
    }
