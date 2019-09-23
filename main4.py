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
        self.tree_list = arcade.SpriteList()


    def setup(self):
        trees = ['tree1','tree2','tree3','tree4','tree5','tree6','tree7','tree8','tree9','tree10']

        for i in range(20):
            tree = random.choice(trees)
            x = random.randint(0,800)
            y = random.randint(0,600)
            self.tree_sprite = arcade.Sprite("PNG/{tree}.png".format(tree=tree), 0.5)
            self.tree_sprite.center_x = x
            self.tree_sprite.center_y = y
            self.tree_list.append(self.tree_sprite)     

    def on_draw(self):
        arcade.start_render()
        self.tree_list.draw()
        pass


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        for i in self.tree_list:
            self.tree_sprite.center_x = x
            self.tree_sprite.center_y = y
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()