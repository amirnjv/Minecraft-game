class Scene:
    """
    Base scene class
    """

    def __init__(self, engine: "Engine"):
        self.engine = engine

    def update(self):
        """
        Scene updating
        """
        pass

    def draw(self):
        """
        Scene rendering
        """
        pass