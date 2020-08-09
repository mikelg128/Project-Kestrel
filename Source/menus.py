
import tcod


def menu(con, header, options, window_width, screen_width, screen_height):
    if len(options) > 26:
        raise ValueError('Cannot have a menu with more than 26 options.')

    # calculate text width
    text_width = window_width - 2

    # calculate total height for the header (after auto-wrap) and one line per option
    header_height = con.get_height_rect(0, 0, text_width, screen_height - 2, header)
    text_height = len(options) + header_height

    # calculate window height based on the calculated text height
    window_height = text_height + 2

    # create an off-screen console that represents the menu's window
    window = tcod.Console(window_width, window_height, order="F")

    # Draw window border
    draw_border(window, window_width, window_height)

    # print the header, with auto-wrap
    window.print_box(1, 1, text_width, text_height, header, tcod.white, alignment=tcod.LEFT)

    # print all the options
    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        window.print(1, y, text, tcod.white, alignment=tcod.LEFT)
        y += 1
        letter_index += 1

    # blit the contents of 'window' to the root console
    x = int(screen_width / 2 - window_width / 2)
    y = int(screen_height / 2 - window_height / 2)
    window.blit(con, x, y, 0, 0, window_width, window_height, 1.0, 0.7)


def inventory_menu(con, header, player, inventory_width, screen_width, screen_height):
    # show a menu with each item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = []

        for item in player.inventory.items:
            if player.equipment.main_hand == item:
                options.append('{0} (on main hand)'.format(item.name))
            elif player.equipment.off_hand == item:
                options.append('{0} (on off hand)'.format(item.name))
            else:
                options.append(item.name)

    menu(con, header, options, inventory_width, screen_width, screen_height)


def main_menu(con, background_image, screen_width, screen_height):
    # tcod.image_blit_2x(background_image, 0, 0, 0)  # Do something about image drawing later.
    con.print(int(screen_width / 2), int(screen_height / 2) - 6, '[Rogue Like]', tcod.light_yellow,
              alignment=tcod.CENTER)
    con.print(int(screen_width / 2), int(screen_height / 2) - 5, 'by Michael Greer & Samar Mathur',
              tcod.light_yellow, alignment=tcod.CENTER)

    menu(con, '', ['Play a new game', 'Continue last game', 'Quit'], 24, screen_width, screen_height)


def level_up_menu(con, header, player, menu_width, screen_width, screen_height):
    options = ['Constitution (+20 HP, from {0})'.format(player.fighter.max_hp),
               'Strength (+1 attach, from {0}'.format(player.fighter.power),
               'Agility (+1 Defense, from {0}'.format(player.fighter.defense)]

    menu(con, header, options, menu_width, screen_width, screen_height)


def character_screen(con, player, character_screen_width, character_screen_height, screen_width, screen_height):
    window = tcod.Console(character_screen_width, character_screen_height)

    window.print_box(0, 1, character_screen_width, character_screen_height, 'Character Information', tcod.white,
                     alignment=tcod.LEFT)
    window.print_box(0, 2, character_screen_width, character_screen_height,
                     'Level: {0}'.format(player.level.current_level), tcod.white, alignment=tcod.LEFT)
    window.print_box(0, 3, character_screen_width, character_screen_height,
                     'Experience: {0}'.format(player.level.current_xp), tcod.white, alignment=tcod.LEFT)
    window.print_box(0, 4, character_screen_width, character_screen_height,
                     'Experience to Level: {0}'.format(player.level.experience_to_next_level), tcod.white,
                     alignment=tcod.LEFT)
    window.print_box(0, 6, character_screen_width, character_screen_height,
                     'Maximum HP: {0}'.format(player.fighter.max_hp), tcod.white, alignment=tcod.LEFT)
    window.print_box(0, 7, character_screen_width, character_screen_height,
                     'Attack: {0}'.format(player.fighter.power), tcod.white, alignment=tcod.LEFT)
    window.print_box(0, 8, character_screen_width, character_screen_height,
                     'Defense: {0}'.format(player.fighter.defense), tcod.white, alignment=tcod.LEFT)

    x = screen_width // 2 - character_screen_width // 2
    y = screen_height // 2 - character_screen_height // 2
    window.blit(con, x, y, 0, 0, character_screen_width, character_screen_height, 1.0, 0.7)


def message_box(con, header, width, screen_width, screen_height):
    menu(con, header, [], width, screen_width, screen_height)


def draw_border(con, width, height):

    for x in range(0, width):
        for y in range(0, height):
            if (x == 0 or x == width - 1) and (y == 0 or y == height - 1):
                con.print(x, y, chr(9532), tcod.white)
            elif x == 0 or x == width - 1:
                con.print(x, y, chr(9474), tcod.white)
            elif y == 0 or y == height - 1:
                con.print(x, y, chr(9472), tcod.white)
