from enum import Enum


class CustomerTypeEnum(str, Enum):
    customer = "customer"
    partner = "partner"

    # def __hash__(self):
    #     return hash(self.name)
