class Bird:
    def fly(self):
        return "I can fly!"


class Eagle(Bird):
    def fly(self):
        return "I can fly high!"


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("I cannot fly!")


def make_bird_fly(bird: Bird):
    return bird.fly()


eagle = Eagle()
print(make_bird_fly(eagle))

penguin = Penguin()
print(make_bird_fly(penguin))
