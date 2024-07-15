from datetime import datetime
import databases
import sqlalchemy
from settings import settings
from models.order import Status

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("userid", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("firstname", sqlalchemy.String(32)),
    sqlalchemy.Column("lastname", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128))
    )

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("productid", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("price", sqlalchemy.Float)
    )

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("orderid", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("userid", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.userid"), nullable=False),
    sqlalchemy.Column("productid", sqlalchemy.Integer, sqlalchemy.ForeignKey("products.productid"), nullable=False),
    sqlalchemy.Column("create_data", sqlalchemy.DateTime, default=datetime.today()),
    sqlalchemy.Column("status", sqlalchemy.Enum(Status, name='status'))
    )

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) 
metadata.create_all(engine)
