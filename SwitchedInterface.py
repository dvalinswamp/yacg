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
        print('Created trunk', name)

    def Print(self):
        if (self.os == 'XE'):
            t = XETrunkTemplate
            #            print('Untagged Detected')
            print(t.substitute(name=self.name, description=self.description, allowed_vlan_list=self.allowed_vlan_list))


class Acc:
    def __init__(self, name, description, acc_vlan, os):
        self.os = os
        self.name = name
        self.description = description
        self.acc_vlan = acc_vlan

    def Print(self):
       # if (self.os == 'XE'):
            t = XEAccessTemplate
            #            print('Untagged Detected')
            print(t.substitute(name=self.name, description=self.description, acc_vlan=self.acc_vlan))
#int1 = Trunk('Ten1/1','test_trunk','10-40','XE')
#int1.Print()
#int2 = Trunk('Ten1/2', '10000', '10G-SR', '1','GRT','10.0.0.1/30', '2001::1/127')
#int2.Print()
#int3 = Interface('Ten1/3','10000','10G-SR','0','A','10.0.1.1/30','2001::2:1/127')
#int3.Print()
#int4 = Interface('Ten1/4', '10000', '10G-SR', '1','B','10.0.2.1/30', '2001::3:1/127')
#int4.Print()
