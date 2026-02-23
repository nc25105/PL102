import Project.test.modules.BulletManager as BulletManager
import Project.test.modules.EnemyManager as EnemyManager
import Project.test.modules.PlayerManager as PlayerManager

class physicsObject():
    def __init__(self, x = 0, y = 0, xv = 0, yv = 0, friction = 500):
        self.xv = xv
        self.yv = yv
        self.x = x
        self.y = y
        self.friction = friction
    def simulateVelocity(self, deltaTime):
        speed = (self.xv**2 + self.yv**2) ** 0.5

        if speed > 0:
            ax = -self.xv / speed * self.friction
            ay = -self.yv / speed * self.friction

            new_xv = self.xv + ax * deltaTime
            new_yv = self.yv + ay * deltaTime

            if self.xv * new_xv < 0:
                self.xv = 0
            else:
                self.xv = new_xv

            if self.yv * new_yv < 0:
                self.yv = 0
            else:
                self.yv = new_yv

        self.x += self.xv * deltaTime
        self.y += self.yv * deltaTime

class gameObject:
    def __init__(self, zindex:int = 0, x = 0, y = 0, hasPhysics:bool = True):
        self.zindex = zindex
        self.hasPhysicsProperties = hasPhysics
        self.x = x
        self.y = y
        if hasPhysics:
            self.physicsInstance = physicsObject(self.x, self.y)

        

def advanceStep(deltaTime, objects):
    for _object in objects:
        if isinstance(_object, physicsObject):
            _object.simulateVelocity(deltaTime)

def renderFrame(objects):
    for _object in objects:
        