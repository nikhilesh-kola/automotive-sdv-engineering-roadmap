voltage = float(input("Enter Battery Voltage: "))
capacity_ah = float(input("Enter Battery Capacity in Ah: "))
energy_wh = voltage * capacity_ah
energy_kwh = energy_wh / 1000
print("\nBattery Energy")
print(f"Energy = {energy_wh:.2f} Wh")
print(f"Energy = {energy_kwh:.2f} KWh")