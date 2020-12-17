from dataclasses import dataclass, field
from typing import List
from itertools import product
from time import time

ACTIVE = '#'
INACTIVE = '.'


@dataclass
class ConwayCube():
    # pylint: disable=invalid-name
    state: str
    dimensions: int
    coords: tuple
    active_neighbors: int = -1

    def __bool__(self):
        return self.state == ACTIVE

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.coords == other

        return self.coords == other.coords

    def __hash__(self):
        return hash(self.coords)

    @property
    def x(self) -> int:
        return self.coords[0]

    @property
    def y(self) -> int:
        return self.coords[1]

    @property
    def z(self) -> int:
        return self.coords[2]

    @property
    def a(self) -> int:
        return self.coords[3]

    def set_state(self, state: str) -> 'ConwayCube':
        return ConwayCube(state, self.dimensions, self.coords)

    def possible_neighors(self) -> List[tuple]:
        ranges = []
        for i in range(self.dimensions):
            ranges.append(range(self.coords[i] - 1,
                                self.coords[i] + 2))

        return set(product(*ranges))

    def cache_active_neighbors(self, count: int) -> None:
        self.active_neighbors = count


@dataclass
class PocketDimension():
    cubes: set = field(default_factory=set)

    def active_cubes(self) -> List[ConwayCube]:
        return len([x for x in self.cubes if x])

    def active_neighbors(self, cube) -> int:
        if cube.active_neighbors == -1:
            cube.cache_active_neighbors(sum(
                x.__bool__() for x in self.existing_neighbors(cube)))

        return cube.active_neighbors

    def existing_neighbors(self, cube) -> List[ConwayCube]:
        if cube.dimensions == 3:
            return {x for x in self.cubes
                    if cube != x
                    and cube.x - 1 <= x.x <= cube.x + 1
                    and cube.y - 1 <= x.y <= cube.y + 1
                    and cube.z - 1 <= x.z <= cube.z + 1}

        return {x for x in self.cubes
                if cube != x
                and cube.x - 1 <= x.x <= cube.x + 1
                and cube.y - 1 <= x.y <= cube.y + 1
                and cube.z - 1 <= x.z <= cube.z + 1
                and cube.a - 1 <= x.a <= cube.a + 1}

        # this is generic, but it's slow
        # return {x for x in self.cubes
        #         if cube != x
        #         and all([y - 1 <= x.coords[i] <= y + 1
        #                  for i, y in enumerate(cube.coords)])}

    def all_neighbors(self, cube) -> List[ConwayCube]:
        neighbors = self.existing_neighbors(cube)

        for neighbor in cube.possible_neighors():
            if neighbor in neighbors:
                continue

            blank_cube = ConwayCube(INACTIVE, cube.dimensions, neighbor)
            neighbors.add(blank_cube)

        return neighbors

    def evaluate_cube(self, cube) -> ConwayCube:
        if not cube and self.active_neighbors(cube) == 3:
            return cube.set_state(ACTIVE)

        if cube and self.active_neighbors(cube) not in [2, 3]:
            return cube.set_state(INACTIVE)

        return cube

    def cycle(self) -> None:
        new_cubes = set()

        for cube in self.cubes:
            for neighbor in self.all_neighbors(cube):
                if neighbor not in new_cubes:
                    new_cube = self.evaluate_cube(neighbor)
                    if new_cube:
                        new_cubes.add(new_cube)

        self.cubes = new_cubes


def create_tuple(x, y, dimensions):
    # pylint: disable=invalid-name
    values = [x, y]
    for _ in range(2, dimensions):
        values.append(0)

    return tuple(values)


def parse_file(path: str, dimensions) -> PocketDimension:
    # pylint: disable=invalid-name
    pocket_dim = PocketDimension()

    with open(path) as file_handle:
        y = 0
        for line in [line.rstrip() for line in file_handle]:
            x = 0
            for char in line:
                pocket_dim.cubes.add(ConwayCube(
                    char, dimensions, create_tuple(x, y, dimensions)))
                x += 1

            y += 1

    return pocket_dim


def main():
    start = time()
    pocket_dim = parse_file('day17_input.txt', 3)

    for _ in range(6):
        pocket_dim.cycle()

    print(f'Active 3D Cubes {pocket_dim.active_cubes()}')
    end = time()

    print(end - start)
    # 301

    # pocket_dim = parse_file('day17_input.txt', 4)

    # for _ in range(6):
    #     pocket_dim.cycle()
    #     print(_)

    # print(f'Active 4D Cubes {pocket_dim.active_cubes()}')
    # 2424


if __name__ == '__main__':
    main()
