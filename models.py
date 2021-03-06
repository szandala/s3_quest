from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    # this one should be normalized...
    address = Column(String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }
