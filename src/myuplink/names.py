"""Methods for getting names etc from API data."""
import re
from .models import Device, System


MAP_NIBEF = {"manufacturer": "Nibe", "series": "F"}
MAP_NIBES = {"manufacturer": "Nibe", "series": "S"}
NAME_MAP = {
    "F1145": MAP_NIBEF,
    "F1155": MAP_NIBEF,
    "F1245": MAP_NIBEF,
    "F1255": MAP_NIBEF,
    "F1345": MAP_NIBEF,
    "F1355": MAP_NIBEF,
    "F370": MAP_NIBEF,
    "F470": MAP_NIBEF,
    "F730": MAP_NIBEF,
    "F750": MAP_NIBEF,
    "SMO20": MAP_NIBEF,
    "SMO 20": MAP_NIBEF,
    "SMO40": MAP_NIBEF,
    "SMO 40": MAP_NIBEF,
    "VVM225": MAP_NIBEF,
    "VVM310": MAP_NIBEF,
    "VVM320": MAP_NIBEF,
    "VVM325": MAP_NIBEF,
    "VVM500": MAP_NIBEF,
    "S1155": MAP_NIBES,
    "S1255": MAP_NIBES,
    "S1256": MAP_NIBES,
    "S320": MAP_NIBES,
    "S325": MAP_NIBES,
    "S735": MAP_NIBES,
    "S2125": MAP_NIBES,
    "SMOS40": MAP_NIBES,
    "SMOS 40": MAP_NIBES,
}


def get_system_name(system: System) -> str | None:
    """Return system name."""
    return system.name


def get_manufacturer(device: Device) -> str | None:
    """Return manufacturer name."""
    for model, data in NAME_MAP.items():
        if re.search(model, device.product_name):
            return data.get("manufacturer")

    return device.productName.split()[0]


def get_model(device: Device) -> str | None:
    """Return model name."""
    for model in NAME_MAP:
        if re.search(model, device.product_name):
            return model
    name_list = device.product_name.split()
    if len(name_list == 0):
        model = name_list[0]
    else:
        model = " ".join(name_list[1:])
    return model


def get_series(device: Device) -> str | None:
    """Return product series."""
    for model, data in NAME_MAP.items():
        if re.search(model, device.product_name):
            return data.get("series")

    return None
