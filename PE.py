from MPLS import LabelledInterface
from RoutedInterface import Interface
from SwitchedInterface import Trunk
from Vlan import Vlan
from VRF import VRF


class PE:
    interfaces = []
    labelled_interfaces = []
    vrfs = []
    vlans = []

    def __init__(self, name, mgmtiface, mgmtip, os):
        self.name = name
        self.mgmtiface = mgmtiface
        self.mgmtip = mgmtip
        self.os = os

    #        print('creating device',self.name)

    #    def print(self):
    #       print('device created:',self.name)

    def CreateInterface(self, name, speed, media, tag, vrf, ipv4_address, ipv6_address):
        #        print('creating interface',name)
        os = self.os
        interface = Interface(name, speed, media, tag, vrf, ipv4_address, ipv6_address, os)
        PE.interfaces.append(interface)

    def CreateVRF(self, name, rd='Null', is_exportable='Null', ipv4_rt_import='Null', ipv4_rt_export='Null',
                  ipv6_rt_import='Null', ipv6_rt_export='Null'):
        vrf = VRF(name, rd, is_exportable, ipv4_rt_import, ipv4_rt_export, ipv6_rt_import, ipv6_rt_export, self.os)
        PE.vrfs.append(vrf)

    def PrintInterfaces(self):
        for i in self.interfaces:
            i.Print()

    def PrintVRFs(self):
        for i in self.vrfs:
            i.Print()

    def CreateLabelledInterface(self, name, tag, protocol):
        #        print('creating interface',name)
        os = self.os
        labelled_interface = LabelledInterface(name, tag, protocol)
        PE.labelled_interfaces.append(labelled_interface)

    def CreateVlan(self, vid, name, description):
        os = self.os
        vlan = Vlan(vid, name, description, os)
        PE.vlans.append(vlan)

    def CreateTrunk(self, name, description, allowed_vlans):
        #        print('creating interface',name)
        os = self.os
        interface = Trunk(name, description, allowed_vlans, os)
        PE.interfaces[name] = interface
