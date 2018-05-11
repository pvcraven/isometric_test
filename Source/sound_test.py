import arcade

arcade.open_window(600, 600, "Hi")

s = arcade.load_sound("Hi.wav")
arcade.play_sound(s)

arcade.run()