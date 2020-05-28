class GameMenu:


    def __init__(self, options, title=""):
        self.options = options
        self.title = title


    def options_string(self):
        menu_string = ""
        indexed_options = list(enumerate(self.options))
        for index, option in indexed_options:
            menu_string += f"[{index+1}] {option['text']}\n"
        return menu_string


    def menu_do(self, choice, *attr):
        choice -= 1
        self.options[choice]["command"](*attr)

