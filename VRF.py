from string import Template

XEVRFExpTemplate = Template(open("./templates/tmpl_xe_vrf_exportable.txt", "r").read())
XEVRFInexpTemplate = Template(open("./templates/tmpl_xe_vrf_inexportable.txt", "r").read())


class VRF:
    def __init__(self, name, os, rd, ipv4_rt_import='', ipv4_rt_export='',
                 ipv6_rt_import='', ipv6_rt_export=''):
        self.name = name
        self.os = os
        self.rd = rd
        self.ipv4_rt_import = ipv4_rt_import
        self.ipv4_rt_export = ipv4_rt_export
        self.ipv6_rt_export = ipv6_rt_export
        self.ipv6_rt_import = ipv6_rt_import

    def Print(self):
        if(bool(self.ipv4_rt_import) & bool(self.ipv4_rt_import) & bool(self.ipv4_rt_import) & bool(self.ipv4_rt_import)):
            self.is_exportable = 1
#            print(self.os)
        else:
            self.is_exportable = 0

        if (self.os == 'XE'):
            if (self.is_exportable == False):
                t = XEVRFInexpTemplate
                return(t.substitute(name=self.name, rd=self.rd))
            else:
                t = XEVRFExpTemplate
                return(t.substitute(name=self.name, rd=self.rd, ipv4_rt_import=self.ipv4_rt_import,
                                   ipv4_rt_export=self.ipv4_rt_export, ipv6_rt_export=self.ipv6_rt_export,
                                   ipv6_rt_import=self.ipv6_rt_import))

#a = VRF('A', 'XE', 'rd', '65400:1','65400:2','65400:3','65400:4')
#b = VRF('B', 'XE', '65400:1')

