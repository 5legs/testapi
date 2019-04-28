from enum import Enum


class RoleEnum(str, Enum):
    none = "none"
    lan = "lan"
    customer = "customer"
    netcenter = "netcenter"
    provider = "provider"
    wan = "wan"
    datacenter = "datacenter"
    store = "store"
    headquarter = "headquarter"

    # def __hash__(self):
    #     return hash(self.name)
