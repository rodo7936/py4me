from enum import Enum



class NotificationEnum(str, Enum):
    ALWAYS = 'always'
    WHEN_OFFLINE = 'when_offline'
    NEVER = 'never'