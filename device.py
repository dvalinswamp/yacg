from RoutedInterface import Interface
from string import Template

XEAETemplate = Template(open("./templates/tmpl_xe_ae.txt", "r").read())
JunAETemplate = Template(open("./templates/tmpl_jun_ae.txt", "r").read())
XRAETemplate = Template(open("./templates/tmpl_xr_ae.txt", "r").read())
GeneralXETemplate = Template(open("./templates/tmpl_xe_general.txt", "r").read())
GeneralXRemplate = Template(open("./templates/tmpl_xr_general.txt", "r").read())
GeneralJunTemplate = Template(open("./templates/tmpl_jun_general.txt", "r").read())



class PacketDevice:
    def __init__(self, name, mgmtiface, mgmtip, os):
        self.name = name
        self.mgmtiface = mgmtiface
        self.mgmtip = mgmtip
        self.os = os
        self.interfaces = []
        self.ae = {}


    def CreateInterface(self, name, speed, media, tag, vrf, ipv4_address, ipv6_address):
        os = self.os
        interface = Interface(name, speed, media, tag, vrf, ipv4_address, ipv6_address, os)
        self.interfaces.append(interface)
#        print('function call - pe/create iface for pe', self.name)


    def CreateAE(self, abbr, aenum):
        self.ae[abbr] = aenum


    def PrintInterfaces(self):
        ifcfg = '!\n'
        for i in self.interfaces:
#           print(i.Print())
            ifcfg += str(i.Print()) + '\n'
        return ifcfg


    def PrintSelf(self):
#        print('PrintSelf subfunction')
        if (self.os == 'XE'):
            t = GeneralXETemplate
        elif (self.os == 'XR'):
            t = GeneralXRemplate
        elif (self.os == 'junos'):
            t = GeneralJunTemplate
        else:
            print('Device ', self.name, "unrecognised platform:", self.os)
#        print (t.substitute(hostname=self.name))
        cfg = t.substitute(hostname=self.name)
        cfg += '\n'
        return(cfg)


    def PrintAE(self):
        if (self.os == 'XE'):
            t = XEAETemplate
        elif (self.os == 'XR'):
            t = XRAETemplate
        elif (self.os == 'junos'):
            t = JunAETemplate
        else:
            print('Device ', self.name, "Unrecognised platform:", self.os)
        aecfg = '!\n'
        for i in self.ae:
            tmpl = t
#            print(i)
#            print(self.ae[i])
#            print(str(tmpl.substitute(i, aenum=str(self.ae[i])))
            aecfg += str(tmpl.substitute(name=i, aenum=self.ae[i]))+'\n'
        return aecfg



