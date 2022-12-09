### DON'T CHANGE THIS SECTION
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

database_url = "sqlite:///app.db"
engine = create_engine(database_url)

## DON'T USE DIFFERENT ENGINE BASE
Base = declarative_base()


## Your Models Dependencies
from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


# Please put your tables below using the defined Base
from typing import Optional
from sqlalchemy import (
    Column,
    Boolean,
    ForeignKey,
    Integer,
    Float,
    String,
    DateTime,
    Enum,
    INTEGER,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

# ----------------- MISC -----------------


class ProviderTypeEnum(str, enum.Enum):
    personal = "personal"
    business = "business"


class CustomerTypeEnum(str, enum.Enum):
    personal = "personal"
    business = "business"


class ProductStatusEnum(str, enum.Enum):
    uploaded = "uploaded"
    reviewed = "reviewed"
    rejected = "rejected"
    approved = "approved"
    disabled = "disabled"
    paused = "paused"


class RoleTypeEnum(str, enum.Enum):
    backoffice = "backoffice"
    customer = "customer"
    provider = "provider"


class AddressTypeEnum(str, enum.Enum):
    entity = "entity"
    billing = "billing"


class EndpointComponentDataTypeEnum(str, enum.Enum):
    integer = "integer"
    string = "string"
    enum = "enum"
    number = "number"
    boolean = "boolean"
    time_24_hour = "time (24-hour) HH:MM"
    date = "date (YYYY-MM-DD)"
    array = "array"


class EndpointStatusEnum(str, enum.Enum):
    private = "private"
    public = "public"


class EndpointMethodEnum(str, enum.Enum):
    get = "get"
    post = "post"
    put = "put"
    delete = "delete"
    patch = "patch"


class EndpointBodyContentTypeEnum(str, enum.Enum):
    json = "application/json"
    # xml = "application/xml"
    # textplain = "text/plain"
    # octet_stream = "application/octet-stream"
    # form = "form-data"
    multipart = "multipart/form-data"


# ----------------- SQL MODEL -----------------


class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    iso3 = Column(String(100))
    phonecode = Column(Integer)


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=True)
    country = relationship("Country")
    full_address = Column(String(300), nullable=False)
    provider_id = Column(Integer, ForeignKey("provider.id"), nullable=True)
    provider = relationship("Provider")
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=True)
    customer = relationship("Customer")
    type = Column(Enum(AddressTypeEnum), nullable=False)


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True, index=True)


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(40), unique=False, index=False, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    avatar = Column(String(300), nullable=True, default="")
    phone = Column(String(18), nullable=True, default="")
    phone_added = Column(DateTime, nullable=True, default=None)
    created = Column(DateTime, nullable=False, default=datetime.now())


class UserAlias(Base):
    __tablename__ = "userAlias"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    profile_id = Column(Integer, ForeignKey("profile.id"), unique=True, nullable=False)
    profile = relationship("Profile")


class Provider(Base):
    __tablename__ = "provider"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    logo_link = Column(String(300), nullable=False)
    name = Column(String(100), nullable=False)
    type = Column(Enum(ProviderTypeEnum))
    created = Column(DateTime, nullable=False, default=datetime.now())


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    logo_link = Column(String(300), nullable=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    short_desc = Column(String(400), nullable=False)
    tnc = Column(Text, nullable=True)
    base_url = Column(String(300), nullable=False)
    link_openapi = Column(String(300), nullable=False)
    need_hardware = Column(Boolean, default=False)
    total_star = Column(Integer, default=0)
    total_reviewer = Column(Integer, default=0)
    star_usefull = Column(Integer, default=0)
    star_user_friendly = Column(Integer, default=0)
    star_performance = Column(Integer, default=0)
    star_reliability = Column(Integer, default=0)
    created = Column(DateTime, nullable=False, default=datetime.now())
    status = Column(
        Enum(ProductStatusEnum), nullable=False, default=ProductStatusEnum.uploaded
    )
    category_id = Column(
        Integer,
        ForeignKey("category.id"),
        nullable=False,
    )
    category = relationship("Category")
    provider_id = Column(
        Integer,
        ForeignKey("provider.id"),
        nullable=False,
    )
    provider = relationship("Provider")


class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30), unique=False, nullable=False)
    entity_id = Column(Integer, nullable=False)
    entity_type = Column(Enum(RoleTypeEnum))
    level = Column(Integer, nullable=False)
    __table_args__ = (
        UniqueConstraint(
            "name", "entity_id", "entity_type", name="_role_per_entity_uc"
        ),
    )


