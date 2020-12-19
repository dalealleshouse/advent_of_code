import re
from functools import reduce
from dataclasses import dataclass, field
from typing import List
from math import prod

PATH = 'day20_input.txt'
TILE_PARSER = re.compile(r'[\d]+')


@dataclass
class Tile:
    # pylint: disable=invalid-name
    id: int
    data: list = field(default_factory=list)

    def edges(self) -> str:
        edges = [
            self.data[0],  # top
            self.data[-1],  # bottom
            ''.join([line[0] for line in self.data]),  # left
            ''.join([line[-1] for line in self.data])]  # right

        # reverse all the strings to account for flipping a tile
        rev = [x[::-1] for x in edges]
        return edges + rev

    def __str__(self):
        tile_data = '\n'.join(self.data)
        return f'tile: {self.id}\n{tile_data}'


@dataclass
class Tiles:
    tiles: List[Tile] = field(default_factory=list)

    def append(self, tile: Tile) -> None:
        self.tiles.append(tile)

    def __getitem__(self, index) -> Tile:
        return self.tiles[index]

    def other_edges(self, tile: Tile) -> List[str]:
        return reduce(list.__add__,
                      [t.edges() for t in self.tiles if t.id != tile.id])

    def mismatched_edges(self, tile: Tile) -> int:
        return len([x for x in tile.edges()
                    if x not in self.other_edges(tile)])

    def corners(self) -> List[Tile]:
        return [tile for tile in self.tiles
                if self.mismatched_edges(tile) == 4]


def parse_file(path=PATH) -> List[Tile]:
    tiles = Tiles()
    tile = None
    mode = 'id'

    with open(path) as file_handle:
        for line in [line.rstrip() for line in file_handle]:
            if mode == 'id':
                match = TILE_PARSER.search(line)
                tile = Tile(int(match[0]))
                mode = 'tile data'
                continue

            if mode == 'tile data':
                if line == '':
                    tiles.append(tile)
                    mode = 'id'
                    continue

                tile.data.append(line)

    tiles.append(tile)
    return tiles


def main():
    tiles = parse_file(PATH)
    ids = [tile.id for tile in tiles.corners()]
    assert len(ids) == 4
    print(f'Product of corner ids = {prod(ids)}')
    # 14986175499719


if __name__ == '__main__':
    main()
