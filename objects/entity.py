from .maths import Transform, Vector3
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import World

@dataclass
class BaseEntity:
    """A base class for representing Minecraft entities."""

    id: int
    transform: Transform
    world: 'World'

class Player(BaseEntity):
    """A class representing an in-game player entity."""

"""    def __init__(self, id: int):
        super().__init__(
            id= id,
            transform= Transform(Vector3(0,0,0), 0, 0),
            
        )"""
