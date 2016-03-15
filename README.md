# yacg
Yet another config generator
focused on mass creation of cfg files for networking hardware based on results of PoC activities.
It is assumed that most of the parameters stay static helping to allocate device variables - vlan nubers, svis, ip addresses etc.
following device roles supported:
-pe
-upe

---
pe
 - generic device config
 -  ipv4 and ipv6 for interfaces:
   - L3vpn enables tagged
   - L3vpn enables untagged
   - GRT tagged
   - GRT untagged
 -  mpls control plane on interfaces:
  - rsvp
  - ldp
 - l2 trunk interfaces
 - SVI interfaces
 - L3vpn instances
  - exportable in BGP
  - local (no RT's assigned)
 - vlan definition

---
upe
 - generic device parameters
 - l2 trunk interface
 - l2 access interface
 - svis
 - vlan definition