from entities.entity import Entity

class Entity1(Entity):
    def __init__(self, screen):
        super().__init__(screen)
        print("entity1 load")

class Entity2(Entity):
    def __init__(self, screen):
        super().__init__(screen)
        print("entity2 load")