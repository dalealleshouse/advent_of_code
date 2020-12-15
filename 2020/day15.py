def process_turn(game_state, last_num, turn):
    if last_num not in game_state:
        game_state[last_num] = turn
        return game_state, 0

    num = turn - game_state[last_num]
    game_state[last_num] = turn
    return game_state, num


def process_game(seed_data, turns):
    game_state = {}
    num = seed_data[-1]

    for turn, seed in enumerate(seed_data[:-1]):
        game_state[seed] = turn + 2

    for turn in range(len(seed_data) + 1, turns + 1):
        game_state, num = process_turn(game_state, num, turn)

    return num


def main():
    seed_data = [9, 19, 1, 6, 0, 5, 4]
    # seed_data = [0, 3, 6]

    final_num = process_game(seed_data, 2020)
    print(f'Final number spoken = {final_num}')
    # 1522

    final_num = process_game(seed_data, 30000000)
    print(f'Final number spoken = {final_num}')
    # 18234


if __name__ == '__main__':
    main()
