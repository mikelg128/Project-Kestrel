import tcod
from debug_functions import print_event
import constants as const
# from game_messages import Message, MessageLog
# from UI_functions import render_ui
# from loader_functions.initialize_new_game import get_constants, get_game_variables
# from game_states import GameStates


def render_graphics(con):

    y = 0
    for j in range(con.height):
        x = 0
        for i in range(con.width):
            con.tiles[x, y] = ord(' '), (*tcod.white, 255), (*tcod.blue, 255)
            if x is not con.width - 1:
                x += 1
                con.tiles[x, y] = ord(' '), (*tcod.white, 255), (*tcod.blue, 255)
            if x is con.width - 1:
                break
            x += 1
        y += 1

def main():

    window_title = 'Graphics Testing'

    tileset = tcod.tileset.load_tilesheet('../assets/arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
    main_loop_count = 0

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

        while True:

            render_graphics(root_console)

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

                    print_event(event)
                elif event.type == 'KEYDOWN':
                    if event.sym == tcod.event.K_ESCAPE:
                        raise SystemExit()


if __name__ == "__main__":
    main()