import tcod as libtcod
from tcod.loader import ffi, lib


class State(libtcod.event.EventDispatch[None]):
    """A state-based superclass that converts `events` into `commands`.

    The configuration used to convert events to commands are hard-coded
    in this example, but could be modified to be user controlled.

    Subclasses will override the `cmd_*` methods with their own
    functionality.  There could be a subclass for every individual state
    of your game.
    """

    def ev_mousemotion(self, event: libtcod.event.MouseMotion) -> None:
        """The mouse has moved within the window."""
        print(event)
        return event.tile



def main() -> None:
    screen_width = 80
    screen_height = 50
    tileset = libtcod.tileset.load_tilesheet('../assets/arial10x10.png', 32, 8, libtcod.tileset.CHARMAP_TCOD)
    main_loop_count = 0
    state = State()
    # Create a new terminal:
    with libtcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title='Event Testing',
            vsync=True
    ) as context:
        # Create the root console:
        root_console = libtcod.Console(screen_width, screen_height, order='F')


        # Create console for panel:
        # panel = libtcod.Console(screen_width, panel_height, order='F')
        while True:  # <- I don't love
            main_loop_count += 1  # For debugging
            for x in range(0, screen_width):
                for y in range(0, screen_height):
                    root_console.tiles_rgb[x, y] = ord(" "), [0, 0, 0], libtcod.blue
            for event in libtcod.event.wait():
                context.convert_event(event)
                tile = state.dispatch(event)
                root_console.print(int(screen_width/2), int(screen_height/2), event.type, libtcod.white,
                                   alignment=libtcod.CENTER)
                # if event.type == "KEYDOWN":
                #     key = event.sym
                # elif event.type == "MOUSEBUTTONDOWN":
                #     mouse = event
                if event.type == "MOUSEMOTION":
                    # pixel = event.pixel
                    # tile = libtcod.event._pixel_to_tile(*pixel)
                    # print(tile)
                    # x, y = pixel
                    # print('{0}, {1}'.format(x, y))
                    # xy = ffi.new("double[2]", (x, y))
                    # lib.TCOD_sys_pixel_to_tile(xy, xy + 1)
                    # print('{0}, {1}'.format(xy[0], xy[1]))
                    # pix_x, pix_y = pixel
                    # pixel_coord = '{0}, {1}'.format(pix_x, pix_y)
                    if tile:
                        tile_str = '{0}, {1}'.format(tile[0], tile[1])
                        root_console.print(int(screen_width / 2), int(screen_height / 2) + 1, tile_str, libtcod.white,
                                           alignment=libtcod.CENTER)
                if event.type == 'QUIT':
                    raise SystemExit()

            context.present(root_console)
            root_console.clear()


if __name__ == '__main__':
    main()