from string import Template

XELDPTemplate = Template(open("./templates/tmpl_xe_iface_ldp.txt", "r").read())
XERSVPTemplate = Template(open("./templates/tmpl_xe_iface_rsvp.txt", "r").read())


class LabelledInterface:
    def __init__(self, name, tag, protocol, os):
        self.name = name
        self.tag = tag
        self.protocol = protocol
        self.os = os

    def Print(self):
        if (self.os == 'XE'):
            if (self.protocol == 'ldp'):
                t = XELDPTemplate
                return(t.substitute(name=self.name, tag=self.tag))

            elif (self.protocol == 'rsvp'):
                t = XERSVPTemplate
                return(t.substitute(name=self.name, tag=self.tag))
