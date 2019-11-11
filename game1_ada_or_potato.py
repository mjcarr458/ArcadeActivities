import arcade
# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60
TIMER_MAX = 100
IMAGE_ADA = arcade.load_texture("images/ada.png")
IMAGE_POTATO = arcade.load_texture("images/potato.png")
PHASE = {
        "fail":"pass",
        "pass":"fail"
}


class AdaPotato(arcade.Sprite):
    timer: int
    test: bool


    def __init__(self):
        super().__init__()
        self.phase = "pass"
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.texture = IMAGE_ADA
        self.timer = 0
        self.test = None

    def update_timer(self):
        if self.timer < TIMER_MAX:
            self.timer += 1
        else:
            self.timer = 0
            self.phase = PHASE[self.phase]

    def update(self):
        if self.phase == "pass":
            self.test = True
        elif self.phase == "fail":
            self.test = False
        self.update_timer()
        self.swap_image()
        self.test_option()

    def swap_image(self):
        if self.timer <= 50:
            self.texture = IMAGE_POTATO
        else:
            self.texture = IMAGE_ADA


    def test_option(self):
        if self.test:
            return True
        else:
            return False


AP = AdaPotato()
class MainGame(arcade.Window, AdaPotato):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None
        self.score = 0
        self.timer = AP.timer

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
        print(AP.test_option())
        if AP.test_option():
            print("end1")
        else:
            print("end2")


def main():
    window = MainGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()