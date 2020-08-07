from sqlalchemy import Column, Integer, String, Unicode
from sqlalchemy.orm import relationship
from ..provider.engine import Base


class Whereabout(Base):
    __tablename__ = 'whereabouts'
    id_whereabouts = Column('idWhereabouts', Integer, primary_key=True)
    name = Column('name', String(100), nullable=False)
    location = Column('location', String(150))
    schedule = Column('schedule', String(100))
    bicycles_available = Column('bicyclesAvailable', Integer, nullable=False)
    coordinates = Column('coordinates', Unicode(500))
    coordinate_type = relationship('CoordinateType')
