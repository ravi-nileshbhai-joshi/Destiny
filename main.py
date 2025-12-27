from functions import recommend
from ui import get_name, get_state, display_result

name = get_name()
energy, focus = get_state(name)
result = recommend(energy, focus)
display_result(name,result)
