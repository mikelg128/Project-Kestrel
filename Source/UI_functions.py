import Tests.constants as const
import tcod
from game_states import GameStates


def render_ui(root, panel, window, game_state, message_log, player, dungeon_level, name_under_mouse):
    panel.clear()
    window.clear()

    render_panel(root, panel, message_log, player, dungeon_level, name_under_mouse)
    window_height = 0
    window_width = 0
    window_dsty = 0
    if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        if game_state == GameStates.SHOW_INVENTORY:
            inventory_title = 'Press the key next to an item to use it, or Esc to cancel.\n'
        else:
            inventory_title = 'Press the key next to an item to drop it, or Esc to cancel.\n'
        render_inventory(window, inventory_title, player)
        # window_width = const.inventory_width
        # window_dsty = int(((const.screen_height - const.panel_height) - window_height)/2)
        # window.draw_frame(0, 0, window_width, window_height, "Inventory")
    # elif game_state == GameStates.LEVEL_UP:
    #     level_up_menu(con, 'Level up! Choose a stat to raise:', player, 40, screen_width, screen_height)
    #
    # elif game_state == GameStates.CHARACTER_SCREEN:
    #     character_screen(con, player, 30, 10, screen_width, screen_height)

    panel.blit(root, const.panel_dstx, const.panel_dsty, 0, 0, const.panel_width, const.panel_height, 1.0, 1.0)
    window.blit(root, const.window_dstx, window_dsty, 0, 0, window_width, window_height, 1.0, 0.7)


def render_panel(root, panel, message_log, player, dungeon_level, name_under_mouse):
    # panel.default_bg = tcod.black
    # panel.clear()

    panel.draw_frame(0, 0, const.panel_width, const.panel_height)

    # panel.print(int(const.panel_width / 2), int(const.panel_height / 2), "Hello World", tcod.white,
    #             alignment=tcod.CENTER)

    # Print the game messages, one line at a time
    y = 1
    for message in message_log.messages:
        panel.print(message_log.x, y, message.text, message.color, alignment=tcod.LEFT)
        y += 1

    # Render HP bar:
    render_bar(panel, const.hp_bar_panel_dstx, const.hp_bar_panel_dsty, const.hp_bar_width, 'HP', 40,
               60, tcod.light_red, tcod.darker_red)

    # Print dungeon level:
    panel.print(1, 3, 'Dungeon level: {0}'.format(dungeon_level), tcod.white, alignment=tcod.LEFT)

    # Print names under mouse:
    panel.print(1, 1, name_under_mouse, tcod.light_gray, alignment=tcod.LEFT)

    # panel.blit(root, const.panel_dstx, const.panel_dsty, 0, 0, const.panel_width, const.panel_height, 1.0, 1.0)


def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color):
    bar_width = int(float(value) / maximum * total_width)

    panel.draw_rect(x, y, total_width, 1, 0, bg=back_color, bg_blend=tcod.BKGND_SCREEN)

    if bar_width > 0:
        panel.draw_rect(x, y, bar_width, 1, 0, bg=bar_color, bg_blend=tcod.BKGND_SCREEN)

    panel.print(int(x + total_width / 2), y, '{0}: {1}/{2}'.format(name, value, maximum), tcod.white,
                alignment=tcod.CENTER)


def render_inventory(window, header, player):
    # show a menu with each item of the inventory as an option
    # window.draw_frame(0, 0, const.popup_width, const.popup_height, "Inventory")
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

    window_height = option_menu(window, header, options, const.inventory_width, const.screen_width, const.screen_height)
    window_width = const.inventory_width
    window_dsty = int(((const.screen_height - const.panel_height) - window_height) / 2)
    window = tcod.Console(window_width, window_height, order='F')
    window.draw_frame(0, 0, window_width, window_height, "Inventory")


# Temp function; may keep menus in the separate menus file:
def option_menu(window, header, options, window_width, screen_width, screen_height):
    if len(options) > 26:
        raise ValueError('Cannot have a menu with more than 26 options.')

    # calculate text width, assuming a border exists
    text_width = window_width - 2

    # calculate total height for the header (after auto-wrap) and one line per option
    header_height = window.get_height_rect(0, 0, text_width, screen_height - 2, header)  # Why reference screen_height?
    text_height = len(options) + header_height

    # calculate window height based on the calculated text height, assuming a border exists
    window_height = text_height + 2

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
    # x = int(screen_width / 2 - window_width / 2)
    # y = int(screen_height / 2 - window_height / 2)
    # window.blit(con, x, y, 0, 0, window_width, window_height, 1.0, 0.7)
    return window_height

# def info_menu():

