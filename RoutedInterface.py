from string import Template

tmpl_routed_tagged = open("./templates/tmpl_xe_routed_tagged.txt", "r")
tmpl_routed_tagged_data = tmpl_routed_tagged.read()

tmpl_routed_untagged = open("./templates/tmpl_xe_routed_untagged.txt", "r")
tmpl_routed_untagged_data = tmpl_routed_untagged.read()

tmpl_vrf_routed_tagged = open("./templates/tmpl_xe_vrf_routed_tagged.txt", "r")
tmpl_vrf_routed_tagged_data = tmpl_vrf_routed_tagged.read()

tmpl_vrf_routed_untagged = open("./templates/tmpl_xe_vrf_routed_untagged.txt", "r")
tmpl_vrf_routed_untagged_data = tmpl_vrf_routed_untagged.read()

tmpl_svi = open("./templates/tmpl_xe_svi.txt", "r")
tmpl_vrf_svi = open("./templates/tmpl_xe_vrf_svi.txt", "r")
tmpl_svi_data = tmpl_svi.read()
tmpl_vrf_svi_data = tmpl_svi.read()

TaggedTemplate = Template(tmpl_routed_tagged_data)
UntaggedTemplate = Template(tmpl_routed_untagged_data)
VRFTaggedTemplate = Template(tmpl_vrf_routed_tagged_data)
VRFUntaggedTemplate = Template(tmpl_vrf_routed_untagged_data)
SVITemplate = Template(tmpl_svi_data)
VRFSVITemplate = Template(tmpl_vrf_svi_data)


class SVI:
    def __init__(self, name, vrf, ipv4_address, ipv6_address, os):
        self.os = os
        self.name = name
        self.vrf = vrf
        self.ipv4address = ipv4_address
        self.ipv6address = ipv6_address

    def Print(self):
        if (self.vrf == 'GRT'):
            t = SVITemplate
            print(t.substitute(name=self.name, ipv4address=self.ipv4address, ipv6address=self.ipv6address))
        if (self.vrf != 'GRT'):
            t = VRFSVITemplate
            #            print('Tagged Detected')
            print(
                t.substitute(name=self.name, vrf=self.vrf, ipv4address=self.ipv4address, ipv6address=self.ipv6address))


class Interface:
    def __init__(self, name, speed, media, tag, vrf, ipv4_address, ipv6_address, os):

        self.os = os
        self.name = name
        self.speed = speed
        self.media = media
        self.tag = tag
        self.vrf = vrf
        self.ipv4address = ipv4_address
        self.ipv6address = ipv6_address
        print('creating an interface', name, tag)

    def Print(self):
        if (self.os == 'XE'):
            if ((self.tag == "0") & (self.vrf == 'GRT')):
                t = UntaggedTemplate
                print('Untagged Detected')
                print(t.substitute(name=self.name, speed=self.speed, media=self.media, ipv4address=self.ipv4address,
                                   ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf == 'GRT')):
                t = TaggedTemplate
                print('Tagged Detected')
                print(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf != 'GRT')):
                t = VRFTaggedTemplate
                print('Tagged Detected')
                print(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag == "0") & (self.vrf != 'GRT')):
                t = VRFUntaggedTemplate
                print('UnTagged Detected')
                print(t.substitute(name=self.name, speed=self.speed, media=self.media, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))


#int1 = Interface('Ten1/1','10000','10G-SR','0','GRT','10.0.0.1/30','2001::1/127', 'XE')
#int1.Print()
#int2 = Interface('Ten1/2', '10000', '10G-SR', '1','GRT','10.0.0.1/30', '2001::1/127', 'XE')
#int2.Print()
#int3 = Interface('Ten1/3','10000','10G-SR','0','A','10.0.1.1/30','2001::2:1/127', 'XE')
#int3.Print()
#int4 = Interface('Ten1/4', '10000', '10G-SR', '1','B','10.0.2.1/30', '2001::3:1/127', 'XE')
#int4.Print()
