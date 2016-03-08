from string import Template

tmpl_xe_access = open("./templates/tmpl_xe_acc_iface.txt", "r")
tmpl_xe_access_data = tmpl_xe_access.read()

tmpl_xe_trunk = open("./templates/tmpl_xe_trunk_iface.txt", "r")
tmpl_xe_trunk_data = tmpl_xe_trunk.read()

XETrunkTemplate = Template(tmpl_xe_trunk_data)
XEAccessTemplate = Template(tmpl_xe_access_data)


class Trunk:
    def __init__(self, name, description, allowed_vlan_list, os):
        self.os = os
        self.name = name
        self.description = description
        self.allowed_vlan_list = allowed_vlan_list

    def Print(self):
        if (self.os == 'XE'):
            t = XETrunkTemplate
            #            print('Untagged Detected')
            print(t.substitute(name=self.name, description=self.description, allowed_vlan_list=self.allowed_vlan_list))


class Acc:
    def __init__(self, name, description, acc_vlan, voice_vlan, os):
        self.os = os
        self.name = name
        self.description = description
        self.acc_vlan = acc_vlan
        self.voice_vlan = voice_vlan

    def Print(self):
        if (self.os == 'XE'):
            t = XEAccessTemplate
            #            print('Untagged Detected')
            print(t.substitute(name=self.name, description=self.description, acc_vlan=self.acc_vlan,
                               voice_vlan=self.voice_vlan))
