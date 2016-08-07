from app.server import app
from app.database import DB

if __name__ == "__main__":
    db = DB("hfa_events_dev")
    db.init_db()
    app.config.update({"db": db})
    app.run()

