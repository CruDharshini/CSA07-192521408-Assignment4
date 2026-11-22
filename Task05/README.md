# Task 5 – Separate Guests from Office (7 marks)

## VLAN plan
- VLAN 10 – Office, 192.168.10.0/24, gateway 192.168.10.1
- VLAN 20 – CCTV, 192.168.20.0/24, gateway 192.168.20.1
- VLAN 30 – Guest Wi-Fi, 192.168.30.0/24, gateway 192.168.30.1

802.1Q inserts a 4-byte VLAN tag into an Ethernet frame. Configure access ports for endpoints and a trunk carrying only VLANs 10, 20 and 30. The guest ACL denies internal private networks and permits internet-bound traffic; apply it inbound on the guest subinterface. A production ACL should include all internal prefixes used by the organisation.

## Completed access-switch configuration
See `access_switch.cfg`. It creates VLAN 30, assigns Fa0/13–20 to CCTV, Fa0/21–24 to Guest, and trunks Gi0/1 with an explicit VLAN allow-list.

## Router-on-a-stick configuration
See `router_on_a_stick.cfg`. Router interface and ISP/default route must be adjusted to the actual Packet Tracer topology.

## Broadcast domains
Before VLAN separation, all devices on one flat LAN share one broadcast domain. After the change there are three broadcast domains (one per VLAN). Switch port collision domains remain separate per access port. Inter-VLAN routing is controlled by the router/L3 switch and ACL.

## Physical guest-switch alternative
A dedicated physical switch and internet circuit provide stronger physical separation and reduce the chance of VLAN misconfiguration, but require extra switch ports, cabling, power and possibly a separate ISP subscription. A dedicated guest switch is justified for strict regulatory isolation or when the existing switching infrastructure cannot enforce VLAN policy securely. A VLAN is normally cheaper and easier to manage.
