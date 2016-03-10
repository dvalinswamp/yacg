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

    def CreateTrunk(self, name, description, allowed_vlans):
        #        print('creating interface',name)
        os = self.os
        interface = Trunk(name, description, allowed_vlans, os)
        UPE.interfaces[name] = interface

    def CreateAcc(self, name, description, acc_vlan, voice_vlan):
        os = self.os
        interface = Acc(name, description, acc_vlan, voice_vlan, os)
        UPE.interfaces[name] = interface

    def CreateVlan(self, vid, name, description):
        os = self.os
        vlan = Vlan(vid, name, description, os)
        UPE.vlans.append(vlan)

    def PrintInterfaces(self):
        for i in self.interfaces:
            i.Print()

    def PrintVlans(self):
        for i in self.vlans:
            i.Print()
