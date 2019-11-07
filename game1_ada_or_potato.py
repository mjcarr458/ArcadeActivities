import arcade
# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60
TIMER_MAX = 60
IMAGE_ADA = arcade.load_texture("images/ada.png")
IMAGE_POTATO = arcade.load_texture("images/potato.png")

class AdaPotato(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__()
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.texture = IMAGE_ADA
        self.timer = 0

    def update_timer(self):
        if self.timer < TIMER_MAX:
            self.timer += 1
        else:
            self.timer = 0

    def update(self):
        self.update_timer()

    def swap_image(self):
        if self.texture == IMAGE_POTATO:
            self.texture = IMAGE_ADA
        else:
            self.texture = IMAGE_POTATO



class MainGame(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(AdaPotato())


    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.logo_list.draw()

    def on_update(self, delta_time):
        self.logo_list.update()
        """ Called every frame of the game (1/GAME_SPEED times per second)"""

    def on_mouse_press(self, x: float, y: float, button: int, modifiers:int):
        for logo in self.logo_list:
            logo.swap_image()


def main():
    window = MainGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()