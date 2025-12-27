from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/bankdb"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class TransferLimit(Base):
    __tablename__ = "transfer_limits"

    id = Column(Integer, primary_key=True)
    daily_limit = Column(Integer, nullable=False)
    per_transaction_limit = Column(Integer, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
