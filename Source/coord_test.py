import unittest


def get_screen_coordinates(tile_x, tile_y, width, height, tilewidth, tileheight):
    screen_x = tilewidth * tile_x // 2 + height * tilewidth // 2 - tile_y  * tilewidth // 2
    screen_y = (height - tile_y - 1) * tileheight // 2 + width * tileheight // 2 - tile_x * tileheight // 2
    return screen_x, screen_y


def get_tile_coordinates(x1, y1):
    x2 = (x1 - y1) / 2
    y2 = (x1 + y1) / 2
    print(f"{x1}, {y1} => {x2}, {y2}")


def get_tile_coordinates2(screen_x, screen_y, width=0, height=0, tilewidth=1, tileheight=1):
    x2 = tilewidth * (screen_x / 2 - screen_y / 2) + width / 2
    y2 = tileheight * (screen_x / 2 + screen_y / 2)
    print(f"{screen_x}, {screen_y} => {x2}, {y2}")


class TestScreenCoordinateMethods(unittest.TestCase):

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


def get_tile_coordinates(screen_x, screen_y, width, height, tilewidth, tileheight):
    hw = tilewidth // 2
    hh = tileheight // 2
    tile_x = width - (screen_x / hw)
    tile_y = height - ((screen_y / hh) + 1) // 2
    return int(tile_x), int(tile_y)


class TestTileCoordinateMethods(unittest.TestCase):

    def test_01(self):
        tilewidth = 16
        tileheight = 16
        width = 1
        height = 1
        screen_x = 8
        screen_y = 8
        x, y = get_tile_coordinates(screen_x, screen_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

    def test_02(self):
        tilewidth = 64
        tileheight = 64
        width = 2
        height = 2
        screen_x = 64
        screen_y = 96
        x, y = get_tile_coordinates(screen_x, screen_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

    def test_03(self):
        tilewidth = 64
        tileheight = 64
        width = 3
        height = 3
        screen_x = 96
        screen_y = 160
        x, y = get_tile_coordinates(screen_x, screen_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

    def test_04(self):
        tilewidth = 64
        tileheight = 64
        width = 3
        height = 3
        screen_x = 64
        screen_y = 128
        x, y = get_tile_coordinates(screen_x, screen_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)

    def test_05(self):
        tilewidth = 64
        tileheight = 64
        width = 5
        height = 1

        screen_x = 32
        screen_y = 160
        x, y = get_tile_coordinates(screen_x, screen_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

        screen_x = 64
        screen_y = 128
        x, y = get_tile_coordinates(screen_x, screen_y, width, height, tilewidth, tileheight)
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)


if __name__ == '__main__':
    unittest.main()