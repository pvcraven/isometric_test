"""
"""

import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5


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

    def read_sprite_list(self, grid, sprite_list):
        row_count = 0
        for row in grid:
            column_count = 0
            for tile_id in row:
                key = str(tile_id)
                if key in self.my_map.global_tile_set:
                    tile_info = self.my_map.global_tile_set[str(tile_id)]
                    tile_sprite = arcade.Sprite(tile_info.source)

                    tile_sprite.center_x = (column_count - row_count) * (self.my_map.tilewidth // 2)
                    tile_sprite.center_y = 1000 - (column_count + row_count) * (self.my_map.tileheight // 2)

                    sprite_list.append(tile_sprite)
                column_count += 1
            row_count += 1

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
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.all_sprites_list.append(self.player_sprite)

        self.my_map = arcade.read_tiled_map('../Tiled/tiledTemplate_isometric.tmx')

        self.read_sprite_list(self.my_map.layers["Floor"], self.floor_list)
        self.read_sprite_list(self.my_map.layers["Walls"], self.wall_list)
        self.read_sprite_list(self.my_map.layers["Wood"], self.wood_list)
        self.read_sprite_list(self.my_map.layers["Objects"], self.objects_list)
        self.read_sprite_list(self.my_map.layers["Second"], self.second_list)

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
        self.floor_list.draw()
        self.wall_list.draw()
        self.wood_list.draw()
        self.objects_list.draw()
        self.player_sprite.draw()
        self.second_list.draw()

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
