from dataclasses import dataclass, field
from typing import Set
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

    def __bool__(self):
        return self.state == ACTIVE

    def __eq__(self, other):
        return self.coords == other.coords

    def __hash__(self):
        return hash(self.coords)

    def set_state(self, state: str) -> 'ConwayCube':
        return ConwayCube(state, self.dimensions, self.coords)

    def possible_neighors(self) -> Set[tuple]:
        ranges = []
        for i in range(self.dimensions):
            ranges.append(range(self.coords[i] - 1, self.coords[i] + 2))

        return set(product(*ranges))


@dataclass
class PocketDimension():
    dimensions: int
    cubes: set = field(default_factory=set)

    def active_cubes(self) -> int:
        return len([x for x in self.cubes if x])

    def active_neighbors(self, cube) -> int:
        return sum(x.__bool__() for x in self.existing_neighbors(cube))

    def existing_neighbors(self, cube) -> Set[ConwayCube]:
        if cube.dimensions == 3:
            return {x for x in self.cubes
                    if cube != x
                    and cube.coords[0] - 1 <= x.coords[0] <= cube.coords[0] + 1
                    and cube.coords[1] - 1 <= x.coords[1] <= cube.coords[1] + 1
                    and cube.coords[2] - 1 <= x.coords[2] <= cube.coords[2] + 1
                    }

        return {x for x in self.cubes
                if cube != x
                and cube.coords[0] - 1 <= x.coords[0] <= cube.coords[0] + 1
                and cube.coords[1] - 1 <= x.coords[1] <= cube.coords[1] + 1
                and cube.coords[2] - 1 <= x.coords[2] <= cube.coords[2] + 1
                and cube.coords[3] - 1 <= x.coords[3] <= cube.coords[3] + 1}

        # this is generic, but it's slow
        # return {x for x in self.cubes
        #         if cube != x
        #         and all([y - 1 <= x.coords[i] <= y + 1
        #                  for i, y in enumerate(cube.coords)])}

    def evaluate_cube(self, cube) -> ConwayCube:
        if not cube and self.active_neighbors(cube) == 3:
            return cube.set_state(ACTIVE)

        if cube and self.active_neighbors(cube) not in [2, 3]:
            return cube.set_state(INACTIVE)

        return cube

    def cycle(self) -> None:
        new_cubes = set()

        canidate_cubes = set.union(
            *[x.possible_neighors() for x in self.cubes])

        canidate_cubes = map(
            lambda x: ConwayCube(INACTIVE, self.dimensions, x), canidate_cubes)

        canidate_cubes = self.cubes.union(canidate_cubes)

        for cube in canidate_cubes:
            new_cube = self.evaluate_cube(cube)
            if new_cube:
                new_cubes.add(new_cube)

        self.cubes = new_cubes


def create_tuple(x, y, dimensions):
    # pylint: disable=invalid-name
    values = [x, y] + [0 for x in range(2, dimensions)]
    return tuple(values)


def parse_file(path: str, dimensions) -> PocketDimension:
    # pylint: disable=invalid-name
    pocket_dim = PocketDimension(dimensions)

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
    pocket_dim = parse_file('day17_input.txt', 3)

    start = time()
    for _ in range(6):
        pocket_dim.cycle()

    end = time()
    print(f'Active 3D Cubes {pocket_dim.active_cubes()}'
          f' - time {end - start}')
    # 301

    pocket_dim = parse_file('day17_input.txt', 4)

    start = time()
    for _ in range(6):
        pocket_dim.cycle()

    end = time()
    print(f'Active 4D Cubes {pocket_dim.active_cubes()}'
          f' - time {end - start}')
    # 2424


if __name__ == '__main__':
    main()
