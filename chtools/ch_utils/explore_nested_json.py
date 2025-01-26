def explore_nested_json(data, prefix=None, sep='.'):
    """
    Recursively explore nested JSON and return flattened key-value pairs
    with hierarchical keys that can be used as multi-index
    """
    items = {}

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{prefix}{sep}{key}" if prefix else key
            if isinstance(value, (dict, list)):
                items.update(explore_nested_json(value, new_key, sep))
            else:
                items[new_key] = value

    elif isinstance(data, list):
        for i, value in enumerate(data):
            new_key = f"{prefix}{sep}{i}" if prefix else str(i)
            if isinstance(value, (dict, list)):
                items.update(explore_nested_json(value, new_key, sep))
            else:
                items[new_key] = value

    return items