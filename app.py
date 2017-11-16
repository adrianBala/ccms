from root_controller import RootController


class App():

    def __init__(self):
        self.root_controller = RootController()

    def main(self):
        self.root_controller.start()


if __name__ == '__main__':
    app = App()
    app.main()
