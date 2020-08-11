import tcod
from debug_functions import print_tile_coord_at_mouse

class UI_element:
    def __init__(self, width, height, frame_flag=False, frame_title=''):
        self.width = width
        self.height = height
        self.frame_title = frame_title
        self.frame_flag = frame_flag
        self.element = tcod.Console(self.width, self.height, order='F')

        if frame_flag:
            self.draw_frame()

    def create_element(self, width, height):
        self.element = tcod.Console(width, height, order='F')

    def blit_element(self, root, dstx, dsty):
        self.element.blit(root, dstx, dsty, 0, 0, self.width, self.height)

    def draw_frame(self):
        self.element.draw_frame(0, 0, self.width, self.height, self.frame_title)

    def menu(self, header, options, window_width, screen_width, screen_height):
        if len(options) > 26:
            raise ValueError('Cannot have a menu with more than 26 options.')

        if self.frame_flag:
            border = 2
        else:
            border = 0

        # calculate text width, subtracting the border if it exists
        text_width = self.width - border

        # set max header height
        max_header_height = 2

        # calculate total height for the header (after auto-wrap) and one line per option
        header_height = self.element.get_height_rect(0, 0, text_width, max_header_height, header)
        text_height = len(options) + header_height

        # calculate new window height based on the calculated text height, adding a border if it exists
        self.height = text_height + border

        # reset the element console with new height
        self.create_element(self.width, self.height)

        # print the header, with auto-wrap
        self.element.print_box(border/2, border/2, text_width, text_height, header, tcod.white, alignment=tcod.LEFT)

        # print all the options
        y = header_height
        letter_index = ord('a')
        for option_text in options:
            text = '(' + chr(letter_index) + ') ' + option_text
            self.element.print(1, y, text, tcod.white, alignment=tcod.LEFT)
            y += 1
            letter_index += 1


def main():
    screen_width = 80
    screen_height = 50
    window_title = 'UI Testing'

    tileset = tcod.tileset.load_tilesheet('../assets/arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
    main_loop_count = 0

    element_1 = UI_element(20, 20, True, "test")
    element_2 = UI_element(10, 10, True, "test 2")

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

            element_1.blit_element(root_console, 10, 10)
            element_2.blit_element(root_console, 20, 20)

            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                context.convert_event(event)
                if event.type == 'QUIT':
                    raise SystemExit()
                if event.type == 'MOUSEMOTION':
                    print_tile_coord_at_mouse(event.tile)


if __name__ == "__main__":
    main()