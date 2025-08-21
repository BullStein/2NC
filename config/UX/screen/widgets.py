def ycentralize(parent_container,current_container):
    value = (parent_container._current_height - current_container._current_height) // 2
    return value

def xcentralize(parent_container, *items):
    total_width_items = sum(i._current_width for i in items)
    remaining_space = parent_container._current_width - total_width_items
    if remaining_space < 0:
        remaining_space = 0
    if len(items) > 1:
        spacing = remaining_space // (len(items) + 1)
    else:
        spacing = remaining_space // 2
    return spacing,0

def items_return(parent_container):
    return len(list(parent_container.winfo_children()))
