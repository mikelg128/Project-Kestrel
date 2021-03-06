
import tcod

window_title = 'Roguelike Tutorial Revised'

screen_width = 80
screen_height = 50

hp_bar_width = 20
hp_bar_panel_dstx = 1
hp_bar_panel_dsty = 2

panel_height = 7
panel_width = screen_width
# panel_y = screen_height - panel_height
panel_dstx = 0
panel_dsty = screen_height - panel_height

overlay_height = screen_height - panel_height
overlay_width = screen_width
overlay_dstx = 0
overlay_dsty = 0

popup_width = 40
popup_height = 20
window_dstx = int((screen_width - popup_width)/2)
window_dsty = int(((screen_height - panel_height) - popup_height)/2)

message_panel_dstx = 22
message_width = screen_width - 22
message_height = panel_height - 2

# Inventory:
inventory_width = 50

# Lvl up menu:
lvlup_width = 40

# Character Screen:
char_screen_width = 30

map_width = 80
map_height = 43

room_max_size = 10
room_min_size = 6
max_rooms = 30

fov_algorithm = 0
fov_light_walls = True
fov_radius = 10

max_monsters_per_room = 3
max_items_per_room = 2

colors = {
    'dark_wall': tcod.Color(0, 0, 100),
    'dark_ground': tcod.Color(50, 50, 150),
    'light_wall': tcod.Color(130, 110, 50),
    'light_ground': tcod.Color(200, 180, 50)
}


# Not used right now, but might be useful to define all the constants in a class at some point, to make them more
# accessible. Right now, none of these constants are editable.
class Constants:
    screen_height = 50
    screen_width = 80
    panel_height = 10

