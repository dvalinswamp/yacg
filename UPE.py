from SwitchedInterface import Acc
from SwitchedInterface import Trunk
from Vlan import Vlan


class UPE:


    def __init__(self, name, mgmtiface, mgmtip, os):
        self.name = name
        self.mgmtiface = mgmtiface
        self.mgmtip = mgmtip
        self.os = os
        self.interfaces = []
        self.vlans = []


    def CreateTrunk(self, name, description, allowed_vlans):
        print('creating interface',name)
        os = self.os
        interface = Trunk(name, description, allowed_vlans, os)
        self.interfaces.append(interface)

    def CreateAcc(self, name, description, acc_vlan, voice_vlan):
        os = self.os
        interface = Acc(name, description, acc_vlan, voice_vlan, os)
        self.interfaces.append(interface)

    def CreateVlan(self, vid, name, description):
        os = self.os
        vlan = Vlan(vid, name, description, os)
        self.vlans.append(vlan)

    def PrintInterfaces(self):
        for i in self.interfaces:
            i.Print()

    def PrintVlans(self):
        for i in self.vlans:
            i.Print()
