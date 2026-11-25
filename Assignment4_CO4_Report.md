# SIMATS Engineering – Computer Networks (CSA07)
## Assignment 4 – CO4: Designing Network Topologies

**Student:** Dharshini  
**Register Number:** 192521408  
**Department:** Information Technology  
**Academic Year:** 2026–2027  
**Faculty:** Dr. Sivachandar K  
**Total Marks:** 50

## Task 1 – Why Does the Whole Office Stop? (6 marks)
The existing office uses a coaxial bus, a hub and a home router. A bus is a shared medium, so a cable or connector fault can interrupt all connected devices. The hub repeats traffic to every port and creates one collision domain. Users share the bus capacity, so month-end file transfers become slow. Moving a desk can disturb the backbone cable, and the home router is a single point of failure.

The redesigned extended star uses managed switches on both floors, structured Cat6/Cat6A cabling, a core switch, business router and firewall. A server connects to the core. Assuming a 10 Mbps old bus, equal share for 30 users is 0.333 Mbps each. With 1 Gbps switched access ports, each PC has a dedicated 1 Gbps full-duplex link; with a 10 Gbps core uplink, a simple equal-share upper bound is 333 Mbps per simultaneously active user. Actual throughput depends on server and uplink capacity. An illustrative 600 Mbps usable Wi-Fi 6 AP shared by 30 active users gives 20 Mbps each; wired switching is more predictable for large file transfers.

## Task 2 – How Many Links Can the Hospital Afford? (8 marks)
For five blocks, bus uses 4 backbone segments, ring 5 links, star 5 links and full mesh 10 links. Each link uses two fibre ports. At ₹60,000 per run and ₹18,000 per port, each link costs ₹96,000. Totals: bus ₹3,84,000; ring ₹4,80,000; star ₹4,80,000; mesh ₹9,60,000.

A bus or star can isolate a critical block after one cable cut. A ring and full mesh survive any single link failure. The least-cost design satisfying the stated Emergency and Operating Theatre requirement is a five-spoke star plus one direct Emergency–Theatre link: six links, twelve ports and ₹5,76,000. Each critical block has two paths to the data centre through the other. This protects the two named blocks but not the other three blocks from a single access-link cut. A five-block ring costs ₹4,80,000, survives one cut but may be partitioned by two cuts. The hybrid costs ₹96,000 more but directly protects the two critical buildings.

## Task 3 – Devices, Media and Cabling (9 marks)
The consulting runs (35–80 m) and waiting-hall AP run (60 m) are within the 90 m permanent-link and 100 m channel limits. The 96 m pharmacy run exceeds the permanent-link limit and leaves insufficient patch-cord margin; move the IDF or use fibre. The 420 m main-building link must use fibre because copper Ethernet channel length is limited to 100 m. Use managed Layer-2 access switches, Layer-3 distribution, router/firewall and wireless APs; avoid hubs. Each switch access port is a separate collision domain, while each VLAN is a broadcast domain.

T568A at one end and T568B at the other creates a crossover cable. Auto-MDIX often allows modern equipment to use it, but consistent T568B termination is preferred. T568B pin order is white-orange, orange, white-green, blue, white-blue, green, white-brown, brown. A scalable BOM uses measured route lengths ×1.10 spare, patch panels, keystone jacks, patch cords, fibre LIU/transceivers and telecom racks. The 420 m fibre route requires 462 m including 10% spare. Fibre avoids powered mid-span switches and does not conduct lightning-induced electrical surges between buildings. Cat6A would need at least five segments and four intermediate switches for 420 m.

## Task 4 – Shared Media, WLAN and WAN (7 marks)
Pure ALOHA throughput maximum is 18.4%; slotted ALOHA is 36.8%. The 2,500 m Ethernet cable has 12.5 μs one-way and 25 μs round-trip propagation. At 10 Mbps, 250 bits (31.25 bytes) can be sent during that interval; the standard 10 Mbps Ethernet minimum frame is 64 bytes. Switched full-duplex Ethernet has no collisions; Wi-Fi remains a shared radio medium and uses CSMA/CA.

For 300 waiting-hall phones, planning at 25 active clients per AP gives 12 APs, to be validated by site survey. Use 2.4 GHz channels 1, 6 and 11 with spatial reuse; assign non-overlapping 5 GHz channels to adjacent APs. Wi-Fi 6 OFDMA divides channel resources among clients, MU-MIMO serves multiple clients concurrently and BSS colouring improves spatial reuse. Bluetooth LE is suitable for low-rate medical sensors, not high-rate imaging.

An ATM cell has 5-byte header and 48-byte payload, giving 9.43% header overhead. Ethernet header plus FCS is 18 bytes over a 1518-byte frame, about 1.19%. Frame Relay uses DLCI, ATM uses VPI/VCI and MPLS uses labels. Internet VPN is cheaper and flexible but cannot guarantee public-internet delay or bandwidth. MPLS costs more but can provide contracted QoS/SLAs; choose it if predictable clinical video quality justifies the recurring premium.

## Task 5 – Separate the Guests from the Office (7 marks)
Create VLAN 10 Office, VLAN 20 CCTV and VLAN 30 Guest Wi-Fi. Configure access ports and an 802.1Q trunk carrying only VLANs 10, 20 and 30. The 802.1Q tag adds 4 bytes per frame. Router-on-a-stick provides gateways 192.168.10.1, 192.168.20.1 and 192.168.30.1. Apply an inbound ACL on the guest subinterface to deny private internal networks and permit other destinations. Before VLAN separation, the flat LAN is one broadcast domain; afterwards there are three broadcast domains. A separate physical guest switch offers stronger physical separation but costs more and requires more management; VLANs are generally more economical.

## Task 6 – New University Campus Design (13 marks)
Use a hierarchical hybrid design with redundant Layer-3 core switches, distribution for each building, star access switches and fibre links. The data centre and each building connect to both core switches. Dual ISP routers/firewalls provide internet redundancy. Cat6A serves horizontal runs; single-mode fibre links buildings. Wi-Fi 6 APs provide campus wireless. VLANs separate staff, students, guests, CCTV, labs, servers, network management and AV.

Use private aggregate 10.40.0.0/16 with VLAN subnets: staff 10.40.0.0/22, students 10.40.4.0/20, guest 10.40.20.0/21, CCTV 10.40.28.0/22, labs 10.40.32.0/22, servers 10.40.36.0/24, management 10.40.37.0/24 and auditorium 10.40.38.0/23. These ranges do not overlap. Planning examples use four 10G access uplinks to a 40G distribution uplink (1:1) and eight 10G uplinks to two 40G uplinks (1:1). Actual sizing must use busy-hour measurements.

A collapsed core can reduce device cost but a single switch failure may disconnect the whole campus. For a ten-year design, a redundant core/distribution architecture provides better resilience. Build a reduced Packet Tracer topology with two core switches, two building switches, representative PCs, VLANs, server and two ISP links; verify VLAN isolation and alternate-path operation after one core link is disabled.

## Conclusion
The designs replace shared, fragile media with structured switched networks, use fibre where distance and resilience require it, separate traffic with VLANs and apply redundant paths to critical buildings. Calculations support the topology, cabling and WAN choices. Packet Tracer project files, screenshots and actual test outputs must be captured during local execution before final submission.

## Evidence status
Python programs and configuration templates are supplied in this repository. The Packet Tracer .pkt files, actual ping results, cabling practical photos and software-version details must be added after testing on the student's computer; no unperformed test is claimed as completed.
