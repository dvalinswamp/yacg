from string import Template

XETaggedTemplate = Template(open("./templates/tmpl_xe_routed_tagged.txt", "r").read())
XEUntaggedTemplate = Template(open("./templates/tmpl_xe_routed_untagged.txt", "r").read())
XEVRFTaggedTemplate = Template(open("./templates/tmpl_xe_vrf_routed_tagged.txt", "r").read())
XEVRFUntaggedTemplate = Template(open("./templates/tmpl_xe_vrf_routed_untagged.txt", "r").read())
XESVITemplate = Template(open("./templates/tmpl_xe_svi.txt", "r").read())
XEVRFSVITemplate = Template(open("./templates/tmpl_xe_vrf_svi.txt", "r").read())

JunTaggedTemplate = Template(open("./templates/tmpl_jun_routed_tagged.txt", "r").read())
JunUntaggedTemplate = Template(open("./templates/tmpl_jun_routed_untagged.txt", "r").read())
JunVRFTaggedTemplate = Template(open("./templates/tmpl_jun_vrf_routed_tagged.txt", "r").read())
JunVRFUntaggedTemplate = Template(open("./templates/tmpl_jun_vrf_routed_untagged.txt", "r").read())

XRTaggedTemplate = Template(open("./templates/tmpl_xr_routed_tagged.txt", "r").read())
XRUntaggedTemplate = Template(open("./templates/tmpl_xr_routed_untagged.txt", "r").read())
XRVRFTaggedTemplate = Template(open("./templates/tmpl_xr_vrf_routed_tagged.txt", "r").read())
XRVRFUntaggedTemplate = Template(open("./templates/tmpl_xr_vrf_routed_untagged.txt", "r").read())


class SVI:
    def __init__(self, name, vrf, ipv4_address, ipv6_address, os):
        self.os = os
        self.name = name
        self.vrf = vrf
        self.ipv4address = ipv4_address
        self.ipv6address = ipv6_address


    def Print(self):
        if (self.vrf == 'GRT'):
            t = XESVITemplate
            print(t.substitute(name=self.name, ipv4address=self.ipv4address, ipv6address=self.ipv6address))
        if (self.vrf != 'GRT'):
            t = XEVRFSVITemplate
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
#        print('creating an interface', name, tag)

    def Print(self):
#        print('starting print')
        if (self.os == 'XE'):
            if ((self.tag == "0") & (self.vrf == 'GRT')):
                t = XEUntaggedTemplate
#                print('Untagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, ipv4address=self.ipv4address,
                                   ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf == 'GRT')):
                t = XETaggedTemplate
#                print('Tagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf != 'GRT')):
                t = XEVRFTaggedTemplate
#                print('Tagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag == "0") & (self.vrf != 'GRT')):
                t = XEVRFUntaggedTemplate
#                print('UnTagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
        if (self.os == 'junos'):
            if ((self.tag == "0") & (self.vrf == 'GRT')):
                t = JunUntaggedTemplate
#                print('Untagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, ipv4address=self.ipv4address,
                                   ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf == 'GRT')):
                t = JunTaggedTemplate
#                print('Tagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf != 'GRT')):
                t = JunVRFTaggedTemplate
#                print('Tagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag == "0") & (self.vrf != 'GRT')):
                t = JunVRFUntaggedTemplate
#                print('UnTagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))



        if (self.os == 'XR'):
            if ((self.tag == "0") & (self.vrf == 'GRT')):
                t = XRUntaggedTemplate
#                print('Untagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, ipv4address=self.ipv4address,
                                   ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf == 'GRT')):
                t = XRTaggedTemplate
#                print('Tagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag != "0") & (self.vrf != 'GRT')):
                t = XRVRFTaggedTemplate
#                print('Tagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, tag=self.tag, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))
            elif ((self.tag == "0") & (self.vrf != 'GRT')):
                t = XRVRFUntaggedTemplate
#                print('UnTagged Detected')
                return(t.substitute(name=self.name, speed=self.speed, media=self.media, vrf=self.vrf,
                                   ipv4address=self.ipv4address, ipv6address=self.ipv6address))



#int = Interface('Ten1/2', '10000', '10G-SR', '1','GRT','10.0.0.1/30', '2001::1/127', 'XE')
#print(int.Print())


