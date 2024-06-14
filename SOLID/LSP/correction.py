class Bird:
    def move(self):
        return "I can move!"


class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"


class Eagle(FlyingBird):
    def fly(self):
        return "I can fly high!"


class Penguin(Bird):
    def move(self):
        return "I can swim!"


def make_bird_fly(bird: FlyingBird):
    return bird.fly()


eagle = Eagle()
print(make_bird_fly(eagle))
print(eagle.fly())

penguin = Penguin()
print(make_bird_fly(penguin))
