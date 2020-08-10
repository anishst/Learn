from enum import  Enum

class State(Enum):
    VA = 'Virgina'
    MD = 'Maryland'


va_info = State.VA

print(va_info.value)
print(va_info.name)