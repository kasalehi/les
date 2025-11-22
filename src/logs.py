import sys
import logging

from pathlib import Path

file_path=Path(__file__).parent.parent / "logs" / "app.log"
file_path.parent.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=file_path,
    force=True
)
logger = logging.getLogger("app_logger")
    
