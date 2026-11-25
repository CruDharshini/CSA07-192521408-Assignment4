"""ALOHA, CSMA/CD and ATM overhead calculations."""
import math
pure = 1 / (2 * math.e)
slotted = 1 / math.e
rate = 10_000_000
distance = 2500
signal_speed = 2e8
one_way = distance / signal_speed
round_trip = 2 * one_way
bits = rate * round_trip
bytes_needed = bits / 8
atm_header = 5
atm_payload = 48
ethernet_overhead = 14 + 4
ethernet_payload = 1500
print(f"Pure ALOHA max: {pure:.4f} ({pure*100:.2f}%)")
print(f"Slotted ALOHA max: {slotted:.4f} ({slotted*100:.2f}%)")
print(f"Propagation one-way: {one_way*1e6:.2f} us; RTT: {round_trip*1e6:.2f} us")
print(f"Bits in RTT: {bits:.0f}; theoretical bytes: {bytes_needed:.2f}")
print("Standard Ethernet minimum MAC frame: 64 bytes")
print(f"ATM header fraction: {atm_header/(atm_header+atm_payload)*100:.2f}%")
print(f"Ethernet header+FCS fraction: {ethernet_overhead/(ethernet_payload+ethernet_overhead)*100:.2f}%")
print("Waiting-hall AP planning estimate:", math.ceil(300/25), "APs")
