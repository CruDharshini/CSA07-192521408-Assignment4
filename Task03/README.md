# Task 3 – Devices, Media and Cabling (9 marks)

## Run checks
TIA/EIA structured cabling permits a 90 m permanent link and 100 m channel (including patch cords).
- Consulting rooms: 35–80 m, within limits. Cat6 UTP is suitable for 1 GbE; Cat6A may be selected for 10 GbE/future capacity.
- Pharmacy: 96 m from telecom room. It exceeds the 90 m permanent-link limit and leaves too little margin for patch cords under the 100 m channel limit. Move an IDF closer or use fibre.
- Waiting hall AP runs: 60 m, within limits. Cat6/Cat6A supports PoE if the switch and cable budget support the AP.
- Main building: 420 m, exceeds copper Ethernet distance. Use fibre (multimode for suitable building-campus reach; single-mode for longer reach/future flexibility).

T568A at one end and T568B at the other makes a crossover cable. Auto-MDIX on modern switches can often adapt transmit/receive pairs, but it does not make mixed standards a good structured-cabling practice. Use T568B consistently at both ends unless a deliberate crossover is needed.

## Devices and domains
Use managed Layer-2 access switches for endpoint connectivity; Layer-3 switch for inter-VLAN routing at the distribution/core; router/firewall for WAN and security policy; wireless APs for WLAN. Avoid hubs. With one VLAN per access switch, each switch port is its own collision domain; each VLAN is one broadcast domain across its switches. A router/L3 switch separates broadcast domains between VLANs.

## Scalable bill of materials
Exact room count, AP count, endpoint count and floor plan are not specified, so quantities that depend on them are expressed as formulas. For each copper run, cable length = measured route × 1.10 spare.
| Item | Quantity / specification |
|---|---|
| Managed PoE access switch | Ports ≥ wired endpoints + APs + 20% spare |
| Cat6/Cat6A horizontal cable | Sum of measured copper routes × 1.10 |
| Fibre uplink to main building | 420 m × 1.10 = 462 m; choose fibre type and transceivers to match |
| Patch panel | Ports ≥ copper drops |
| RJ45 plugs/keystone jacks | 2 terminations per copper drop, plus spares |
| Fibre termination | Compatible patch panel/LIU, pigtails and connectors at both ends |
| Racks/cabinets | One telecom cabinet per IDF, sized for switches, patch panels and UPS |
| Patch cords | One at each outlet and switch end, plus spares |
| UPS | Sized for PoE switch and critical network equipment |

## T568B order (pins 1–8)
White-orange, orange, white-green, blue, white-blue, green, white-brown, brown.

## 420 m alternative
Fibre supports the 420 m run without intermediate powered equipment (choose optics and fibre grade for the reach). Cat6A is limited to a 100 m channel, so a mid-way switch still leaves two segments and needs a powered, protected intermediate cabinet; 420 m requires at least five copper segments (four intermediate switches) if every segment is kept under 100 m. Fibre is electrically non-conductive and does not carry lightning-induced ground potential along the data path; copper between buildings needs surge protection and grounding. Fibre transceivers and termination can cost more initially, but avoid remote switch power and maintenance.
