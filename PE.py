from MPLS import LabelledInterface
from RoutedInterface import Interface
from SwitchedInterface import Trunk
from Vlan import Vlan
from VRF import VRF
from device import PacketDevice

class PE(PacketDevice):


    def __init__(self, name, mgmtiface, mgmtip, os):
        PacketDevice.__init__(self, name, mgmtiface, mgmtip, os)
        self.labelled_interfaces = []
        self.vrfs = []
        self.vlans = []

## moved to device par3ent class
#    def CreateInterface(self, name, speed, media, tag, vrf, ipv4_address, ipv6_address):
#        os = self.os
#        interface = Interface(name, speed, media, tag, vrf, ipv4_address, ipv6_address, os)
#        self.interfaces.append(interface)
#        print('function call - pe/create iface for pe', self.name)


    def CreateVRF(self, name, rd='Null', ipv4_rt_import='Null', ipv4_rt_export='Null',
                  ipv6_rt_import='Null', ipv6_rt_export='Null'):
        vrf = VRF(name, self.os, rd, ipv4_rt_import, ipv4_rt_export, ipv6_rt_import, ipv6_rt_export)
        self.vrfs.append(vrf)


    def PrintVRFs(self):
        cfg = '!\n'
        for i in self.vrfs:
            cfg = cfg + str(i.Print()) + '\n'
        return cfg


    def CreateLabelledInterface(self, name, tag, protocol):
        os = self.os
        labelled_interface = LabelledInterface(name, tag, protocol)
        self.labelled_interfaces.append(labelled_interface)


    def PrintLabelledInterfaces(self):
        cfg = '!\n'
        for i in self.labelled_interfaces:
            cfg = cfg + str(i.Print()) + '\n'
        return cfg


    def CreateVlan(self, vid, name, description):
        os = self.os
        vlan = Vlan(vid, name, description, os)
        self.vlans.append(vlan)


    def PrintVlans(self):
        cfg = '!\n'
        for i in self.vlans:
            cfg = cfg + str(i.Print()) + '\n'
        return cfg


    def CreateTrunk(self, name, description, allowed_vlans):
        #        print('creating interface',name)
        os = self.os
        interface = Trunk(name, description, allowed_vlans, os)
        self.interfaces.append(interface)


    def PrintCfg(self):
        cfg = self.PrintSelf()
#        print(self.name)
#        print(self.PrintInterfaces())
        cfg += self.PrintInterfaces()
        cfg += '\n!'
        cfg += self.PrintVRFs()
        cfg += '\n!'
        cfg += self.PrintLabelledInterfaces()
        cfg += '\n!'
        cfg += self.PrintVlans()
        cfg += '\n!'
        return cfg


s= PE('scd-pe01','Lo0','10.224.0.1','XE')
