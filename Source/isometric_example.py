"""
Example code showing Isometric Grid coordinates
"""

import arcade
import os

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

MAP_WIDTH = 5
MAP_HEIGHT = 4
TILE_WIDTH = 128
TILE_HEIGHT = 128


def get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight):
    screen_x = tilewidth * tile_x // 2 + height * tilewidth // 2 - tile_y * tilewidth // 2
    screen_y = (height - tile_y - 1) * tileheight // 2 + width * tileheight // 2 - tile_x * tileheight // 2
    return screen_x, screen_y


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.axis_shape_list = None
        self.isometric_grid_shape_list = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Set the background color
        arcade.set_background_color((50, 50, 50))

        self.axis_shape_list = arcade.ShapeElementList()

        # Axis
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = SCREEN_HEIGHT
        line = arcade.create_line(start_x, start_y, end_x, end_y, arcade.color.WHITE, 2)
        self.axis_shape_list.append(line)

        # Axis
        start_x = 0
        start_y = 0
        end_x = SCREEN_WIDTH
        end_y = 0
        line = arcade.create_line(start_x, start_y, end_x, end_y, arcade.color.WHITE, 2)
        self.axis_shape_list.append(line)

        # x Tic Marks
        for x in range(0, SCREEN_WIDTH, 64):
            start_y = -10
            end_y = 0
            line = arcade.create_line(x, start_y, x, end_y, arcade.color.WHITE, 2)
            self.axis_shape_list.append(line)

        # y Tic Marks
        for y in range(0, SCREEN_HEIGHT, 64):
            start_x = -10
            end_x = 0

            line = arcade.create_line(start_x, y, end_x, y, arcade.color.WHITE, 2)
            self.axis_shape_list.append(line)

        tilewidth = TILE_WIDTH
        tileheight = TILE_HEIGHT
        width = MAP_WIDTH
        height = MAP_HEIGHT

        # Gridlines 1
        for tile_row in range(-1, height):
            tile_x = 0
            start_x, start_y = get_screen_coordinates(tile_x, tile_row, width, height, tilewidth, tileheight)
            tile_x = width - 1
            end_x, end_y = get_screen_coordinates(tile_x, tile_row, width, height, tilewidth, tileheight)

            start_x -= tilewidth // 2
            end_y -= tileheight // 2

            line = arcade.create_line(start_x, start_y, end_x, end_y, arcade.color.WHITE)
            self.axis_shape_list.append(line)

        # Gridlines 2
        for tile_column in range(-1, width):
            tile_y = 0
            start_x, start_y = get_screen_coordinates(tile_column, tile_y, width, height, tilewidth, tileheight)
            tile_y = height - 1
            end_x, end_y = get_screen_coordinates(tile_column, tile_y, width, height, tilewidth, tileheight)

            start_x += tilewidth // 2
            end_y -= tileheight // 2

            line = arcade.create_line(start_x, start_y, end_x, end_y, arcade.color.WHITE)
            self.axis_shape_list.append(line)

        for tile_x in range(width):
            for tile_y in range(height):
                screen_x, screen_y = get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight)
                point_width = 3
                point_height = 3
                point = arcade.create_rectangle_filled(screen_x, screen_y, point_width, point_height, arcade.color.LIGHT_CORNFLOWER_BLUE, 3)
                self.axis_shape_list.append(point)
                print(f"{tile_x}, {tile_y} => {screen_x:3}, {screen_y:3}")


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()


        self.axis_shape_list.draw()

        # x Labels
        for x in range(0, SCREEN_WIDTH, 64):
            text_y = -25
            arcade.draw_text(f"{x}", x, text_y, arcade.color.WHITE, 12, width=200, align="center",
                         anchor_x="center")

        # y Labels
        for y in range(0, SCREEN_HEIGHT, 64):
            text_x = -50
            arcade.draw_text(f"{y}", text_x, y - 4, arcade.color.WHITE, 12, width=70, align="right",
                         anchor_x="center")


        tilewidth = TILE_WIDTH
        tileheight = TILE_HEIGHT
        width = MAP_WIDTH
        height = MAP_HEIGHT

        for tile_x in range(width):
            for tile_y in range(height):
                screen_x, screen_y = get_screen_coordinates(tile_x, tile_y,
                                                            width, height,
                                                            tilewidth, tileheight)
                arcade.draw_text(f"{tile_x}, {tile_y}",
                                 screen_x, screen_y + 6,
                                 arcade.color.WHITE, 12,
                                 width=200, align="center", anchor_x="center")

    def update(self, delta_time):
        view_left = -50
        view_bottom = -50
        arcade.set_viewport(view_left,
                            SCREEN_WIDTH + view_left,
                            view_bottom,
                            SCREEN_HEIGHT + view_bottom)

    def on_mouse_press(self, x: float, y: float):
        screen_x = x + self.view_left
        screen_y = y + self.view_bottom

        grid_x = screen_x // TILE_WIDTH
        grid_y = screen_y // TILE_HEIGHT
        point_x = (screen_x % TILE_WIDTH) - (TILE_WIDTH / 2)
        point_y = (screen_y % TILE_HEIGHT) - (TILE_HEIGHT / 2)


        # print(f"({screen_x}, {screen_y}) -> ({map_x:.2}, {map_y:.2})")


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
