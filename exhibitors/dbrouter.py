from .models import Exhibitor

...


class ExhibitorDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model == Exhibitor:
            return 'exhibitors'
        return None

    def db_for_write(self, model, **hints):
        """ writing SomeModel to otherdb """
        if model == Exhibitor:
            return 'exhibitors'
        return None
