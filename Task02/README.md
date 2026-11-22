# Task 2 – How Many Links Can the Hospital Afford? (8 marks)

Five blocks: Emergency (E), Outpatient (O), Operating Theatres (T), Laboratory (L), Administration (A). Servers are at the central data-centre/core. One fibre run costs Rs 60,000; each fibre port costs Rs 18,000 at each end. Cost per link = 60,000 + 2×18,000 = Rs 96,000.

## Topology comparison
Treat each inter-block cable/run as one link; for a bus, count the four backbone segments joining five blocks. Port count is two per link.
| Topology | Links | Link ports | Fibre cost | Port cost | Total |
|---|---:|---:|---:|---:|---:|
| Bus | 4 | 8 | ₹2,40,000 | ₹1,44,000 | ₹3,84,000 |
| Ring | 5 | 10 | ₹3,00,000 | ₹1,80,000 | ₹4,80,000 |
| Star (data centre centre) | 5 | 10 | ₹3,00,000 | ₹1,80,000 | ₹4,80,000 |
| Full mesh | 10 | 20 | ₹6,00,000 | ₹3,60,000 | ₹9,60,000 |

## Single cable failure
- Bus: a cut in the backbone separates downstream blocks; emergency/theatres can be isolated.
- Ring: any one cut leaves the ring as a connected path in the opposite direction.
- Star: a cut to Emergency or Theatres disconnects that block; other spokes remain connected.
- Full mesh: one cable cut does not disconnect any block because alternate paths exist.

## Least-cost hybrid satisfying the critical rule
Use a star from the data centre to all five blocks, plus one additional direct E–T fibre link. Links = 6; ports = 12. Fibre = 6×₹60,000 = ₹3,60,000; port cost = 12×₹18,000 = ₹2,16,000; total = **₹5,76,000**.

Emergency and theatres each have two independent paths to the data centre: their direct star link and the route through the other critical block. If any one cable is cut, both critical blocks retain a route to the data centre. The other three blocks have single links; their availability was not included in the stated critical requirement. This is cheaper than a full mesh and more reliable for the two specified blocks than a simple star.

## Ring alternative
A five-block ring uses 5 links, 10 ports and costs ₹4,80,000. It survives any one ring cable cut, but two cuts can partition the ring depending on their locations. The proposed six-link hybrid costs ₹96,000 more but specifically gives E and T two independent routes to the server. It does not guarantee that O, L or A survives a cable cut.

## Packet Tracer
Build five block switches and a central L3/core switch. Create direct links from core to each block plus E–T. Test pings from E and T to the server, shut down each core-to-critical-block link one at a time, and repeat. Save the actual .pkt and screenshots under `evidence/`.