class Action(Base):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), unique=True, nullable=False)
    backoffice_min_level = Column(Integer, nullable=False)
    customer_min_level = Column(Integer, nullable=False)
    provider_min_level = Column(Integer, nullable=False)
    policy = Column(Text, nullable=True)


class RoleHasAction(Base):
    __tablename__ = "role_has_action"
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False, primary_key=True)
    role = relationship("Role")
    action_id = Column(
        Integer, ForeignKey("action.id"), nullable=False, primary_key=True
    )
    action = relationship("Action")


class UserHasRole(Base):
    __tablename__ = "user_has_role"
    uid = Column(Integer, ForeignKey("userAlias.id"), nullable=False, primary_key=True)
    user = relationship("UserAlias")
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False, primary_key=True)
    role = relationship("Role")
    created = Column(DateTime, nullable=False, default=datetime.now())


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ektp_link = Column(String(300), nullable=True)
    type = Column(Enum(CustomerTypeEnum), nullable=False)
    created = Column(DateTime, default=datetime.now())


class Endpoint(Base):
    __tablename__ = "endpoint"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False, index=True)
    product = relationship("Product")
    title = Column(String(100), nullable=False)
    description = Column(String(300), nullable=True)
    base_path = Column(String(300), nullable=False)
    method = Column(Enum(EndpointMethodEnum), nullable=False)
    price = Column(Integer, nullable=False, default=0)
    status = Column(
        Enum(EndpointStatusEnum), nullable=False, default=EndpointStatusEnum.private
    )
    latency = Column(Float(asdecimal=True, decimal_return_scale=100), nullable=True)
    sla = Column(Float(asdecimal=True, decimal_return_scale=10), nullable=True)


class EndpointPath(Base):
    __tablename__ = "endpoint_path"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoint.id"), index=True, nullable=False)
    endpoint = relationship("Endpoint")
    name = Column(String(100), nullable=False)
    data_type = Column(
        Enum(EndpointComponentDataTypeEnum),
        nullable=False,
        default=EndpointComponentDataTypeEnum.string,
    )
    required = Column(Boolean, nullable=False, default=True)
    index = Column(Integer, nullable=False)
    enums_value = Column(String(300), nullable=True, default=None)


class EndpointHeader(Base):
    __tablename__ = "endpoint_header"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoint.id"), index=True, nullable=False)
    endpoint = relationship("Endpoint")
    name = Column(String(100), nullable=False)
    data_type = Column(
        Enum(EndpointComponentDataTypeEnum),
        nullable=False,
        default=EndpointComponentDataTypeEnum.string,
    )
    required = Column(Boolean, nullable=False, default=False)
    enums_value = Column(String(300), nullable=True, default=None)


class EndpointQuery(Base):
    __tablename__ = "endpoint_query"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoint.id"), index=True, nullable=False)
    endpoint = relationship("Endpoint")
    name = Column(String(100), nullable=False)
    data_type = Column(
        Enum(EndpointComponentDataTypeEnum),
        nullable=False,
        default=EndpointComponentDataTypeEnum.string,
    )
    required = Column(Boolean, nullable=False, default=False)
    enums_value = Column(String(300), nullable=True, default=None)


class EndpointBody(Base):
    __tablename__ = "endpoint_body"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    endpoint_id = Column(Integer, ForeignKey("endpoint.id"), index=True, nullable=False)
    endpoint = relationship("Endpoint")
    value = Column(String(3000), nullable=False)
    content_type = Column(
        Enum(EndpointBodyContentTypeEnum),
        nullable=False,
        default=EndpointBodyContentTypeEnum.json,
    )
    required = Column(Boolean, nullable=False, default=True)
