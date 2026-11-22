"""Office bandwidth and Wi-Fi sharing calculator."""
def main():
    users = 30
    old_bus_mbps = 10       # explicit planning assumption; not given in question
    access_port_mbps = 1000
    core_uplink_mbps = 10_000
    wifi_aggregate_mbps = 600  # illustrative usable throughput assumption

    print(f"Old shared bus equal-share: {old_bus_mbps / users:.3f} Mbps/user")
    print(f"New dedicated switch access: {access_port_mbps} Mbps/PC port")
    print(f"New core-uplink equal-share: {core_uplink_mbps / users:.1f} Mbps/user")
    print(f"Wi-Fi 6 equal-share estimate: {wifi_aggregate_mbps / users:.1f} Mbps/user")
    print("Note: actual throughput depends on traffic, uplinks, radio conditions and contention.")

if __name__ == "__main__":
    main()
