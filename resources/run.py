from db import db
from app_flask_restful import app

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.run(port=4998, debug=True)