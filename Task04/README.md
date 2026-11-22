# Task 4 – Shared Media, WLAN and WAN (7 marks)

## Multiple access
Pure ALOHA maximum throughput is 1/(2e) = 0.184, or **18.4%** of channel capacity. Slotted ALOHA is 1/e = 0.368, or **36.8%**.

For 10 Mbps shared Ethernet over 2,500 m at 2×10^8 m/s, one-way propagation = 12.5 μs; round trip = 25 μs. Bits sent during the round trip = 10,000,000×25×10^-6 = 250 bits = 31.25 bytes. The theoretical minimum from this cable delay is therefore about 32 bytes. Classic 10 Mbps Ethernet uses a 512-bit slot time and a 64-byte minimum MAC frame, which is larger and is the standard minimum. Switched full-duplex Ethernet has dedicated point-to-point links and no collisions, so CSMA/CD is not used. Wi-Fi is a shared radio medium and uses CSMA/CA to reduce collision probability.

## Waiting hall WLAN
Planning assumption: 25 concurrently active clients per AP gives 300/25 = **12 APs**. Actual AP count must be validated with a site survey, capacity and coverage. Use 2.4 GHz channels 1, 6 and 11 with channel reuse only between sufficiently separated APs. Use non-overlapping 5 GHz channels (for example 36, 40, 44, 48, 149, 153, 157, 161 subject to local regulations and device support). Avoid assigning the same channel to adjacent APs.
Wi-Fi 6 OFDMA divides a channel into resource units for multiple clients; MU-MIMO serves multiple clients concurrently; BSS colouring helps devices distinguish overlapping networks and reuse airtime more efficiently. Bluetooth Low Energy suits low-rate nearby sensors/wearables; it is not suitable as the primary transport for high-rate imaging or real-time multi-camera video.

## Backbone and WAN
ATM cell = 5-byte header + 48-byte payload = 53 bytes. Header fraction = 5/53 = **9.43%**; payload efficiency = 90.57%. Ethernet with 1500-byte payload and 14-byte header + 4-byte FCS has 18/1518 = **1.19%** frame overhead (excluding preamble and inter-frame gap).
Frame Relay identifies a virtual circuit with DLCI; ATM uses VPI/VCI; MPLS forwards using labels.

For three clinics, an internet VPN is lower cost and flexible but depends on public-internet congestion and does not inherently guarantee bandwidth or delay. MPLS is provider-managed and can offer contracted QoS/SLAs, usually at higher recurring cost. If video consultations need predictable delay/jitter, MPLS may justify the premium; otherwise use site-to-site IPsec VPN with dual ISPs and QoS.
