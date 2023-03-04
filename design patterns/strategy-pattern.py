from abc import ABC, abstractmethod

""" FlyBehaviour interface and its implementations """


class FlyBehaviour(ABC):
    """An interface for flying behaviour"""

    @abstractmethod
    def fly(self):
        """Each class will have different implementations"""
        pass


class FlyWithWings(FlyBehaviour):

    def fly(self):
        print('Fly..... With wings ! wings ! wings !')


class FlyWithRocket(FlyBehaviour):

    def fly(self):
        print('Fly..... With booster rocket ! rocket ! rocket !')


class NoFly(FlyBehaviour):

    def fly(self):
        print('No Fly..... Sit on ground !!!!!! !')


""" QuarkBehaviour interface and its implementations """


class QuarkBehaviour(ABC):
    """An interface for quark behaviour"""

    @abstractmethod
    def quark(self):
        """Each class will have different implementations"""
        pass


class StandardQuark(QuarkBehaviour):

    def quark(self):
        print("Quark ! Quark ! Quark !")


class SqueakQuark(QuarkBehaviour):

    def quark(self):
        print("Squeak ! Squeak ! Squeak !")


class MuteQuark(QuarkBehaviour):

    def quark(self):
        print("Mute ! Mute ! Mute !")


"""Base Abstract class"""


class Duck(ABC):

    def __init__(self, fly_behaviour, quark_behaviour):
        self._fly_behaviour = fly_behaviour
        self._quark_behaviour = quark_behaviour

    def perform_fly(self):
        self._fly_behaviour.fly()

    def perform_quark(self):
        self._quark_behaviour.quark()


""" Real implemented Duck classes """


class RubberDuck(Duck):
    pass


class DecoyDuck(Duck):
    pass


class MountainDuck(Duck):
    pass


class CityDuck(Duck):
    pass


if __name__ == '__main__':
    rd = RubberDuck(fly_behaviour=NoFly(), quark_behaviour=SqueakQuark())
    dd = DecoyDuck(fly_behaviour=NoFly(), quark_behaviour=MuteQuark())
    md = MountainDuck(fly_behaviour=FlyWithWings(), quark_behaviour=StandardQuark())
    cd = CityDuck(fly_behaviour=FlyWithRocket(), quark_behaviour=StandardQuark())

    print("Rubber Duck ")
    rd.perform_fly()
    rd.perform_quark()

    print("\nDecoy Duck ")
    dd.perform_fly()
    dd.perform_quark()

    print("\nMountain Duck ")
    md.perform_fly()
    md.perform_quark()

    print("\nCity Duck ")
    cd.perform_fly()
    cd.perform_quark()
