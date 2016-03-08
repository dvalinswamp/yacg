from string import Template

tmpl_xe_exp_vrf = open("./templates/tmpl_xe_vrf_exportable.txt", "r")
tmpl_xe_inexp_vrf = open("./templates/tmpl_xe_vrf_inexportable.txt", "r")
tmpl_xe_exp_vrf_data = tmpl_xe_exp_vrf.read()
tmpl_xe_inexp_vrf_data = tmpl_xe_inexp_vrf.read()

XEVRFExpTemplate = Template(tmpl_xe_exp_vrf_data)
XEVRFInexpTemplate = Template(tmpl_xe_inexp_vrf_data)


class VRF:
    def __init__(self, os, name, rd='Null', is_exportable='Null', ipv4_rt_import='Null', ipv4_rt_export='Null',
                 ipv6_rt_import='Null', ipv6_rt_export='Null'):
        self.os = os
        self.name = name
        self.rd = rd
        self.is_exportable = is_exportable
        self.ipv4_rt_import = ipv4_rt_import
        self.ipv4_rt_export = ipv4_rt_export
        self.ipv6_rt_export = ipv6_rt_export
        self.ipv6_rt_import = ipv6_rt_import

    def Print(self):
        if (self.os == 'XE'):
            if (self.is_exportable == '0'):
                print('Inexp Detected')
                t = XEVRFInexpTemplate
                print(t.substitute(name=self.name, rd=self.rd))
            else:
                t = XEVRFExpTemplate
                print('Exp Detected')
                print(t.substitute(name=self.name, rd=self.rd, ipv4_rt_import=self.ipv4_rt_import,
                                   ipv4_rt_export=self.ipv4_rt_export, ipv6_rt_export=self.ipv6_rt_export,
                                   ipv6_rt_import=self.ipv6_rt_import))

                # a=VRF('A','65400:1','1','65400:1','65400:2','65400:3','65400:4')
                # b=VRF('A','65400:1','0')
                # a.Print()
                # b.Print()
