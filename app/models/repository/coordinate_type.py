from sqlalchemy import Column, Integer, String, ForeignKey
from ..provider.engine import Base


class CoordinateType(Base):
    __tablename__ = 'coordinate_type'
    id_coordinate_type = Column('idCoordinateType', Integer, primary_key=True)
    coordinate_type = Column('coordinateType', String(50), nullable=False)
    # bikeway = Column(Integer, ForeignKey('bikeway.idCoordinateType'), nullable=False)
    #whereabouts = Column(Integer, ForeignKey='whereabouts.idCoordinateType')
