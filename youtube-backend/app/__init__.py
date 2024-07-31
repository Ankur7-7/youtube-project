from app.routes.index_routes import index
from app.routes.glue_routes import glue

from .app import app

app.register_blueprint(index)
app.register_blueprint(glue)
