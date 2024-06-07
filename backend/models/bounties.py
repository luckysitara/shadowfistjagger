from . import db
from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

class Bounty(db.Model):
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=False)
    amount = Column(Float, nullable=False)
    creator_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    claimed_by = Column(Integer, ForeignKey('user.id'), nullable=True)
    project = relationship('Project')
    creator = relationship('User', foreign_keys=[creator_id])
    claimer = relationship('User', foreign_keys=[claimed_by])
