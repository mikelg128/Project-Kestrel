import tcod
from enum import Enum, auto
from game_states import GameStates
from menus import inventory_menu, level_up_menu, character_screen


class RenderOrder(Enum):
    STAIRS = auto()
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()


def get_names_under_mouse(mouse_tile, entities, fov_map):
    # (x, y) = mouse.tile
    x, y = mouse_tile[0], mouse_tile[1]
    names = [entity.name for entity in entities
             if entity.x == x and entity.y == y and tcod.map_is_in_fov(fov_map, entity.x, entity.y)]
    names = ', '.join(names)

    return names.capitalize()


def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color):
    bar_width = int(float(value) / maximum * total_width)

    panel.draw_rect(x, y, total_width, 1, 0, bg=back_color, bg_blend=tcod.BKGND_SCREEN)

    if bar_width > 0:
        panel.draw_rect(x, y, bar_width, 1, 0, bg=bar_color, bg_blend=tcod.BKGND_SCREEN)

    panel.print(int(x + total_width / 2), y, '{0}: {1}/{2}'.format(name, value, maximum), tcod.white,
                alignment=tcod.CENTER)


def render_all(con, panel, entities, player, game_map, fov_map, fov_recompute, message_log, screen_width, screen_height,
               bar_width, panel_height, panel_y, mouse_tile, colors, game_state):
    # Draw all the tiles in the game map
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = tcod.map_is_in_fov(fov_map, x, y)  # TODO: look into newer FOV functions
                wall = game_map.tiles[x][y].block_sight

                if visible:  # TODO: Use *.tiles_RGB() or similar to render game map
                    if wall:
                        tcod.console_set_char_background(con, x, y, colors.get('light_wall'), tcod.BKGND_SET)
                    else:
                        tcod.console_set_char_background(con, x, y, colors.get('light_ground'), tcod.BKGND_SET)
                    game_map.tiles[x][y].explored = True
                elif game_map.tiles[x][y].explored:
                    if wall:
                        tcod.console_set_char_background(con, x, y, colors.get('dark_wall'), tcod.BKGND_SET)
                    else:
                        tcod.console_set_char_background(con, x, y, colors.get('dark_ground'), tcod.BKGND_SET)

    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)

    # Draw all entities in the list
    for entity in entities_in_render_order:
        draw_entity(con, entity, fov_map, game_map)

    # con.blit(0, 0, screen_width, screen_height, 0, 0, 0)

    # Set panel to black and clear it
    panel.default_bg = tcod.black
    panel.clear()

    # Print the game messages, one line at a time
    y = 1
    for message in message_log.messages:
        panel.print(message_log.x, y, message.text, message.color, alignment=tcod.LEFT)
        y += 1

    # Render health bar:
    render_bar(panel, 1, 2, bar_width, 'HP', player.fighter.hp, player.fighter.max_hp, tcod.light_red,
               tcod.darker_red)
    # Print dungeon level:
    panel.print(1, 3, 'Dungeon level: {0}'.format(game_map.dungeon_level), tcod.white, alignment=tcod.LEFT)

    # Print names under mouse:
    panel.print(1, 1, get_names_under_mouse(mouse_tile, entities, fov_map), tcod.light_gray, alignment=tcod.LEFT)

    # Draw Panel Frame
    panel.draw_frame(0, 0, screen_width, panel_height, clear=False)

    # Blit panel to root console:
    panel.blit(con, 0, panel_y, 0, 0, screen_width, panel_height)

    if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        if game_state == GameStates.SHOW_INVENTORY:
            inventory_title = 'Press the key next to an item to use it, or Esc to cancel.\n'
        else:
            inventory_title = 'Press the key next to an item to drop it, or Esc to cancel.\n'

        inventory_menu(con, inventory_title, player, 50, screen_width, screen_height)
    elif game_state == GameStates.LEVEL_UP:
        level_up_menu(con, 'Level up! Choose a stat to raise:', player, 40, screen_width, screen_height)

    elif game_state == GameStates.CHARACTER_SCREEN:
        character_screen(con, player, 30, 10, screen_width, screen_height)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov_map, game_map):
    if tcod.map_is_in_fov(fov_map, entity.x, entity.y) \
            or (entity.stairs and game_map.tiles[entity.x][entity.y].explored):
        con.print(entity.x, entity.y, entity.char, entity.color)


def clear_entity(con, entity):
    # erase the character that represents this object
    tcod.console_put_char(con, entity.x, entity.y, ' ', tcod.BKGND_NONE)