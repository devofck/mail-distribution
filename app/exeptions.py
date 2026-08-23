

class InvalidPhotoLinkFormat(Exception):
    def __init__(
            self,
            msg = "Unsupported Photo Link Format\n"
                  "Use direct link to the photo\n"
                  "Supported Formats: png, jpg, jpeg, gif"
    ):
        self.msg = msg
        super().__init__(self.msg)

class InvalidTelegramText(Exception):
    def __init__(
            self,
            msg = "Text length must be bigger than 1 and less then 4096\n"
                  "Of course, this is a Telegram limitation."
    ):
        self.msg = msg
        super().__init__(self.msg)


class InvalidInlineMarkupJSON(Exception):
    def __init__(
            self,
            msg = "Unsupported Inline Markup Format\n",
            additional_data: str = ""
    ):
        self.msg = msg + '\nMore details: ' + additional_data
        super().__init__(self.msg)