from sqlalchemy import Column, Integer, String
from app.db import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="open")
    
class Notification(Base): 
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    message = Column(String)