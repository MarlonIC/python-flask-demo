from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CoordinateType(Base):
    __tablename__ = 'coordinate_type'
    id_coordinate_type = Column('idCoordinateType', Integer, primary_key=True)
    coordinate_type = Column('coordinateType', String(50), nullable=False)
    whereabouts = Column(Integer, ForeignKey='whereabouts.idCoordinateType')
