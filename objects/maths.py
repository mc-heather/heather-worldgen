import math

class Vector2:
    """A class representing a point on a 2D plain."""

    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def distance(self, pos: 'Vector2') -> float:
        """Returns the distance between 2 points (using pythagoras)."""

        return math.sqrt(((self.x - pos.x) ** 2) + ((self.y - pos.y) ** 2))
    
    def __eq__(self, o: 'Vector2') -> bool:
        return self.x == o.x and self.y == o.y

class Vector3:
    """A class representing a point on a 3D space."""

    __slots__ = ("x", "y", "z")

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def distance(self, pos: 'Vector3') -> float:
        """Calculates the straight line distance between 2 3D points using
        3D Pythagoras."""

        return math.sqrt(
            ((self.x - pos.x) ** 2)
            + ((self.y - pos.y) ** 2)
            + ((self.z - pos.z) ** 2)
        )
    
    def __hash__(self) -> int:
        """Treates a unique integer from the values in the vector."""

        return int(f"{self.x}{self.y}{self.z}")
    
    def __eq__(self, o: 'Vector3') -> bool:
        return self.x == o.x and self.y == o.y and self.z == o.z

class Transform:
    """Represents the precise position, orientation etc of an object."""

    __slots__ = ("pos", "yaw", "pitch")

    def __init__(self, pos: Vector3, yaw: float, pitch: float) -> None:
        self.pos = pos
        self.yaw = yaw
        self.pitch = pitch
    
    def __eq__(self, o: 'Transform') -> bool:
        return self.pos == o.pos and self.yaw == o.yaw and self.pitch == o.pitch
