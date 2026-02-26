from entities.trigger import Trigger

class Entity1(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        print("entity1 load")
        self.rect.x = 450
    
    def whenCollided(self):
        self.screen.tm.loadMap("u1")
        self.screen.player1.pos.x = 80 * 5.5
        self.screen.player1.pos.y = 80 * 7.5

class Entity2(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        print("entity2 load")
        self.rect.x, self.rect.y = 900, 320
    
    def whenCollided(self):
        self.screen.tm.loadMap("r1")
        self.screen.player1.pos.x = 80 * 0.5
        self.screen.player1.pos.y = 80 * 3.5