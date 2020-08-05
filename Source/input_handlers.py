import tcod
from game_states import GameStates


def handle_keys(key_event, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key_event)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key_event)
    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key_event)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key_event)
    elif game_state == GameStates.LEVEL_UP:
        return handle_level_up_menu(key_event)
    elif game_state == GameStates.CHARACTER_SCREEN:
        return handle_character_screen(key_event)

    return {}


def handle_player_turn_keys(key_event):  # TODO solve some key conflicts
    # Movement keys
    if key_event.sym == tcod.event.K_RETURN and key_event.mod == tcod.event.KMOD_LALT:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    if key_event.sym in (tcod.event.K_UP, tcod.event.K_k, tcod.event.K_w):
        return {'move': (0, -1)}
    elif key_event.sym in (tcod.event.K_DOWN, tcod.event.K_j, tcod.event.K_s):
        return {'move': (0, 1)}
    elif key_event.sym in (tcod.event.K_LEFT, tcod.event.K_h, tcod.event.K_a):
        return {'move': (-1, 0)}
    elif key_event.sym in (tcod.event.K_RIGHT, tcod.event.K_l, tcod.event.K_d):
        return {'move': (1, 0)}
    elif key_event.sym in (tcod.event.K_y, tcod.event.K_q):
        return {'move': (-1, -1)}
    elif key_event.sym in (tcod.event.K_u, tcod.event.K_e):
        return {'move': (1, -1)}
    elif key_event.sym in (tcod.event.K_b, tcod.event.K_z):
        return {'move': (-1, 1)}
    elif key_event.sym in (tcod.event.K_n, tcod.event.K_c):
        return {'move': (1, 1)}
    elif key_event.sym == tcod.event.K_b:
        return {'wait': True}

    if key_event.sym == tcod.event.K_g:
        return {'pickup': True}

    if key_event.sym == tcod.event.K_i:
        return {'show_inventory': True}

    elif key_event.sym == tcod.event.K_o:  # I would prefer this not to be 'd', since I like wasd controls.
        return {'drop_inventory': True}

    elif key_event.sym == tcod.event.K_RETURN:
        return {'take_stairs': True}

    elif key_event.sym == tcod.event.K_v:
        return {'show_character_screen': True}

    elif key_event.sym == tcod.event.K_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No Key was pressed
    return{}


def handle_targeting_keys(key_event):
    if key_event.sym == tcod.event.K_ESCAPE:
        return {'exit': True}

    return {}


def handle_player_dead_keys(key_event):
    # key_char = chr(key.c)

    if key_event.sym == tcod.event.K_i:
        return {'show inventory': True}

    if key_event.sym == tcod.event.K_RETURN and key_event.mod == tcod.event.K_LALT:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    elif key_event.sym == tcod.event.K_ESCAPE:
        # Exit the game
        return {'exit': True}

    return {}


def handle_mouse(mouse):
    (x, y) = mouse.tile
    if mouse.type == "MOUSEBUTTONDOWN":
        if mouse.button == tcod.event.BUTTON_LEFT:
            return {'left_click': (x, y)}
        elif mouse.button == tcod.event.BUTTON_RIGHT:
            return {'right_click': (x, y)}

    return {}


def handle_inventory_keys(key_event):
    if key_event is not None:
        index = key_event.sym - tcod.event.K_a

        if index >= 0:
            return {'inventory_index': index}

        if key_event.sym == tcod.event.K_RETURN and key_event.mod == tcod.event.K_LALT:
            # Alt+Enter: toggle full screen
            return {'fullscreen': True}

        elif key_event.sym == tcod.event.K_ESCAPE:
            # Exit the menu
            return {'exit': True}

    return {}


def handle_main_menu(key_event):
    if key_event.sym == tcod.event.K_a:
        return {'new_game': True}
    elif key_event.sym == tcod.event.K_b:
        return {'load_game': True}
    elif key_event.sym == tcod.event.K_c or key_event.sym == tcod.event.K_ESCAPE:
        return {'exit': True}

    return {}


def handle_level_up_menu(key_event):
    if key_event:
        # key_char = chr(key.c)

        if key_event.sym == tcod.event.K_a:
            return {'level_up': 'hp'}
        elif key_event.sym == tcod.event.K_b:
            return {'level_up': 'str'}
        elif key_event.sym == tcod.event.K_c:
            return {'level_up': 'def'}

    return {}


def handle_character_screen(key_event):
    if key_event.sym == tcod.event.K_ESCAPE:
        return {'exit': True}

    return {}
