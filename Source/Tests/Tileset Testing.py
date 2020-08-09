import tcod as tcod
from typing import List

def main():
    screen_width = 80
    screen_height = 50
    window_title = 'UI Testing'

    tileset = tcod.tileset.load_tilesheet('../assets/arial10x10.png', 32, 8, tcod.tileset.CHARMAP_TCOD)
    main_loop_count = 0
    event_log: List[str] = []
    j = 0
    characters = tcod.tileset.CHARMAP_TCOD
    # Create a new terminal:
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title=window_title,
            vsync=True
    ) as context:
        # Create the root console:
        console = tcod.Console(*context.recommended_console_size())

        while True:
            # console.print(30, 20, 'Hello World', tcod.white, alignment=tcod.CENTER)
            console.clear()
            for i, item in enumerate(event_log[::-1]):
                y = console.height - 3 - i
                if y < 0:
                    break
                console.print(0, y, item)

            context.present(console, integer_scaling=True)

            # for character in tcod.tileset.CHARMAP_TCOD:
            #     tileset_char = 'Character # {0}: '.format(character) + chr(character)
            #     event_log.append(tileset_char)

            for event in tcod.event.wait():
                if event.type == 'QUIT':
                    raise SystemExit()
                elif event.type == 'KEYDOWN':
                    tileset_char = 'Character Number {0}: '.format(characters[j]) + chr(characters[j])
                    print(tileset_char)
                    event_log.append(tileset_char)
                    tileset_char = tileset_char + '\n'
                    with open('Arial_Char_map.txt', 'ab') as f:
                        f.write(tileset_char.encode('utf8'))
                        f.close()

                    j += 1


if __name__ == "__main__":
    main()