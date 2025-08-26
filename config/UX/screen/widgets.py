from config.data.main import *
#? boxes in the x way

from config.data.main import *

def centralize(parent_container, *items, axis="x"):
    valid_items = [i for i in items if hasattr(i, "_current_width") and hasattr(i, "_current_height")]
    if not valid_items:
        return []

    if (hasattr(parent_container, "_current_height") and 
        hasattr(parent_container, "_current_width") and
        parent_container._current_height > 0 and
        parent_container._current_width > 0):
        
        if parent_container._current_height > parent_container._current_width:
            axis = "y" if axis == "x" else "x"

    if axis == "x":
        total_width = sum(i._current_width for i in valid_items)
        remaining = max(parent_container._current_width - total_width, 0)
        if len(valid_items) == 1:
            return [remaining // 2]
        spacing = remaining // (len(valid_items) + 1)
        return [spacing for _ in valid_items]

    elif axis == "y":
        total_height = sum(i._current_height for i in valid_items)
        remaining = max(parent_container._current_height - total_height, 0)
        if len(valid_items) == 1:
            return [remaining // 2]
        spacing = remaining // (len(valid_items) + 1)
        return [spacing for _ in valid_items]

    else:
        raise ValueError("axis deve ser 'x' ou 'y'")

def items_return(parent_container):
    return len(list(parent_container.winfo_children()))

def theme_getter(radio_var):
    data = read_data()
    value_taken = data["data"]["user"]["theme"]
    return radio_var.set(value_taken)
def items_return(parent_container):
    return len(list(parent_container.winfo_children()))
def theme_getter(radio_var):
    data = read_data()
    value_taken = data["data"]["user"]["theme"]
    return radio_var.set(value_taken)