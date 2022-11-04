from dataclasses import dataclass


@dataclass
class Sound:
    # Represents an individual sound in a 4 beat bar
    frequency: int
    amplitude: int
    duration: int
    offset: int
    decreasing: bool
    volume: float
