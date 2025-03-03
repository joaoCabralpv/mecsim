from enum import Enum
import body

class Mode(Enum):
    DEFAULT=0
    ADD_FORCE_SELECT_OBJECT=1
    ADD_FORCE_CHOSE_VECTOR=2

mode:Mode=Mode.DEFAULT
paused = True

bodyList:list[body.Body] = []
show_forces=True