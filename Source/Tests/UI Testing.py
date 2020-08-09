import tcod as tcod


def main():
    screen_width = 80
    screen_height = 50
    window_title = 'UI Testing'

    tileset = tcod.tileset.load_tilesheet('../assets/arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
    main_loop_count = 0

    # Create a new terminal:
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title=window_title,
            vsync=True
    ) as context:
        # Create the root console:
        root_console = tcod.Console(screen_width, screen_height, order='F')
        panel_width, panel_height = 60, 40
        panel = tcod.Console(panel_width, panel_height, order='F')

        while True:
            panel.print(30, 20, 'Hello World', tcod.white, alignment=tcod.CENTER)

            for x in range(0, panel_width):
                for y in range(0, panel_height):
                    if (x == 0 or x == 59) and (y == 0 or y == 39):
                        panel.print(x, y, chr(9532), tcod.white)
                    elif x == 0 or x == 59:
                        panel.print(x, y, chr(9474), tcod.white)
                    elif y == 0 or y == 39:
                        panel.print(x, y, chr(9472), tcod.white)

            panel.blit(root_console, 10, 5, 0, 0, panel_width, panel_height, 1.0, 1.0)
            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                if event.type == 'QUIT':
                    raise SystemExit()


if __name__ == "__main__":
    main()