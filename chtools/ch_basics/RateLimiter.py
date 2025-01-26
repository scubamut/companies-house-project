from chtools.ch_utils import setup_logging, get_api_key
from chtools.ch_basics import Config, APIResponse

import logging
import time
from datetime import datetime, timedelta
from collections import deque

# logger = setup_logging
# api_key = get_api_key

class RateLimiter:

    """Implements rate limiting for API requests."""
    
    def __init__(self, max_requests: int, time_window: int, logger: logging.Logger):
        self.max_requests = max_requests
        self.time_window = time_window
        self.logger = logger  # Add logger as instance variable
        self.requests: deque = deque()
    
    def can_make_request(self) -> bool:
        now = datetime.utcnow()
        while self.requests and self.requests[0] < now - timedelta(seconds=self.time_window):
            self.requests.popleft()
        
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False
    
    def wait_if_needed(self) -> int:
        current_requests = len(self.requests)
        if current_requests >= self.max_requests:
            self.logger.info(f"Rate limit reached. Current requests in window: {current_requests}")
        
        while not self.can_make_request():
            self.logger.debug(f"Waiting for rate limit. Current requests: {len(self.requests)}")
            time.sleep(1)
        
        current_requests = len(self.requests)
        self.logger.debug(f"Request allowed. Current requests in window: {current_requests}")
        return current_requests