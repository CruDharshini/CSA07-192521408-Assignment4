"""Campus address and uplink oversubscription checks."""
import ipaddress

vlans = {
    10: "10.40.0.0/22",
    20: "10.40.4.0/20",
    30: "10.40.20.0/21",
    40: "10.40.28.0/22",
    50: "10.40.32.0/22",
    60: "10.40.36.0/24",
    70: "10.40.37.0/24",
    80: "10.40.38.0/23",
}

def main():
    networks = [(v, ipaddress.ip_network(c)) for v, c in vlans.items()]
    for i, (vid, net) in enumerate(networks):
        print(f"VLAN {vid:2}: {net} usable hosts={net.num_addresses - 2}")
        for other_id, other in networks[i + 1:]:
            if net.overlaps(other):
                raise ValueError(f"Overlap: VLAN {vid} and VLAN {other_id}")
    print("Address plan: no overlaps")
    access_aggregate = 4 * 10_000  # four 10G access-switch uplinks
    distribution = 40_000
    print(f"4 x 10G to 40G uplink oversubscription: {access_aggregate/distribution:.1f}:1")
    access_aggregate = 8 * 10_000
    distribution = 2 * 40_000
    print(f"8 x 10G to 2 x 40G uplinks: {access_aggregate/distribution:.1f}:1")
    print("These are design examples; replace with measured busy-hour traffic.")

if __name__ == "__main__":
    main()
