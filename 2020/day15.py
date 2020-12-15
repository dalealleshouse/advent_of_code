def process_turn(seed_data, game_state, last_num, turn):
    if last_num is None:
        return {}, seed_data[0]

    if turn <= len(seed_data):
        game_state[last_num] = turn
        return game_state, seed_data[turn - 1]

    if last_num not in game_state:
        game_state[last_num] = turn
        return game_state, 0

    num = turn - game_state[last_num]
    game_state[last_num] = turn
    return game_state, num


def process_game(seed_data, turns):
    game_state = {}
    num = None
    for turn in range(1, turns + 1):
        game_state, num = process_turn(seed_data, game_state, num, turn)

    return num


def main():
    seed_data = [9, 19, 1, 6, 0, 5, 4]

    final_num = process_game(seed_data, 2020)
    print(f'Final number spoken = {final_num}')

    final_num = process_game(seed_data, 30000000)
    print(f'Final number spoken = {final_num}')


if __name__ == '__main__':
    main()
