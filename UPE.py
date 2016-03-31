from SwitchedInterface import Acc
from SwitchedInterface import Trunk
from Vlan import Vlan
from device import PacketDevice

class UPE(PacketDevice):


    def __init__(self, name, mgmtiface, mgmtip, os):
        PacketDevice.__init__(self, name, mgmtiface, mgmtip, os)
        self.vlans = []


    def CreateTrunk(self, name, description, allowed_vlans):
        print('creating interface',name)
        os = self.os
        interface = Trunk(name, description, allowed_vlans, os)
        self.interfaces.append(interface)


    def CreateAcc(self, name, description, acc_vlan):
        os = self.os
        interface = Acc(name, description, acc_vlan, os)
        self.interfaces.append(interface)


    def CreateVlan(self, vid, name, description):
        os = self.os
        vlan = Vlan(vid, name, description, os)
        self.vlans.append(vlan)

    def PrintVlans(self):
        cfg = '!\n'
        for i in self.vlans:
#             print(i.name)
            cfg += i.Print()

        return cfg


    def PrintCfg(self):
        cfg = ''
        cfg += self.PrintSelf()
        cfg = '!\n'
        cfg += self.PrintInterfaces()
        cfg += '\n!'
        cfg += self.PrintVlans()
        return cfg