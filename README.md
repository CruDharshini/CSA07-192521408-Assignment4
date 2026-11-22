# CSA07 – Computer Networks | Assignment 4 (CO4)
**Student:** Dharshini | **Register No.:** 192521408  
**Department:** Information Technology | **Academic Year:** 2026–2027  
**Course Outcome:** CO4 – Network topology, media, switching, VLANs and routing  
**Total:** 50 marks

## Tasks
| Folder | Topic | Marks |
|---|---|---:|
| Task01 | Office network redesign | 6 |
| Task02 | Reliable hospital topology | 8 |
| Task03 | Devices, media, cabling and BOM | 9 |
| Task04 | Shared media, WLAN, backbone and WAN | 7 |
| Task05 | VLANs and switch configuration | 7 |
| Task06 | University campus design challenge | 13 |
| Report | Consolidated written answers | — |

## Requirements
- Python 3.10+ (standard library only)
- Cisco Packet Tracer for the network simulations/configurations
- Optional: Wireshark for packet inspection
- Cisco IOS-like commands are provided as templates; interface names and available features depend on the Packet Tracer device model.

## Run Python programs
From the repository root:
```bash
python Task01/task1_code.py
python Task02/task2_code.py
python Task03/task3_code.py
python Task04/task4_code.py
python Task06/task6_code.py
```
On Windows, use `py` if `python` is not recognised. Task05 contains the completed switch and router configurations.

## Assumptions
Where the assignment does not give a bandwidth, device count or unit price, the report states an explicit planning assumption rather than presenting it as a measured fact. Recalculate these values if the instructor supplies different figures.

## Evidence still to capture locally
Packet Tracer project files (.pkt), screenshots of topology/configuration, actual ping tests, cable-test evidence and software versions must be generated on the student's computer. They are not fabricated in this repository. Add them to each task's `evidence/` folder and update this README with the actual OS, Python and Packet Tracer versions used.

## Suggested validation
1. Run every Python script and save its terminal output.
2. Build the reduced Packet Tracer topologies for Tasks 2, 5 and 6.
3. Test connectivity before and after link failure/VLAN changes.
4. Capture `show vlan brief`, `show interfaces trunk`, `show ip route` and ping outputs as applicable.
5. Commit evidence progressively, at least one commit per task.
