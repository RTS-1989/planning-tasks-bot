from dataclasses import dataclass


@dataclass(frozen=True)
class Messages:
    test: str = 'Календарь мне запилил быстро!'


msg = Messages()
