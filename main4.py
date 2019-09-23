#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)
        self.car_list = arcade.SpriteList()


    def setup(self):
        cars = ['bus','kart','police','buggy','ambulance','bus_school','hotdog','scooter','station','cycle']

        for i in range(20):
            car = random.choice(cars)
            x = random.randint(0,800)
            y = random.randint(0,600)
            self.car_sprite = arcade.Sprite("Cars/{car}.png".format(car=car), 0.5)
            self.car_sprite.center_x = x
            self.car_sprite.center_y = y
            self.car_list.append(self.car_sprite)     

    def on_draw(self):
        arcade.start_render()
        self.car_list.draw()
        pass


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        for i in self.car_list:
            self.car_sprite.center_x = x
            self.car_sprite.center_y = y
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()