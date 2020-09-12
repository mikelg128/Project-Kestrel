import tcod

def changeResolution(resolution_width, resolution_height, tileset_width, tileset_height,tileset, name,fullscreenFlag):
    screen_width = int(resolution_width / tileset_width)
    screen_height = int(resolution_height / tileset_height)
    context = tcod.context.new_terminal(screen_width, screen_height, tileset=tileset,title=name, vsync=True, )
    root_console = tcod.Console(screen_width, screen_height, order="F")
    if fullscreenFlag == 1:
        tcod.lib.SDL_SetWindowFullscreen(context.sdl_window_p, tcod.lib.SDL_WINDOW_FULLSCREEN_DESKTOP)

    return root_console, context

def main() -> None:
    """Script entry point."""
    tileset = tcod.tileset.load_tilesheet(
        "source/assets/arial10x10.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    tileset1 = tcod.tileset.load_tilesheet(
        "source/assets/terminal16x16_gs_ro.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )


    resolution_width = 720
    resolution_height = 360
    tileset_width = 10
    tileset_height = 10
    fullscreenFlag = 0
    name = 'resolution test'
    root_console, context = changeResolution(resolution_width, resolution_height, tileset_width, tileset_height, tileset, name, fullscreenFlag)

    while True:
        root_console.print(x=1, y=1, string="@")

        context.present(root_console)

        for event in tcod.event.wait():
            #if event.type == "QUIT":
            #    raise SystemExit()
            if event.type == "KEYDOWN":
                fullscreenFlag =0
                tileset_width = 16
                tileset_height = 16
                resolution_width1 = 720
                resolution_height1 = 360
                name = 'resolution text resize'
                root_console, context = changeResolution(resolution_width1, resolution_height1, tileset_width,
                                                         tileset_height, tileset1, name, fullscreenFlag)
            if event.type == "QUIT":
                fullscreenFlag =1
                tileset_width = 16
                tileset_height = 16
                resolution_width2 = int(720*3)
                resolution_height2 = int(360*3)
                name = 'resolution text resize1'
                root_console, context = changeResolution(resolution_width2, resolution_height2, tileset_width,
                                                         tileset_height, tileset1, name, fullscreenFlag)



if __name__ == '__main__':
    main()