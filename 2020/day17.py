from dataclasses import dataclass, field
from abc import abstractmethod
from typing import List
from itertools import product

ACTIVE = '#'
INACTIVE = '.'


class AbstractConwayCube():
    state: str

    def __init__(self, state: str):
        self.state = state

    def __bool__(self):
        return self.state == ACTIVE

    @abstractmethod
    def __eq__(self, other):
        ...

    @abstractmethod
    def __hash__(self):
        ...

    @abstractmethod
    def set_state(self, state: str) -> 'AbstractConwayCube':
        ...

    @abstractmethod
    def possible_neighors(self) -> List[tuple]:
        ...


class ConwayCube3D(AbstractConwayCube):
    # pylint: disable=invalid-name
    x: int
    y: int
    z: int

    def __init__(self, state: str, x: int, y: int, z: int):
        AbstractConwayCube.__init__(self, state)
        self.x = x
        self.y = y
        self.z = z

    def __bool__(self):
        return self.state == ACTIVE

    def __eq__(self, other):
        if isinstance(other, tuple):
            return (self.x == other[0]
                    and self.y == other[1]
                    and self.z == other[2])

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def set_state(self, state: str) -> 'AbstractConwayCube':
        return ConwayCube3D(state, self.x, self.y, self.z)

    def possible_neighors(self) -> List[tuple]:
        # including this cube
        return list(product(range(self.x - 1, self.x + 2),
                            range(self.y - 1, self.y + 2),
                            range(self.z - 1, self.z + 2)))


@dataclass
class PocketDimension():
    cubes: list = field(default_factory=list)

    def active_cubes(self) -> List[ConwayCube3D]:
        return len([x for x in self.cubes if x])

    def active_neighbors(self, cube) -> int:
        return sum(x.__bool__() for x in self.existing_neighbors(cube))

    def existing_neighbors(self, cube) -> List[ConwayCube3D]:
        return [x for x in self.cubes
                if cube != x
                and cube.x - 1 <= x.x <= cube.x + 1
                and cube.y - 1 <= x.y <= cube.y + 1
                and cube.z - 1 <= x.z <= cube.z + 1]

    def all_neighbors(self, cube) -> List[ConwayCube3D]:
        neighbors = self.existing_neighbors(cube)

        for neighbor in cube.possible_neighors():
            if neighbor in neighbors:
                continue

            blank_cube = ConwayCube3D(INACTIVE, neighbor[0],
                                      neighbor[1], neighbor[2])

            neighbors.append(blank_cube)

        return neighbors

    def evaluate_cube(self, cube) -> ConwayCube3D:
        if not cube and self.active_neighbors(cube) == 3:
            return cube.set_state(ACTIVE)

        if cube and self.active_neighbors(cube) not in [2, 3]:
            return cube.set_state(INACTIVE)

        return cube

    def cycle(self) -> None:
        new_cubes = []

        for cube in self.cubes:
            for neighbor in self.all_neighbors(cube):
                if neighbor not in new_cubes:
                    new_cube = self.evaluate_cube(neighbor)
                    if new_cube:
                        new_cubes.append(new_cube)

        self.cubes = new_cubes


def parse_file(path: str) -> PocketDimension:
    # pylint: disable=invalid-name
    pocket_dim = PocketDimension()

    z = 0
    with open(path) as file_handle:
        y = 0
        for line in [line.rstrip() for line in file_handle]:
            x = 0
            for char in line:
                pocket_dim.cubes.append(ConwayCube3D(char, x, y, z))
                x += 1

            y += 1

    return pocket_dim


def main():
    pocket_dim = parse_file('day17_input.txt')

    for _ in range(6):
        pocket_dim.cycle()

    print(f'Active 3D Cubes {pocket_dim.active_cubes()}')
    # 301


if __name__ == '__main__':
    main()
