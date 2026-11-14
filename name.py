import hashlib
import json
import uuid
from datetime import datetime, timedelta, timezone
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Pacific Rim International Coin Exchange (PRICE) - Core API",
    description="Headless Transaction, Compliance, Escrow, and Notary Custody Engine",
    version="1.0.0",
)

# =====================================================================
