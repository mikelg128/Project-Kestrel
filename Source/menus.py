
import tcod


def option_menu(con, header, options, window_width, con_width, con_height):
    if len(options) > 26:
        raise ValueError('Cannot have a menu with more than 26 options.')

    # calculate text width, assuming a border exists
    text_width = window_width - 2

    # calculate total height for the header (after auto-wrap) and one line per option
    header_height = con.get_height_rect(0, 0, text_width, con_height - 2, header)  # Why reference screen_height?
    text_height = len(options) + header_height

    # calculate window height and location (centered on the console) based on the calculated text height,
    # assuming a border exists
    window_height = text_height + 2
    window_dstx = int((con_width - window_width) / 2)
    window_dsty = int((con_height - window_height) / 2)

    # Calculate text start coordinates:
    text_dstx = window_dstx + 1
    text_dsty = window_dsty + 1

    # print the header, with auto-wrap
    con.print_box(text_dstx, text_dsty, text_width, text_height, header, tcod.white, alignment=tcod.LEFT)

    # print all the options
    y = text_dsty + header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        con.print(text_dstx, y, text, tcod.white, alignment=tcod.LEFT)
        y += 1
        letter_index += 1

    # blit the contents of 'window' to the root console
    # x = int(screen_width / 2 - window_width / 2)
    # y = int(screen_height / 2 - window_height / 2)
    # window.blit(con, x, y, 0, 0, window_width, window_height, 1.0, 0.7)
    return window_dstx, window_dsty, window_height


def info_menu(con, info_list, window_width, con_width, con_height):

    # Calculate text height based on number of options, assuming a border exists
    text_height = len(info_list)

    # calculate window height and location (centered on the console) based on the calculated text height,
    # assuming a border exists
    window_height = text_height + 2
    window_dstx = int((con_width - window_width) / 2)
    window_dsty = int((con_height - window_height) / 2)

    # Calculate text destination based on the window destination
    text_dstx = window_dstx + 1
    text_dsty = window_dsty + 1

    y = text_dsty
    for info_text in info_list:
        con.print_box(text_dstx, y, window_width, window_height, info_text, tcod.white, alignment=tcod.LEFT)
        y += 1

    return window_dstx, window_dsty, window_height


def message_box(con, header, width, screen_width, screen_height):
    option_menu(con, header, [], width, screen_width, screen_height)


def draw_border(con, width, height):

    for x in range(0, width):
        for y in range(0, height):
            if (x == 0 or x == width - 1) and (y == 0 or y == height - 1):
                con.print(x, y, chr(9532), tcod.white)
            elif x == 0 or x == width - 1:
                con.print(x, y, chr(9474), tcod.white)
            elif y == 0 or y == height - 1:
                con.print(x, y, chr(9472), tcod.white)
