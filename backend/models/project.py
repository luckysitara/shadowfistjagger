from . import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Project(db.Model):
    id = Column(Integer, primary_key=True)
    project_id = Column(String(80), unique=True, nullable=False)
    details = Column(String(500), nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    owner = relationship('User')
