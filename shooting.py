import time
from validation_input import input_validation_coulumn, input_validation_row 
from parematers import alphabet_max, players_availlable, ship_direction,board_size_sep, board_maximal_rang, game_command, game_who_play, game_difficult, board_signes, game_colours
from messages import game_messages
from time_game import day_time


def print_boards(board_size_len, board_size, player, competitor):
    print(game_colours["MESSE_STA"]+f"PLAYER 1"+game_colours["MESSE_END"] + " "*62 + 
          game_colours["MESSE_STA"]+f"PLAYER 2"+game_colours["MESSE_END"])
    sep = 24 - len(player['name'][1])
    print(game_colours["ERROR_STA"]+f"{player['name'][0]} {player['name'][1]} armour status and below his target MAP"+game_colours["ERROR_END"] + " "*(sep -2)+ 
          game_colours["ERROR_STA"]+f"{competitor['name'][0]} {competitor['name'][1]} armour status and below his target MAP"+game_colours["ERROR_END"])
    #status_bar(player, board_size)
    play_board = []
    compet_board = []
    for x, y in enumerate(player["board"][1]):
        if x == 0:
            play_board.append((game_colours["MESSE_STA"]+f'{"COLUMN"}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"]))
            play_board.append((f'{"-" * 10}{"-" * (board_size * 2)}'))
        else:
            play_board.append((game_colours["MESSE_STA"]+f'ROW  {x}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"]))
    play_board.append((f'{"-" * 10}{"-" * (board_size * 2)}'))

    for x, y in enumerate(competitor["board"][1]):
        if x == 0:
            compet_board.append((game_colours["MESSE_STA"]+f'{"COLUMN"}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"]))
            compet_board.append((f'{"-" * 10}{"-" * (board_size * 2)}'))
        else:
            compet_board.append((game_colours["MESSE_STA"]+f'ROW  {x}{" " * (board_size_len - len(str(x)))} | {board_size_sep.join(y)}'+game_colours["MESSE_END"]))
    compet_board.append((f'{"-" * 10}{"-" * (board_size * 2)}'))
    
    for a, b in zip(status_bar(player, board_size), status_bar(competitor, board_size)):
        print(f'{a}{" " * 23}{b}')
    sep1 = 70 - int(len(play_board[1]))
    sep2 = 72 - int(len(play_board[1]))
    for a, b in zip(play_board, compet_board):
        if '-' in b:
            print(f'{a}{" " * sep1}{b}')
        else:     
            print(f'{a}{" " * sep2}{b}')

def status_bar(player_bar, board_size):
    bar = []
    display_factor_bullets = 25 #to match screen size
    display_factor_ships = 5 #to match screen size

    bullet_availlave = int((player_bar["bullets"][0] / (player_bar["bullets"][0]+player_bar["bullets"][1])) * display_factor_bullets)
    ships_availlable = int((player_bar["ship_no"][1] / len(player_bar['ship_location'])) * display_factor_ships) 
    
    bullet_uesed = int(display_factor_bullets - bullet_availlave)
    ships_lost = int(display_factor_ships - ships_availlable)

    bar.append(('-' * ((display_factor_bullets + display_factor_ships)+17)))
    bar.append(((" BULLETS ")+((game_colours["STATUS_BAR_AVAILLABLE_S"]+f"{' '}"+ game_colours["STATUS_BAR_AVAILLABLE_E"]) * bullet_availlave)
          +((game_colours["STATUS_BAR_USED_S"]+f"{' '}"+ game_colours["STATUS_BAR_USED_E"]) * bullet_uesed)
          +(" SHIPS ")+((game_colours["STATUS_BAR_AVAILLABLE_S"]+f"{' '}"+ game_colours["STATUS_BAR_AVAILLABLE_E"]) * ships_availlable)
          +((game_colours["STATUS_BAR_USED_S"]+f"{' '}"+ game_colours["STATUS_BAR_USED_E"]) * ships_lost)))
    bar.append(('-' * ((display_factor_bullets + display_factor_ships)+17)))
    return bar