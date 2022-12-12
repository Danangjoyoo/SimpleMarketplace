"""
uWSGI Application Runner
"""
from app import make_app

if __name__ == "__main__":
    application = make_app("/base/app/.env")
    application.run()