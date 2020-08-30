import Tests.constants as const
import tcod


def render_ui(root, panel, overlay, game_state, message_log, player, dungeon_level, name_under_mouse):
    render_panel(root, panel, message_log, player, dungeon_level, name_under_mouse)
    if game_state == 2:
        render_overlay(root, overlay)


def render_panel(root, panel, message_log, player, dungeon_level, name_under_mouse):
    # panel.default_bg = tcod.black
    panel.clear()

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

    panel.blit(root, const.panel_dstx, const.panel_dsty, 0, 0, const.panel_width, const.panel_height, 1.0, 1.0)


def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color):
    bar_width = int(float(value) / maximum * total_width)

    panel.draw_rect(x, y, total_width, 1, 0, bg=back_color, bg_blend=tcod.BKGND_SCREEN)

    if bar_width > 0:
        panel.draw_rect(x, y, bar_width, 1, 0, bg=bar_color, bg_blend=tcod.BKGND_SCREEN)

    panel.print(int(x + total_width / 2), y, '{0}: {1}/{2}'.format(name, value, maximum), tcod.white,
                alignment=tcod.CENTER)


def render_overlay(overlay, root):
    overlay.draw_frame(0, 0, const.popup_width, const.popup_height, "Pop-Up Window")
    overlay.print(int(const.popup_width / 2), int(const.popup_height / 2), "This is a pop up window", tcod.white,
                  alignment=tcod.CENTER)

    overlay.blit(root, const.popup_dstx, const.popup_dsty, 0, 0, const.popup_width, const.popup_height)


