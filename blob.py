from dataclasses import dataclass


@dataclass
class Blob:
    # Represents component/ labelled area in image
    x: int
    y: int
    width: int
    height: int
    area: int
    density: int
    center_x: int
    center_y: int
