from enum import Enum


class TypeEnum(str, Enum):
    none = "none"
    router = "router"
    lan = "switch"
    customer = "firewall"

    # def __hash__(self):
    #     return hash(self.name)
