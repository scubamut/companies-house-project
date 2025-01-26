# Data Models
class RegisteredOffice(BaseModel):
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    locality: Optional[str] = None
    postal_code: Optional[str] = None