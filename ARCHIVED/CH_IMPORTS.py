from __future__ import annotations

import base64
import getpass
import logging
import os
import time  # Add time module import
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, List, Any
from collections import deque

import pandas as pd
import requests
from pydantic import BaseModel, Field
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry