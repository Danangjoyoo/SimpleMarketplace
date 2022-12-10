"""
Query Init File
"""
from sqlalchemy.engine.row import Row


def meta_object_to_dict(instance):
    """
    Convert query data to dict

    Params:
        - instance (SQLAlchemy Meta Instance)

    Returns:
        - data (dict)
    """
    attributes = [
        key for key in vars(instance.__class__).keys()
        if "_" not in [key[0], key[-1]]
    ]
    data = {attr: getattr(instance, attr) for attr in attributes}

    return data


def as_dict(instance):
    """
    convert query result as a dict

    Args:
        - instance (query or list query): single or multiple query result object

    Return:
        - mapped_object (List[Dict[str, Any]] or Dict[str, Any])
    """
    # multiple instance in list or tuple
    if isinstance(instance, list):
        mapped_object = []
        for _object in instance:
            if isinstance(_object, Row):
                mapped_object.append(_object._asdict())
            else:
                mapped_object.append(meta_object_to_dict(_object))

    # single object
    else:
        if isinstance(instance, Row):
            mapped_object = instance._asdict()
        else:
            mapped_object = meta_object_to_dict(instance)

    return mapped_object