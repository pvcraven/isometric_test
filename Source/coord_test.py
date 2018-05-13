import unittest


def get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight):
    screen_x = tilewidth * (tile_x) // 2 + height * tilewidth // 2 - tile_y  * tilewidth // 2
    screen_y = (height - tile_y - 1) * tileheight // 2 + width * tileheight // 2 - tile_x * tileheight // 2
    return screen_x, screen_y


class TestStringMethods(unittest.TestCase):

    def test_01(self):
        tilewidth = 10
        tileheight = 10
        width = 1
        height = 1
        tile_x = 0
        tile_y = 0
        x, y = get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 5)
        self.assertEqual(y, 5)

    def test_02(self):
        tilewidth = 20
        tileheight = 10
        width = 1
        height = 1
        tile_x = 0
        tile_y = 0
        x, y = get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 10)
        self.assertEqual(y, 5)

    def test_03(self):
        tilewidth = 16
        tileheight = 16
        width = 2
        height = 1
        tile_x = 0
        tile_y = 0
        x, y = get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 8)
        self.assertEqual(y, 16)

        tile_x = 1
        tile_y = 0
        x, y = get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 16)
        self.assertEqual(y, 8)

    def test_04(self):
        tilewidth = 16
        tileheight = 16
        width = 1
        height = 2
        tile_x = 0
        tile_y = 0
        x, y = get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 16)
        self.assertEqual(y, 16)

        tile_x = 0
        tile_y = 1
        x, y = get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 8)
        self.assertEqual(y, 8)


if __name__ == '__main__':
    unittest.main()