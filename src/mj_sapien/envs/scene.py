import newton
class Scene:
    def __init__(self):
        pass
    def add_builder(self, builder):
        """
        Add a builder to the scene, which is used to construct a part of the scene
        """
        pass
    def finalize(self):
        """
        Finalize the scene and compile it, ready for simulation/rendering
        """


class NewtonScene(Scene):
    def __init__(self):
        super().__init__()
        self._newton_scene = newton.ModelBuilder()

    def add_builder(self, builder):
        self._newton_scene.add_builder(builder)

    def finalize(self):
        self._newton_scene.finalize()