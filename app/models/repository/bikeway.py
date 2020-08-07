from sqlalchemy import Column, Integer, String, Unicode, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..provider.engine import Base


class Bikeway(Base):
    __tablename__ = 'bikeway'
    id_bikeway = Column('idBikeway', Integer, primary_key=True)
    name = Column('name', String(100), nullable=False)
    characteristic = Column('characteristic', String(150))
    type_segregation = Column('typeSegregation', String(100))
    type_bikeway = Column('typeBikeWay', String(100), nullable=False)
    id_district = Column('idDistrict', Integer, nullable=False)
    id_province = Column('idProvince', Integer, nullable=False)
    id_departament = Column('idDepartament', Integer, nullable=False)
    location = Column('location', String(150))
    description = Column('description', Unicode(200))
    length = Column('length', String(50))
    coordinates = Column('coordinates', Unicode(500))
    temporary = Column('temporary', Boolean)
    id_coordinate_type = Column('idCoordinateType', Integer, ForeignKey('coordinate_type.idCoordinateType'),
                                nullable=False)
    coordinate_type = relationship('CoordinateType')
