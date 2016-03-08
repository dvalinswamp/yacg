from string import Template

tmpl_xe_ldp = open("./templates/tmpl_xe_mpls_iface_ldp.txt", "r")
tmpl_xe_rsvp = open("./templates/tmpl_xe_mpls_iface_rsvp.txt", "r")
tmpl_xe_ldp_data = tmpl_xe_ldp.read()
tmpl_xe_rsvp_data = tmpl_xe_rsvp.read()

XELDPTemplate = Template(tmpl_xe_ldp_data)
XERSVPTemplate = Template(tmpl_xe_rsvp_data)


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
                print(t.substitute(name=self.name, tag=self.tag))

            elif (self.protocol == 'rsvp'):
                t = XERSVPTemplate
                print(t.substitute(name=self.name, tag=self.tag))
