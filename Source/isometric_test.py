"""
"""

import arcade
import os

SPRITE_SCALING = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5
MAP_WIDTH = 5
MAP_HEIGHT = 15
TILE_WIDTH = 64
TILE_HEIGHT = 64


def get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight):
    screen_x = tilewidth * (tile_x) // 2 + height * tilewidth // 2 - tile_y  * tilewidth // 2
    screen_y = (height - tile_y - 1) * tileheight // 2 + width * tileheight // 2 - tile_x * tileheight // 2
    return screen_x, screen_y


def read_sprite_list(grid, sprite_list):
    for row in grid:
        for grid_location in row:
            if grid_location.tile is not None:
                tile_sprite = arcade.Sprite(grid_location.tile.source, SPRITE_SCALING)
                tile_sprite.center_x = grid_location.center_x * SPRITE_SCALING
                tile_sprite.center_y = grid_location.center_y * SPRITE_SCALING
                # print(f"({tile_sprite.center_x:4}, {tile_sprite.center_y:4})")
                sprite_list.append(tile_sprite)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        """
        Initializer
        """
        super().__init__(width, height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.wall_list = None
        self.wood_list = None
        self.objects_list = None
        self.second_list = None
        self.view_bottom = 0
        self.view_left = 0
        self.my_map = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.floor_list = arcade.SpriteList()
        self.wood_list = arcade.SpriteList()
        self.objects_list = arcade.SpriteList()
        self.second_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite("../images/character.png", 0.4)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 0
        self.all_sprites_list.append(self.player_sprite)

        self.my_map = arcade.read_tiled_map('../Tiled/tiledTemplate_isometric.tmx')

        read_sprite_list(self.my_map.layers["Floor"], self.floor_list)
        # read_sprite_list(self.my_map.layers["Walls"], self.wall_list)
        # read_sprite_list(self.my_map.layers["Wood"], self.wood_list)
        # read_sprite_list(self.my_map.layers["Objects"], self.objects_list)
        # read_sprite_list(self.my_map.layers["Second"], self.second_list)

        # Set the background color
        arcade.set_background_color(self.my_map.backgroundcolor)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        # self.floor_list.draw()
        # self.wall_list.draw()
        # self.wood_list.draw()
        # self.objects_list.draw()
        # self.player_sprite.draw()
        # self.second_list.draw()

        # self.my_map.width = 2
        # for row_number in range(self.my_map.width):
        #
        #     start_x = self.my_map.tilewidth // 2 * self.my_map.width + self.my_map.tilewidth // 2 * row_number
        #     start_y = self.my_map.tilewidth // 2 * row_number
        #     end_x = self.my_map.tilewidth // 2 * row_number
        #     end_y = self.my_map.tileheight // 2 * self.my_map.height + self.my_map.tilewidth // 2 * row_number
        #     arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.WHITE, 2)
        #
        # start_x = self.my_map.tilewidth // 2 * self.my_map.width
        # start_y = 0
        # end_x = self.my_map.tilewidth // 2 * self.my_map.width * 2
        # end_y = self.my_map.tileheight // 2 * self.my_map.height
        # arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.LIGHT_CYAN, 2)

        tilewidth = TILE_WIDTH
        tileheight = TILE_HEIGHT
        width = MAP_WIDTH
        height = MAP_HEIGHT

        # Axis
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 1000
        arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.WHITE, 2)

        # Axis
        start_x = 0
        start_y = 0
        end_x = 1000
        end_y = 0
        arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.WHITE, 2)

        # Gridlines 1
        for tile_row in range(-1, height):
            tile_x = 0
            start_x, start_y = get_screen_coordinates(tile_x, tile_row, width, height, tilewidth, tileheight)
            tile_x = width - 1
            end_x, end_y = get_screen_coordinates(tile_x, tile_row, width, height, tilewidth, tileheight)

            start_x -= tilewidth // 2
            end_y -= tileheight // 2

            arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.WHITE)

        # Gridlines 2
        for tile_column in range(-1, width):
            tile_y = 0
            start_x, start_y = get_screen_coordinates(tile_column, tile_y, width, height, tilewidth, tileheight)
            tile_y = height - 1
            end_x, end_y = get_screen_coordinates(tile_column, tile_y, width, height, tilewidth, tileheight)

            start_x += tilewidth // 2
            end_y -= tileheight // 2

            arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.WHITE)


        for tile_x in range(width):
            for tile_y in range(height):
                screen_x, screen_y = get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight)
                if tile_x == 0 and tile_y == 0:
                    color = arcade.color.GREEN
                elif tile_x == 1 and tile_y == 0:
                    color = arcade.color.AFRICAN_VIOLET
                else:
                    color = arcade.color.RED
                arcade.draw_point(screen_x, screen_y, color, 3)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        screen_x = x + self.view_left
        screen_y = y + self.view_bottom
        tile_width_half = self.my_map.tilewidth
        tile_height_half = self.my_map.tileheight
        map_x = (screen_x / tile_width_half + (screen_y / tile_height_half)) / 2
        map_y = (screen_y / tile_height_half - (screen_x / tile_width_half)) / 2

        # print(f"({screen_x}, {screen_y}) -> ({map_x:.2}, {map_y:.2})")

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.player_sprite.update()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
