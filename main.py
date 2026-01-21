# Energy Monitoring System (EEE + DevOps)


import os

voltage = float(os.getenv("VOLTAGE", 230))
current = float(os.getenv("CURRENT", 5))
time = float(os.getenv("TIME", 2))

power = voltage * current
energy = power * time

SAFE_POWER_LIMIT = 1000  # Relay threshold

print("\n--- Energy Report ---")
print(f"Voltage : {voltage} V")
print(f"Current : {current} A")
print(f"Power   : {power} W")
print(f"Energy  : {energy} Wh")

if power > SAFE_POWER_LIMIT:
    status = "RELAY TRIP: OVERLOAD DETECTED"
else:
    status = "POWER NORMAL"

print("Status :", status)

# Logging data
log_entry = (
    f"{datetime.now()} | "
    f"V={voltage}V | I={current}A | "
    f"P={power}W | E={energy}Wh | "
    f"Status={status}\n"
)

with open("energy_log.txt", "a") as file:
    file.write(log_entry)













































