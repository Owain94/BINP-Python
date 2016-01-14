class Hero:
    @staticmethod
    def say_hello():
        print("Helllo...")

    @classmethod
    def say_class_hello(cls):
        if cls.__name__ == "HeroSon":
            print("Hi Kido")
        elif cls.__name__ == "HeroDaughter":
            print("Hi Princess")


class HeroSon(Hero):
    @staticmethod
    def say_son_hello():
        print("test  hello")


class HeroDaughter(Hero):
    @staticmethod
    def say_daughter_hello():
        print("test  hello daughter")


testson = HeroSon()

testson.say_class_hello()

testson.say_hello()

testdaughter = HeroDaughter()

testdaughter.say_class_hello()

testdaughter.say_hello()
