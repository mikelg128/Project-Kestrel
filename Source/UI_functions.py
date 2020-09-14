import constants as const
import tcod
from game_states import GameStates
from menus import option_menu, info_menu


def render_ui(root, panel, overlay, game_state, message_log, player, dungeon_level, name_under_mouse):
    # Clear the UI consoles
    panel.clear()
    overlay.clear()

    # Game state logic
    if not game_state == GameStates.MAIN_MENU:
        # Currently, the MAIN_MENU game state is never called.
        render_panel(root, panel, message_log, player, dungeon_level, name_under_mouse)
        if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
            if game_state == GameStates.SHOW_INVENTORY:
                inventory_title = 'Press the key next to an item to use it, or Esc to cancel.\n'
            else:
                inventory_title = 'Press the key next to an item to drop it, or Esc to cancel.\n'
            render_inventory(overlay, inventory_title, player)
        elif game_state == GameStates.LEVEL_UP:
            render_lvlup(overlay, 'Level up! Choose a stat to raise:', player)
        elif game_state == GameStates.CHARACTER_SCREEN:
            render_char_screen(overlay, player)
        panel.blit(root, const.panel_dstx, const.panel_dsty, 0, 0, const.panel_width, const.panel_height, 1.0, 1.0)
        if not game_state in (GameStates.PLAYERS_TURN, GameStates.PLAYER_DEAD):
            overlay.blit(root, const.overlay_dstx, const.overlay_dsty, 0, 0, const.overlay_width, const.overlay_height,
                         1.0, 0.5)
    else:
        render_main_menu(root)


def render_panel(root, panel, message_log, player, dungeon_level, name_under_mouse):
    panel.draw_frame(0, 0, const.panel_width, const.panel_height)

    # Print the game messages, one line at a time
    y = 1
    for message in message_log.messages:
        panel.print(message_log.x, y, message.text, message.color, alignment=tcod.LEFT)
        y += 1

    # Render HP bar:
    render_bar(panel, const.hp_bar_panel_dstx, const.hp_bar_panel_dsty, const.hp_bar_width, 'HP', player.fighter.hp,
               player.fighter.max_hp, tcod.light_red, tcod.darker_red)

    # Print dungeon level:
    panel.print(1, 3, 'Dungeon level: {0}'.format(dungeon_level), tcod.white, alignment=tcod.LEFT)

    # Print names under mouse:
    panel.print(1, 1, name_under_mouse, tcod.light_gray, alignment=tcod.LEFT)


def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color):
    bar_width = int(float(value) / maximum * total_width)

    panel.draw_rect(x, y, total_width, 1, 0, bg=back_color, bg_blend=tcod.BKGND_SCREEN)

    if bar_width > 0:
        panel.draw_rect(x, y, bar_width, 1, 0, bg=bar_color, bg_blend=tcod.BKGND_SCREEN)

    panel.print(int(x + total_width / 2), y, '{0}: {1}/{2}'.format(name, value, maximum), tcod.white,
                alignment=tcod.CENTER)


def render_inventory(con, header, player):
    # show a menu with each item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = []
        # Checks for equipped items
        for item in player.inventory.items:
            if player.equipment.main_hand == item:
                options.append('{0} (on main hand)'.format(item.name))
            elif player.equipment.off_hand == item:
                options.append('{0} (on off hand)'.format(item.name))
            else:
                options.append(item.name)

    window_dstx, window_dsty, window_height = option_menu(con, header, options, const.inventory_width,
                                                          const.overlay_width, const.overlay_height)
    con.draw_frame(window_dstx, window_dsty, const.inventory_width, window_height, "Inventory", clear=False)


def render_lvlup(con, header, player):
    options = ['Constitution (+20 HP, from {0})'.format(player.fighter.max_hp),
               'Strength (+1 attach, from {0}'.format(player.fighter.power),
               'Agility (+1 Defense, from {0}'.format(player.fighter.defense)]

    window_dstx, window_dsty, window_height = option_menu(con, header, options, const.lvlup_width, const.overlay_width,
                                                          const.overlay_height)
    con.draw_frame(window_dstx, window_dsty, const.lvlup_width, window_height, "Level Up!", clear=False)


def render_char_screen(con, player):
    info_list = ['Character Screen',
                 'Level: {0}'.format(player.level.current_level),
                 'Experience: {0}'.format(player.level.current_xp),
                 'Experience to Level: {0}'.format(player.level.experience_to_next_level),
                 'Maximum HP: {0}'.format(player.fighter.max_hp),
                 'Attack: {0}'.format(player.fighter.power),
                 'Defense: {0}'.format(player.fighter.defense)
                 ]

    window_dstx, window_dsty, window_height = info_menu(con, info_list, const.char_screen_width, const.overlay_width,
                                                        const.overlay_height)
    con.draw_frame(window_dstx, window_dsty, const.char_screen_width, window_height, "Character Screen", clear=False)


def render_main_menu(con):
    con.print(int(const.screen_width / 2), int(const.screen_height / 2) - 6, '[Project Kestrel]', tcod.light_yellow,
              alignment=tcod.CENTER)
    con.print(int(const.screen_width / 2), int(const.screen_height / 2) - 5, 'by Michael Greer & Samar Mathur',
              tcod.light_yellow, alignment=tcod.CENTER)

    option_menu(con, '', ['Play a new game', 'Continue last game', 'Quit'], 24, const.screen_width, const.screen_height)
