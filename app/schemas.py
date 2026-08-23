from exeptions import InvalidPhotoLinkFormat, InvalidTelegramText, InvalidInlineMarkupJSON
from typing import Literal
import json
from pydantic import BaseModel, field_validator




class CreateTelegramBroadcastQuery(BaseModel):
    mail_text: str
    parse_mode: Literal["markdown", "HTML"]
    inline_markup: str
    image_url: str
    audience: list
    @field_validator("image_url")
    @classmethod
    def image_url_validator(cls, v):
        accepted_formats = ("png", "jpg", "jpeg", "webp")
        if not v.startswith("https") and not v.endswith(accepted_formats):
            return v
        raise InvalidPhotoLinkFormat()

    @field_validator("mail_text")
    @classmethod
    def mail_text_validator(cls, v):
        if 1 < len(v) < 4096:
            return v
        raise InvalidTelegramText()

    @field_validator('inline_markup')
    @classmethod
    def validate_inline_markup(cls, v: str) -> str:
        if not v or v == '{}':
            return ''

        try:
            data = json.loads(v)
        except json.JSONDecodeError:
            raise InvalidInlineMarkupJSON(..., 'Invalid JSON structure')

        if 'inline_keyboard' not in data:
            raise InvalidInlineMarkupJSON(..., 'Must contain inline_keyboard')

        for row in data['inline_keyboard']:
            for button in row:
                if 'url' not in button:
                    raise InvalidInlineMarkupJSON(..., 'Must contain url')

                if not button['url'].startswith(('http://', 'https://')):
                    raise InvalidInlineMarkupJSON(..., 'Invalid URL, use http:// or https://')

        return v


class CreateEmailBroadcastQuery(BaseModel):
    mail_text: str
    mail_subject: str
