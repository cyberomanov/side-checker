from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    type: int
    typeName: str
    subType: int
    subTypeName: str
    amount: int


class SideAirdropResponse(BaseModel):
    alreadyRegistered: bool
    hasEligibility: bool
    tooLate: bool
    totalAmount: int
    items: List[Item]
