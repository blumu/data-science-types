class Artist:
    def set_label(self, s: str) -> None: ...

class Line2D(Artist): ...
class Collection(Artist): ...
class LineCollection(Collection): ...
class Patch(Artist): ...
class Rectangle(Patch): ...
