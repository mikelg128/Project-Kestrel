import tcod
from debug_functions import print_tile_coord_at_mouse


class UserInterface:
    def __init__(self, screen_width, screen_height, con):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.root = con

        # UI Element definitions:
        # Panel definition:
        self.panel_width = screen_width
        self.panel_height = 10
        self.panel = tcod.Console(self.panel_width, self.panel_height, order='F')
        # Panel location:
        self.panel_dstx = 0
        self.panel_dsty = self.screen_height - self.panel_height

        # Misc Pop Up Element:
        self.popup_width = 40
        self.popup_height = 20
        self.popup = tcod.Console(self.popup_width, self.popup_height, order='F')
        self.popup_dstx = int((self.screen_width - self.popup_width)/2)
        self.popup_dsty = int(((self.screen_height - self.panel_height) - self.popup_height)/2)

    def render_popup(self):
        self.popup.draw_frame(0, 0, self.popup_width, self.popup_height, "Pop-Up Window")
        self.popup.print(int(self.popup_width/2), int(self.popup_height/2), "This is a pop up window", tcod.white,
                         alignment=tcod.CENTER)

        self.popup.blit(self.root, self.popup_dstx, self.popup_dsty, 0, 0, self.popup_width, self.popup_height)

    def render_panel(self):
        self.panel.draw_frame(0, 0, self.panel_width, self.panel_height)

        self.panel.print(int(self.panel_width/2), int(self.panel_height/2), "Hello World", tcod.white,
                         alignment=tcod.CENTER)

        self.panel.blit(self.root, self.panel_dstx, self.panel_dsty, 0, 0, self.panel_width, self.panel_height, 1.0,
                        1.0)

    def render_ui(self, game_state):
        if game_state == 1:
            self.render_panel()
        elif game_state == 2:
            self.render_panel()
            self.render_popup()


def main():
    screen_width = 80
    screen_height = 50
    window_title = 'UI Testing'

    tileset = tcod.tileset.load_tilesheet('../assets/arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
    main_loop_count = 0

    game_state = 1

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

        # Create the UI
        panel_width, panel_height = 60, 40
        ui = UserInterface(screen_width, screen_height, root_console)

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

            ui.render_ui(game_state)
            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                context.convert_event(event)
                if event.type == 'QUIT':
                    raise SystemExit()
                if event.type == 'MOUSEMOTION':
                    print_tile_coord_at_mouse(event.tile)
                if event.type == 'MOUSEBUTTONDOWN':
                    game_state = 2
                if event.type == 'KEYDOWN':
                    game_state = 1


if __name__ == "__main__":
    main()