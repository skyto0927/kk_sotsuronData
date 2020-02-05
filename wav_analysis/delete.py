import matplotlib.font_manager as font_manager
del font_manager.weight_dict['roman']
font_manager._rebuild()