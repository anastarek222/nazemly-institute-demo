"""Vercel demo adapter for the original Nazemly Python HTTP app.

SQLite is transient on Vercel. This deployment is for the institute demo only.
"""
import os
import sys
import zipfile
from pathlib import Path

archive = Path(__file__).resolve().parent.parent / "source.zip"
app_root = Path("/tmp/nazemly-institute-demo-source")
if not (app_root / "app" / "server.py").is_file():
    app_root.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as bundle:
        bundle.extractall(app_root)

admin_password = os.environ.get("NAZEMLY_ADMIN_PASSWORD", "")
employee_password = os.environ.get("NAZEMLY_EMPLOYEE_PASSWORD", "")
if len(admin_password) < 14 or len(employee_password) < 14 or admin_password == employee_password:
    raise RuntimeError("Set two distinct private demo passwords, at least 14 characters each.")

os.environ["HR_DB_PATH"] = "/tmp/nazemly-institute-demo-db/hr.sqlite3"
os.environ["HR_DEMO_MODE"] = "1"
os.environ["HR_SEED_EXAMPLES"] = "1"
os.environ["NAZEMLY_CLOUD_DEMO"] = "1"
sys.path.insert(0, str(app_root / "app"))

import server
import demo_seed
from common import cairo_today
from storage import db

server.init()
with db() as connection:
    demo_seed.seed(connection, cairo_today())

class handler(server.Handler):
    pass
