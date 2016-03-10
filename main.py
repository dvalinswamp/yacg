from openpyxl import load_workbook

from PE import PE
from UPE import UPE

# from MPLS import LabeledInterface

management = {'snmp_community': [],
              'management_subnets': [],
              'default_user': [],
              'default_password': []
              }

devices = {}
data = load_workbook('data.xlsx')
sheet = data.get_sheet_by_name('Devices')
for row in range(2, sheet.max_row + 1):
    host = sheet['A' + str(row).strip()].value
    if (not host): print('Device undefinedint row', row)
    devtype = sheet['B' + str(row).strip()].value
    if (not devtype): print('Device ' + host + ' type absent')
    mgmtiface = sheet['C' + str(row).strip()].value
    if (not mgmtiface): print('Device ' + host + ' mgmtiface absent')
    ip = sheet['D' + str(row).strip()].value
    if (not ip): print('Device ' + host + ' mgmt ip absent')
    os = sheet['E' + str(row).strip()].value
    if (not os): print('Device ' + host + ' os definition absent')
    if (devtype == 'PE'):
        devices[host] = (PE(host, mgmtiface, ip, os))
    if (devtype == 'UPE'):
        devices[host] = (UPE(host, mgmtiface, ip, os))

sheet = data.get_sheet_by_name('Interfaces')
for row in range(2, sheet.max_row + 1):
    device = str(sheet['A' + str(row).strip()].value)
    name = str(sheet['B' + str(row).strip()].value)
    media = str(sheet['C' + str(row).strip()].value)
    speed = str(sheet['D' + str(row).strip()].value)
    tag = str(sheet['E' + str(row).strip()].value)
    vrf = str(sheet['F' + str(row).strip()].value)
    ipv4_address = str(sheet['G' + str(row).strip()].value)
    ipv6_address = str(sheet['H' + str(row).strip()].value)
    devices[device].CreateInterface(name, speed, media, tag, vrf, ipv4_address, ipv6_address)
    print('created interface',name,'for pe',device)


sheet = data.get_sheet_by_name('L2ifaces')
for row in range(2, sheet.max_row + 1):
    print('starting l2 interfaces')
    device = sheet['A' + str(row).strip()].value
    ifname = sheet['B' + str(row).strip()].value
    description =  sheet['C' + str(row).strip()].value
    mode = sheet['D' + str(row).strip()].value
    allowed_vlans = sheet['E' + str(row).strip()].value
    print ('processing', device, ifname, mode)
    if (mode=='trunk'):
        print('creating a trunk from main')
        devices[device].CreateTrunk(ifname, description, allowed_vlans)
    elif (mode=='access'):
        devices[device].CreateAccess(ifname, description, allowed_vlans)


# sheet = data.get_sheet_by_name('MPLS_P2P')
# for row in range (2, sheet.max_row+1):
#    device = sheet['A' + str(row)].value
#    name = sheet['B' + str(row)].value
#    tag = sheet['E' + str(row)].value
#    devices[device].CreateInterface(name, speed, media, tag, vrf, ipv4_address, ipv6_address)


# sheet = data.get_sheet_by_name('DHCP')
# for row in range (2, sheet.max_row+1):
#    device = sheet['A' + str(row)].value
#    name = sheet['B' + str(row)].value
#    media = sheet['C' + str(row)].value
#    speed = sheet['D' + str(row)].value
#    tag = sheet['E' + str(row)].value
#    vrf = sheet['F' + str(row)].value
#    ipv4_address = sheet['G' + str(row)].value
#    ipv6_address = sheet['H' + str(row)].value
#    devices[device].CreateInterface(name, speed, media, tag, vrf, ipv4_address, ipv6_address)

# devices['bbr02'].PrintInterfaces()
for host in devices:
    print(host)
    devices[host].PrintInterfaces()
