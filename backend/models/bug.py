from . import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Bug(db.Model):
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=False)
    description = Column(String(500), nullable=False)
    reporter_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    project = relationship('Project')
    reporter = relationship('User')
