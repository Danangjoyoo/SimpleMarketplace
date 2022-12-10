"""
SQL Models
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Image(Base):
    __tablename__ = "image"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    url = Column(String(500), nullable=False)


class Image_Collection(Base):
    __tablename__ = "image_collection"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)


class Image_Collection_Link(Base):
    __tablename__ = "image_collection_link"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    image_collection_id = Column(Integer, ForeignKey("image_collection.id", ondelete="CASCADE"), nullable=False)
    image_id = Column(Integer, ForeignKey("image.id", ondelete="CASCADE"), nullable=False)


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, default="", nullable=True)
    images = Column(Integer, ForeignKey("image_collection.id", ondelete="CASCADE"), nullable=True)
    logo_id = Column(Integer, ForeignKey("image.id", ondelete="CASCADE"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=func.now(), nullable=False)


class Variant(Base):
    __tablename__ = "variant"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    size = Column(String(50), nullable=False)
    color = Column(String(20), nullable=False)
    images = Column(Integer, ForeignKey("image_collection.id", ondelete="CASCADE"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=func.now(), nullable=False)
