from dataclasses import dataclass
from typing import Optional
from .maths import Transform, Vector3
from ..constants.world import Biomes, Weather
import logging

CHUNK_X = 16
CHUNK_Y = 256
CHUNK_Z = 16

@dataclass
class Block:
    """Represents a singular in-game block."""

    id: int
    position: Vector3
    biome: Biomes

@dataclass
class Chunk:
    """An object representing a group of blocks."""

    position: Vector3
    blocks: dict[Vector3, Block]

    def set_block_relative(self, pos: Vector3, block: Block) -> None:
        """Sets a block at a given position relative to the position in the chunk.
        
        Note:
            NO CHECKS ARE PERFORMED ON WHETHER THE BLOCK IS PART OF CHUNK. CLAMPING
                IS RECOMMENDED.
        """

        self.blocks[pos] = block
    
    def get_block_relative(self, pos: Vector3) -> Optional[Block]:
        """Attempts to fetch a block from a position relative to the chunk."""

        return self.blocks.get(pos)
    
    def pos_to_relative(self, pos: Vector3, validate: bool = False) -> Vector3:
        """Converts a coordinate to a chunk relative position.
        
        Args:
            validate (bool): Whether to check if the position is a real relative pos.
                If isnt, raises `ValueError`.
        """

        sub_x = CHUNK_X * self.position.x
        sub_z = CHUNK_Z * self.position.z

        rel_pos = Vector3(
            pos.x - sub_x,
            pos.y,
            pos.z - sub_z
        )

        if validate and (rel_pos.x < 0 or rel_pos.z < 0):
            raise ValueError("Relative pos validation: Position is outside chunk!")
        
        return rel_pos
    
    def relative_to_pos(self, pos: Vector3) -> Vector3:
        """Converts a chunk relative position to a real coordinate."""

        sub_x = CHUNK_X * self.position.x
        sub_z = CHUNK_Z * self.position.z

        return Vector3(
            pos.x + sub_x, pos.y, pos.z + sub_z
        )
    
    def set_block(self, pos: Vector3, block: Block) -> None:
        """Sets a block at a given coordinate relative to (0, 0)."""

        self.set_block_relative(self.pos_to_relative(pos), block)
    
    def get_block(self, pos: Vector3) -> Optional[Block]:
        """Gets a block from a world coordinate."""

        return self.get_block_relative(self.pos_to_relative(pos))
    
    # Debug generation.
    @classmethod
    def gen_void(cls, pos: Vector3) -> 'Chunk':
        """Generates a void chunk."""
        blocks = {}
        for y in range(CHUNK_Y):
            for x in range(CHUNK_X):
                for z in range(CHUNK_Z):
                    pos = Vector3(x, y, z)
                    blocks[pos] = Block(
                        id= 0,
                        position= pos,
                        biome= Biomes.PLAINS,
                    )

@dataclass
class World:
    """A class representing a Minecraft World."""

    name: str
    spawn_pos: Transform
    weather: Weather
