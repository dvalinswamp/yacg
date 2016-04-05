from string import Template

XEVlanTemplate = Template((open("./templates/tmpl_xe_vlan.txt", "r")).read())


class Vlan:
    def __init__(self, vid, name, description, os):
        self.os = os
        self.name = name
        self.vid = vid
        self.description = description

    def Print(self):
        if (self.os == 'XE'):
            t = XEVlanTemplate
            return(t.substitute(vid=self.vid, description=self.description))
        if (self.os == 'XR'):
            t = XRVlanTemplate
            return(t.substitute(vid=self.vid, description=self.description))
        if (self.os == 'Jun'):
            t = JunVlanTemplate
            return(t.substitute(vid=self.vid, description=self.description))


#a=Vlan('400','cust1','Custome1 test vlan','XE')
#print(a.Print())