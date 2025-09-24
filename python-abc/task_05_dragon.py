#!/usr/bin/env python3
"""The Mystical Dragon - Mastering Mixins"""


class SwimMixin:
    """Mixin for swimming capability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin for flying capability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class using mixins."""

    def roar(self):
        print("The dragon roars!")
