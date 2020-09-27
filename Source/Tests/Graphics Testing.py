import tcod
from debug_functions import print_event
import constants as const
# from game_messages import Message, MessageLog
# from UI_functions import render_ui
# from loader_functions.initialize_new_game import get_constants, get_game_variables
# from game_states import GameStates


def render_graphics(con, tile):

    for j in range(con.height):
        for i in range(con.width):
            con.tiles_rgb[i, j] = ord(' '), tcod.white, tcod.darker_gray

    highlight_tile(con, tile)
    # tile_bg = con.tiles_rgb[x, y][2]
    #
    # tile_bg[1] = tile_bg[1] + 50
    # print(tile_bg)
    # con.tiles_rgb[x, y] = ord(' '), tcod.white, tile_bg


def highlight_tile(con, tile):
    x, y = tile[0], tile[1]
    tile_ch, tile_fg, tile_bg = con.tiles_rgb[tile]
    i = 0
    for c in tile_bg:
        if c < 205:
            tile_bg[i] = c + 50

        else:
            tile_bg[i] = 255
        i += 1

    print(tile_bg)
    con.tiles_rgb[tile] = tile_ch, tile_fg, tile_bg


def main():

    window_title = 'Graphics Testing'

    tileset = tcod.tileset.load_tilesheet('../assets/arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
    main_loop_count = 0

    current_mouse_tile = 0, 0

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

            render_graphics(root_console, current_mouse_tile)

            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                context.convert_event(event)
                # print_event(event)
                if event.type == 'QUIT':
                    raise SystemExit()
                elif event.type == 'MOUSEMOTION':
                    # print_tile_coord_at_mouse(event.tile)
                    mouse = event
                    current_mouse_tile = event.tile
                elif event.type == 'MOUSEBUTTONDOWN':

                    print_event(event)
                elif event.type == 'KEYDOWN':
                    if event.sym == tcod.event.K_ESCAPE:
                        raise SystemExit()


if __name__ == "__main__":
    main()