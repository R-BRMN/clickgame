import mouse
import time


class ClickGame:
    """
    ClickGame objects are capable of playing a clicking game with a user.
    
    The game tests the time it takes the user to get from a corner on their
    screen to a target area on the screen[1] and click it.

    [1] The rectangle currently has no visual representation on the screen.
    """
    def __init__(self):
        self.start_position = ()
        self.target_area_corners = []
        self.prepare_game()


    def prepare_game(self):
        """
        Resets variables to setup a new game.
        """
        self.launch_time = None
        self.result_time = 0


    def callback_start_position_registrar(self):
        """
        Set starting point to mouse position
        """
        self.start_position = mouse.get_position()


    def register_start_position(self):
        """
        Register next mouse click as the starting point
        """
        callback = mouse.on_click(self.callback_start_position_registrar)
        self.start_position = None
        while self.start_position == None:
            pass
        mouse.unhook(callback)


    def callback_corner_position_registrar(self):
        """
        Set a bounds corner at mouse position.
        """
        self.target_area_corners.append(mouse.get_position())


    def register_corner(self):
        """
        Register next mouse click as a bounds corner.
        """
        callback = mouse.on_click(self.callback_corner_position_registrar)
        corners_logged = len(self.target_area_corners)
        while len(self.target_area_corners) == corners_logged:
            pass
        mouse.unhook(callback)


    def prepare_bounds(self):
        """
        Set bounds around target rectangle.
        """
        pointA, pointB = self.target_area_corners

        self.left_bound = min(pointA[0], pointB[0])
        self.right_bound = max(pointA[0], pointB[0])
        self.bottom_bound = min(pointA[1], pointB[1])
        self.top_bound = max(pointA[1], pointB[1])


    def mouse_is_in_bounds(self):
        """
        Checks if mouse is inside the bounds of the target rectangle.
        """
        mouse_x, mouse_y = mouse.get_position()
        if mouse_x > self.left_bound and mouse_x < self.right_bound:
            if mouse_y > self.bottom_bound and mouse_y < self.top_bound:
                return True


    def launch(self):
        """
        Interactive interface which takes the time as soon as the mouse leaves
        the starting point.
        """
        print ("Ready..")
        # Wait for mouse to arrive at starting point
        while mouse.get_position() != self.start_position:
            pass
        print ("Set..")
        # Wait for mouse to leave the starting point
        while mouse.get_position() == self.start_position:
            pass
        print ("Go!")
        self.launch_time = time.time()


    def act_click(self):
        """
        Sets time of arrival at target rectangle if mouse is in bounds.
        """
        click_time = time.time()
        if self.mouse_is_in_bounds():
            self.result_time = click_time - self.launch_time


    def await_click_in_bounds(self):
        """
        Listen for a click inside the target rectangle, and register the result.
        """
        callback = mouse.on_click(self.act_click)
        while not self.result_time:
            pass
        mouse.unhook(callback)


    def play_game(self):

        self.prepare_game()

        print ("Choose starting position")
        self.register_start_position()
        print (f"Your starting position is: {self.start_position}")

        print ("Please choose first corner of destination")
        self.register_corner()
        print ("Please choose second corner of destination")
        self.register_corner()
        self.prepare_bounds()

        self.launch()
        self.await_click_in_bounds()
        print (self.result_time)


if __name__ == '__main__':
    clickgame = ClickGame()
    clickgame.play_game()
