from pydantic import BaseModel
from typing import Optional
from datetime import datetime as dt

from .contacts import Contact
from .people import Person
from .request_templates import RequestTemplate
from .attachments import Attachment
from .addresses import Address
from .ui_extensions import UiExtension
from .accounts import AccountShortModel


class OrganizationShortModel(BaseModel):
    id: int
    name: str
    account: AccountShortModel = None
    sourceID: str = None
    nodeID: str = None


class Organization(BaseModel):
    id: int
    name: str
    addresses: Optional[list[Address]] = None
    attachments: Optional[list[Attachment]] = None
    business_unit: Optional[bool] = None
    business_unit_organization: Optional[OrganizationShortModel] = None
    contacts: Optional[list[Contact]] = None
    created_at: Optional[dt] = None
    custom_fields: Optional[list[dict]] = None
    disabled: Optional[bool] = None
    financialID: Optional[str] = None
    manager: Optional[Person] = None
    order_template: Optional[RequestTemplate] = None
    parent: Optional[OrganizationShortModel] = None
    picture_uri: Optional[str] = None
    region: Optional[str] = None
    remarks: Optional[str] = None
    source: Optional[str] = None
    sourceID: Optional[str] = None
    substitute: Optional[Person] = None
    ui_extension: Optional[UiExtension] = None
    updated_at: Optional[dt] = None


class OrganizationCreateModel(BaseModel):
    name: str
    business_unit: Optional[bool] = False
    custom_fields: Optional[list[dict]] = None
    custom_fields_attachments: Optional[list[Attachment]] = None
    disabled: Optional[bool] = False
    financialID: Optional[str] = None
    manager: Optional[int] = None
    order_template: Optional[int] = None
    parent: Optional[int] = None
    picture_uri: Optional[str] = None
    region: Optional[str] = None
    remarks: Optional[str] = None
    remarks_attachments: Optional[list[Attachment]] = None
    source: Optional[str] = None
    sourceID: Optional[str] = None
    substitute: Optional[int] = None
