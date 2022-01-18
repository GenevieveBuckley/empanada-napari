import os

__all__ = [
    'get_configs',
]

def get_configs():
    # get dict of all model configs
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configs')
    model_configs = {}
    for fn in os.listdir(config_path):
        if fn.endswith('.yaml'):
            model_configs[fn[:-len('.yaml')]] = os.path.join(config_path, fn)

    empanada_path = os.path.join(os.path.expanduser('~'), '.empanada/configs')
    if os.path.isdir(empanada_path):
        for fn in os.listdir(empanada_path):
            if fn.endswith('.yaml'):
                model_configs[fn[:-len('.yaml')]] = os.path.join(empanada_path, fn)

    return model_configs
