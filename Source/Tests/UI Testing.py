import tcod
from debug_functions import print_tile_coord_at_mouse, print_event
from Tests.constants import Constants
import Tests.constants as const
import time
from game_messages import Message, MessageLog
from UI_functions import render_ui


def main():

    window_title = 'UI Testing'

    tileset = tcod.tileset.load_tilesheet('../assets/arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
    main_loop_count = 0

    game_state = 1

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
        overlay_con = tcod.Console(const.popup_width, const.popup_height, order='F')

        while True:
            # panel.print(30, 20, 'Hello World', tcod.white, alignment=tcod.CENTER)
            #
            # for x in range(0, panel_width):
            #     for y in range(0, panel_height):
            #         if (x == 0 or x == 59) and (y == 0 or y == 39):
            #             panel.print(x, y, chr(9532), tcod.white)
            #         elif x == 0 or x == 59:
            #             panel.print(x, y, chr(9474), tcod.white)
            #         elif y == 0 or y == 39:
            #             panel.print(x, y, chr(9472), tcod.white)
            #
            # panel.blit(root_console, 10, 5, 0, 0, panel_width, panel_height, 1.0, 1.0)

            # root_console.draw_frame(10, 5, panel_width, panel_height, 'Hello World')

            # ui.render_ui(game_state)
            render_ui(root_console, panel_con, overlay_con, game_state, message_log, 0, 1, 'Something')

            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                context.convert_event(event)
                print_event(event)
                if event.type == 'QUIT':
                    raise SystemExit()
                if event.type == 'MOUSEMOTION':
                    print_tile_coord_at_mouse(event.tile)
                if event.type == 'MOUSEBUTTONDOWN':
                    message_log.add_message(Message('Click!'))
                    game_state = 2
                if event.type == 'KEYDOWN':
                    message_log.add_message(Message('Clack!'))
                    game_state = 1


if __name__ == "__main__":
    main()