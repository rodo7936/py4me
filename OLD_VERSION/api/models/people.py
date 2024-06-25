from typing import Optional
from datetime import datetime as dt
from pydantic import BaseModel
from enums import NotificationEnum
from src.api.models.addresses import Address
from src.api.models.attachments import Attachment
from src.api.models.calendars import Calendar
from src.api.models.contacts import Contact
from src.api.models.sites import Site
from src.api.models.ui_extensions import UiExtension


class PersonCreateModel(BaseModel):
    name: str
    custom_fields_attachments: Optional[list[Attachment]] = None
    authenticationID: Optional[str] = None
    auto_translation: Optional[bool] = None
    cost_per_hour: Optional[float] = None
    cost_per_hour_currency: Optional[str] = None  # TODO: Implement currency enum
    custom_fields: Optional[list[dict]] = None
    disabled: Optional[bool] = False
    do_not_translate_languages: Optional[str] = None
    employeeID: Optional[str] = None
    exclude_team_notifications: Optional[bool] = None
    guest: Optional[bool] = None
    information: Optional[str] = None
    information_attachments: Optional[list[Attachment]] = None
    job_title: Optional[str] = None
    locale: Optional[str] = None
    location: Optional[str] = None
    manager: Optional[int] = None
    oauth_person_enablement: Optional[bool] = False
    organization: Optional[int] = None
    picture_uri: Optional[str] = None
    primary_email: Optional[str] = None
    send_email_notificsations: Optional[NotificationEnum] = None
    show_notification_popup: Optional[NotificationEnum] = None
    site: Optional[int] = None
    source: Optional[str] = None
    sourceID: Optional[str] = None
    supportID: Optional[str] = None
    time_format_24h: Optional[bool] = None
    time_zone: Optional[str] = None  # TODO: Implement timezone enum
    vip: Optional[bool] = None
    work_hours: Optional[Calendar] = None


class PersonShortModel(BaseModel):
    id: int
    name: str
    account: Optional[dict] = None
    sourceID: Optional[str] = None
    nodeID: Optional[str] = None


class Person(BaseModel):
    id: int
    name: str
    addresses: Optional[list[Address]] = None
    attachments: Optional[list[Attachment]] = None
    authenticationID: Optional[str] = None
    auto_transaltion: Optional[bool] = None
    contacts: Optional[list[Contact]] = None
    cost_per_hour: Optional[float] = None
    cost_per_hour_currency: Optional[str] = None  # TODO: Implement currency enum
    created_at: Optional[dt] = None
    custom_fields: Optional[list[dict]] = None
    disabled: Optional[bool] = False
    do_not_translate_languages: Optional[str] = None
    employeeID: Optional[str] = None
    exclude_team_notifications: Optional[bool] = None
    guest: Optional[bool] = None
    information: Optional[str] = None
    job_title: Optional[str] = None
    locale: Optional[str] = None
    location: Optional[str] = None
    manager: Optional[PersonShortModel] = None
    oauth_person_enablement: Optional[bool] = None
    organization: Optional['Organization'] = None
    picture_uri: Optional[str] = None
    primary_email: Optional[str] = None
    send_email_notificsations: Optional[NotificationEnum] = None
    show_notification_popup: Optional[NotificationEnum] = None
    site: Optional[Site] = None
    source: Optional[str] = None
    sourceID: Optional[str] = None
    supportID: Optional[str] = None
    time_format_24h: Optional[bool] = None
    time_zone: Optional[str] = None  # TODO: Implement timezone enum
    ui_extension: Optional[UiExtension] = None
    updated_at: Optional[dt] = None
    vip: Optional[bool] = None
    work_hours: Optional[Calendar] = None
