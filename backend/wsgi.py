"""
uWSGI Application Runner
"""
from app import make_app

application = make_app("/base/app/.env")

if __name__ == "__main__":
    application.run()