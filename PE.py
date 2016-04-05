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
        if (bool(self.interfaces)):
           print('something in interfaces found')
           cfg += '!!\n!!starting interface portion\n!!\n'
           cfg += self.PrintInterfaces()
        if (bool(self.vrfs)):
           cfg += '\n!'
           cfg += '!!\n!!starting vrf portion\n!!\n'
           cfg += self.PrintVRFs()
        if(bool(self.labelled_interfaces)):
           cfg += '\n'
           cfg += '!!!\n!!starting labelif portion\n!!!\n'
           cfg += self.PrintLabelledInterfaces()
        if(bool(self.vlans)):
           cfg += '\n'
           cfg += '!!!\n!!starting vlan portion\n!!!\n'
           cfg += self.PrintVlans()
        return cfg


#s= PE('scd-pe01','Lo0','10.224.0.1','XE')
