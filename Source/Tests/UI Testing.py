import tcod as libtcod


def main():
    screen_width = 80
    screen_height = 50
    window_title = 'UI Testing'

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, window_title, False)

    con = libtcod.console_new(60, 40)

    while not libtcod.console_is_window_closed():

        libtcod.console_set_default_foreground(con, libtcod.white)
        libtcod.console_print_ex(con, 30, 20, libtcod.BKGND_NONE, libtcod.CENTER,
                                 'Hello World')
        # libtcod.console_put_char(con, 0, 0, '+', libtcod.BKGND_NONE)
        # libtcod.console_put_char(con, 0, 40 - 1, '+', libtcod.BKGND_NONE)
        # libtcod.console_put_char(con, 60 - 1, 0, '+', libtcod.BKGND_NONE)
        # libtcod.console_put_char(con, 60 - 1, 40 - 1, '+', libtcod.BKGND_NONE)
        for x in range(0, 60):
            for y in range(0, 40):
                if (x == 0 or x == 59) and (y == 0 or y == 39):
                    libtcod.console_put_char(con, x, y, '+', libtcod.BKGND_NONE)
                elif x == 0 or x == 59:
                    libtcod.console_put_char(con, x, y, 179, libtcod.BKGND_NONE)
                elif y == 0 or y == 39:
                    libtcod.console_put_char(con, x, y, 196, libtcod.BKGND_NONE)

        libtcod.console_blit(con, 0, 0, 60, 40, 0, 10, 5, 1.0, 1.0)
        libtcod.console_flush()

        key = libtcod.console_check_for_keypress()

        if key.vk == libtcod.KEY_ESCAPE:
            return True


if __name__ == "__main__":
    main()