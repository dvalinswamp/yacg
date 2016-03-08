from SwitchedInterface import Acc
from SwitchedInterface import Trunk
from Vlan import Vlan


class UPE:
    interfaces = {}
    vlans = []

    def __init__(self, name, mgmtiface, mgmtip, os):
        self.name = name
        self.mgmtiface = mgmtiface
        self.mgmtip = mgmtip
        self.os = os

    @staticmethod
    def CreateTrunk(name, description, allowed_vlans):
        #        print('creating interface',name)
        os = UPE.os
        interface = Trunk(name, description, allowed_vlans, os)
        UPE.interfaces[name] = interface

    @staticmethod
    def CreateAcc(name, description, acc_vlan, voice_vlan):
        os = UPE.os
        interface = Acc(name, description, acc_vlan, voice_vlan, os)
        UPE.interfaces[name] = interface

    @staticmethod
    def CreateVlan(vid, name, description):
        os = UPE.os
        vlan = Vlan(vid, name, description, os)
        UPE.vlans.append(vlan)

    def PrintInterfaces(self):
        for i in self.interfaces:
            i.Print()

    def PrintVlans(self):
        for i in self.vlans:
            i.Print()
