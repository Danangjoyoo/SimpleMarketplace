"""
uWSGI Application Runner
"""
from app import make_app
from dotenv import load_dotenv

load_dotenv("/base/app/.env")
application = make_app()

if __name__ == "__main__":
    application.run()