from app.db.database import Base, engine
from app.models.user import User
from app.models.item import Item

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Done.")


