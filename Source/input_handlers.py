import tcod as libtcod  # TODO Update TCOD Function (fix_deprecations)
from game_states import GameStates


def handle_keys(key, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key)
    elif game_state == GameStates.LEVEL_UP:
        return handle_level_up_menu(key)
    elif game_state == GameStates.CHARACTER_SCREEN:
        return handle_character_screen(key)

    return {}


def handle_player_turn_keys(key):  # TODO solve some key conflicts
    # Movement keys
    # key_char = chr(key.c)
    if key in (libtcod.event.K_UP, libtcod.event.K_k, libtcod.event.K_w):
        return {'move': (0, -1)}
    elif key in (libtcod.event.K_DOWN, libtcod.event.K_j, libtcod.event.K_s):
        return {'move': (0, 1)}
    elif key in (libtcod.event.K_LEFT, libtcod.event.K_h, libtcod.event.K_a):
        return {'move': (-1, 0)}
    elif key in (libtcod.event.K_RIGHT, libtcod.event.K_l, libtcod.event.K_d):
        return {'move': (1, 0)}
    elif key in (libtcod.event.K_y, libtcod.event.K_q):
        return {'move': (-1, -1)}
    elif key in (libtcod.event.K_u, libtcod.event.K_e):
        return {'move': (1, -1)}
    elif key in (libtcod.event.K_b, libtcod.event.K_z):
        return {'move': (-1, 1)}
    elif key in (libtcod.event.K_n, libtcod.event.K_c):
        return {'move': (1, 1)}
    elif key == libtcod.event.K_b:
        return {'wait': True}

    if key == libtcod.event.K_g:
        return {'pickup': True}

    if key == libtcod.event.K_i:
        return {'show_inventory': True}

    elif key == libtcod.event.K_o:  # I would prefer this not to be 'd', since I like wasd controls.
        return {'drop_inventory': True}

    elif key == libtcod.event.K_RETURN:
        return {'take_stairs': True}

    elif key == libtcod.event.K_v:
        return {'show_character_screen': True}

    # if key.vk == libtcod.KEY_ENTER and key.lalt:  # TODO pass modifier as well as key
    #     # Alt+Enter: toggle full screen
    #     return {'fullscreen': True}

    elif key == libtcod.event.K_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No Key was pressed
    return{}


def handle_targeting_keys(key):
    if key == libtcod.event.K_ESCAPE:
        return {'exit': True}

    return {}


def handle_player_dead_keys(key):
    # key_char = chr(key.c)

    if key == libtcod.event.K_i:
        return {'show inventory': True}

    # if key.vk == libtcod.KEY_ENTER and key.lalt:
    #     # Alt+Enter: toggle full screen
    #     return {'fullscreen': True}

    elif key == libtcod.event.K_ESCAPE:
        # Exit the game
        return {'exit': True}

    return {}


def handle_mouse(mouse):
    (x, y) = mouse.tile
    if mouse.type == "MOUSEBUTTONDOWN":
        if mouse.button == libtcod.event.BUTTON_LEFT:
            return {'left_click': (x, y)}
        elif mouse.button == libtcod.event.BUTTON_RIGHT:
            return {'right_click': (x, y)}

    return {}


def handle_inventory_keys(key):
    if key is not None:
        index = key - libtcod.event.K_a

        if index >= 0:
            return {'inventory_index': index}

        # if key.vk == libtcod.KEY_ENTER and key.lalt:
        #     # Alt+Enter: toggle full screen
        #     return {'fullscreen': True}

        elif key == libtcod.event.K_ESCAPE:
            # Exit the menu
            return {'exit': True}

    return {}


def handle_main_menu(key):
    if key == libtcod.event.K_a:
        return {'new_game': True}
    elif key == libtcod.event.K_b:
        return {'load_game': True}
    elif key == libtcod.event.K_c or key == libtcod.event.K_ESCAPE:
        return {'exit': True}

    return {}


def handle_level_up_menu(key):
    if key:
        # key_char = chr(key.c)

        if key == libtcod.event.K_a:
            return {'level_up': 'hp'}
        elif key == libtcod.event.K_b:
            return {'level_up': 'str'}
        elif key == libtcod.event.K_c:
            return {'level_up': 'def'}

    return {}


def handle_character_screen(key):
    if key == libtcod.event.K_ESCAPE:
        return {'exit': True}

    return {}
