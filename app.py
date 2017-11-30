from controller.root_controller import RootController


class App():

    def __init__(self):
        self.root_controller = RootController()

    def run(self):
        self.root_controller.start()


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
