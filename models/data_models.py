import logging
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

@dataclass
class CustomerSignupData:
    first_name: str
    last_name: str
    country: str
    phone: str
    email: str
    password: str

@dataclass
class CustomerLoginData:
    email: str
    password: str