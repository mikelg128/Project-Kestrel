import tcod
from enum import Enum, auto
from UI_functions import render_ui


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


def render_all(con, panel, overlay, entities, player, game_map, fov_map, fov_recompute, message_log, mouse_tile, colors,
               game_state):
    # Draw all the tiles in the game map;
    #   This code block could be condensed into a standalone function for "rendering game map" that outputs to its
    #   own console, which then flows to the root console.
    if fov_recompute:  # This currently doesn't mean much, because it's always true iirc
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
    #   More game map work, could be included in the game map specific render functions
    for entity in entities_in_render_order:
        draw_entity(con, entity, fov_map, game_map)

    # New UI function:
    render_ui(con, panel, overlay, game_state, message_log, player, game_map.dungeon_level, get_names_under_mouse(
        mouse_tile, entities, fov_map))


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