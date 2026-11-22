"""Cable-limit and bill-of-materials helper."""
RUNS = {
    "consulting rooms (maximum stated)": 80,
    "pharmacy": 96,
    "waiting hall APs": 60,
    "main building": 420,
}
PERMANENT_LIMIT_M = 90
CHANNEL_LIMIT_M = 100
for name, length in RUNS.items():
    if length <= PERMANENT_LIMIT_M:
        result = "within 90 m permanent-link limit"
    elif length <= CHANNEL_LIMIT_M:
        result = "permanent-link violation; channel may fit only with very short patch cords"
    else:
        result = "exceeds copper channel limit; use fibre or add IDF"
    print(f"{name:34} {length:3} m: {result}")
print("420 m route with 10% spare:", 420 * 1.10, "m")
print("Copper segments needed for 420 m at <=100 m each:", 5)
print("Intermediate switches required for 5 segments:", 4)
