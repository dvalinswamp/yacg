from string import Template

tmpl_xe_vlan = open("./templates/tmpl_xe_vlan.txt", "r")
tmpl_xe_vlan_data = tmpl_xe_vlan.read()
XEVlanTemplate = Template(tmpl_xe_vlan)


class Vlan:
    def __init__(self, vid, name, description, os):
        self.os = os
        self.name = name
        self.vid = vid
        self.description = description

    def Print(self):
        if (self.os == 'XE'):
            t = XEVlanTemplate
            print(t.substitute(vid=self.vid, description=self.description))
