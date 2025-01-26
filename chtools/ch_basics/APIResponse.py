from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any

class APIResponse(BaseModel):
    items: List[Dict[str, Any]]
    total_results: Optional[int] = None
    page_number: Optional[int] = None
    kind: Optional[str] = None