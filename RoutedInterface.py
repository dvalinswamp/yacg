from string import Template

TaggedTemplate = Template(open("./templates/tmpl_xe_routed_tagged.txt", "r").read())
UntaggedTemplate = Template(open("./templates/tmpl_xe_routed_untagged.txt", "r").read())
VRFTaggedTemplate = Template(open("./templates/tmpl_xe_vrf_routed_tagged.txt", "r").read())
VRFUntaggedTemplate = Template(open("./templates/tmpl_xe_vrf_routed_untagged.txt", "r").read())
SVITemplate = Template(open("./templates/tmpl_xe_svi.txt", "r").read())
VRFSVITemplate = Template(open("./templates/tmpl_xe_vrf_svi.txt", "r").read())


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
        print('starting print')
        if (self.os == 'XE'):
            if ((self.tag == "0") & (self.vrf == 'GRT')):
                t = UntaggedTemplate
                print('Untagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, ipv4address=self.ipv4address,
                                   ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf == 'GRT')):
                t = TaggedTemplate
                print('Tagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf != 'GRT')):
                t = VRFTaggedTemplate
                print('Tagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag == "0") & (self.vrf != 'GRT')):
                t = VRFUntaggedTemplate
                print('UnTagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))

#int = Interface('Ten1/2', '10000', '10G-SR', '1','GRT','10.0.0.1/30', '2001::1/127', 'XE')
#print(int.Print())