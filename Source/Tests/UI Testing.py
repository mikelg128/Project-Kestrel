import tcod
from debug_functions import print_tile_coord_at_mouse, print_event
from Tests.constants import Constants
import Tests.constants as const
import time
from game_messages import Message, MessageLog
from UI_functions import render_ui
from loader_functions.initialize_new_game import get_constants, get_game_variables
from game_states import GameStates


def main():

    window_title = 'UI Testing'

    tileset = tcod.tileset.load_tilesheet('../assets/arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
    main_loop_count = 0

    constants = get_constants()
    player, entities, game_map, message_log, game_state = get_game_variables(constants)
    message_log = MessageLog(const.message_panel_dstx, const.message_width, const.message_height)

    # Create a new terminal:
    with tcod.context.new_terminal(
            const.screen_width,
            const.screen_height,
            tileset=tileset,
            title=window_title,
            vsync=True
    ) as context:
        # Create the root console:
        root_console = tcod.Console(const.screen_width, const.screen_height, order='F')
        # Create UI element consoles:
        panel_con = tcod.Console(const.panel_width, const.panel_height, order='F')
        window_con = tcod.Console(const.popup_width, const.popup_height, order='F')
        overlay_con = tcod.Console(const.overlay_width, const.overlay_height, order='F')

        # Create UI console, which contains all UI elements.
        # ui_con = tcod.Console(const.screen_width, const.screen_height, order='F')

        while True:
            render_ui(root_console, panel_con, overlay_con, game_state, message_log, player, 1, 'Something')

            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                context.convert_event(event)
                # print_event(event)
                if event.type == 'QUIT':
                    raise SystemExit()
                # elif event.type == 'MOUSEMOTION':
                    # print_tile_coord_at_mouse(event.tile)
                elif event.type == 'MOUSEBUTTONDOWN':
                    message_log.add_message(Message('Click!'))
                    print_event(event)
                elif event.type == 'KEYDOWN':
                    if event.sym == tcod.event.K_ESCAPE and game_state == GameStates.PLAYERS_TURN:
                        raise SystemExit()
                    elif event.sym == tcod.event.K_ESCAPE:
                        game_state = GameStates.PLAYERS_TURN
                    message_log.add_message(Message('Clack!'))
                    if event.sym == tcod.event.K_i:
                        message_log.add_message(Message('You check your bag.'))
                        game_state = GameStates.SHOW_INVENTORY
                        print(game_state)
                    elif event.sym == tcod.event.K_l:
                        message_log.add_message(Message('You leveled up!'))
                        game_state = GameStates.LEVEL_UP
                        print(game_state)
                    elif event.sym == tcod.event.K_c:
                        message_log.add_message(Message('You think about your stats..'))
                        game_state = GameStates.CHARACTER_SCREEN
                        print(game_state)



if __name__ == "__main__":
    main()