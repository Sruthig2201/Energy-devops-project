# Energy Monitoring System (EEE + DevOps)

voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))
time = float(input("Enter Time (hours): "))

power = voltage * current          # P = V * I
energy = power * time              # Energy in Wh

print("\n--- Energy Report ---")
print(f"Voltage : {voltage} V")
print(f"Current : {current} A")
print(f"Power   : {power} W")
print(f"Energy  : {energy} Wh")

# Status detection

from datetime import datetime 
# Threshold values 
SAFE_POWER_LIMIT = 1000      #WATTS
WARNING_LIMIT = 800
if power > SAFE_POWER_LIMIT:
    status = "CRITICAL OVERLOAD"
elif power > WARNING_LIMIT:
    status = "WARNING: High Load"
else:
    status = "NORMAL OPERATION"
def relay_trip(power):
    if power > SAFE_POWER_LIMIT:
        return "TRIP ⚡ Overload detected! Circuit breaker opened."
    elif power > WARNING_LIMIT:
        return "WARNING ⚠ High load. Approaching trip limit."
    else:
        return "NORMAL ✅ Load within safe limit."
status = relay_trip(power)

print("Status :", status)
# Display report
print("\n--- Energy Report ---")
print(f"Voltage : {voltage} V")
print(f"Current : {current} A")
print(f"Power   : {power} W")
print(f"Energy  : {energy} Wh")
print(f"Status  : {status}")

# Logging data
log_entry = (
    f"{datetime.now()} | "
    f"V={voltage}V | I={current}A | "
    f"P={power}W | E={energy}Wh | "
    f"Status={status}\n"
)

with open("energy_log.txt", "a") as file:
    file.write(log_entry)













































