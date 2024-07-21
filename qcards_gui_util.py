class QCardsGUIUtil:

    # Calculate the position of the center of the screen
    def calculate_window_center(self, x, y, screen_width, screen_height):
        x = (screen_width // 2) - (x // 2)
        y = (screen_height // 2) - (y // 2)
        return (x, y)
