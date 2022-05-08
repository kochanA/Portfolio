from abc import ABC


class Item(ABC):

    def __init__(self):
        self.available_observer = AvailableObserver()
        self.promotion_observer = PromotionObserver()
        self.last_remained_observer = LastRemainedObserver()


class Shooses(Item):

    def __init__(self):
        super().__init__()
        self._state = None

    def make_available(self):
        self._state = "available"
        self.available_observer.notify_followers()

    def make_promotion(self):
        self._state = "promotion"
        self.promotion_observer.notify_followers()

    def make_last_remained(self):
        self._state = "last_remained"
        self.last_remained_observer.notify_followers()


class Observer(ABC):

    def __init__(self):
        self.followers = set()

    def attach(self, follower):
        self.followers.add(follower)

    def detach(self, follower):
        self.followers.remove(follower)

    def notify_followers(self):
        for follower in self.followers:
            print(f"Notification sent to {follower}")


class AvailableObserver(Observer):
    pass


class PromotionObserver(Observer):
    pass


class LastRemainedObserver(Observer):
    pass


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def notify_when_item_available(self, item):
        item.available_observer.attach(self)

    def notify_when_item_on_promotion(self, item):
        item.promotion_observer.attach(self)

    def notify_when_item_last_remained(self, item):
        item.last_remained_observer.attach(self)

    def stop_observing(self, item):
        item.available_observer.detach(self)
        item.promotion_observer.detach(self)
        item.last_remained_observer.detach(self)


if __name__ == "__main__":

    shooses = Shooses()

    user_both = User("Alicja")
    user_both.notify_when_item_available(shooses)
    user_both.notify_when_item_on_promotion(shooses)
    user_only_available = User("Michal")
    user_only_available.notify_when_item_available(shooses)
    user_only_available.notify_when_item_last_remained(shooses)
    user_only_promotion = User("Kamil")
    user_only_promotion.notify_when_item_on_promotion(shooses)

    shooses.make_available()
    shooses.make_last_remained()
    shooses.make_promotion()