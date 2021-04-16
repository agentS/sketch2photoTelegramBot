from enum import IntEnum

class BotConversationStates(IntEnum):
    RECEIVE_SKETCH = 0
    SEND_PHOTO = 1
    RECEIVE_PHOTO = 10
    SEND_SKETCH = 11
    SUCCESS = 95
    END = 99
