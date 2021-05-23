from __future__ import annotations

from typing import TypeVar, Generic, List

Item = TypeVar('Item')


class PlanResponse:

    def __init__(self, status: int):
        self.status = status


class PlanListSuccessResponse(PlanResponse, Generic[Item]):

    def __init__(self, items: List[Item], status: int, count: int, left: int, has_next: bool = False):
        super().__init__(status)
        self.items = items
        self.count = count
        self.has_next = has_next
        self.left = left


class PlanCreateSuccessResponse(PlanResponse, Generic[Item]):

    def __init__(self, item: Item, status: int, ):
        super().__init__(status)
        self.item = item
