


# def run_purity_check():
#     print("--- D-CORP FOUNDRY CONTROL SYSTEM ---")
#     print("MOLTEN SPILL ALLOY MONITOR v1.1.2")
#
#     try:
#         temperature = input("\nEnter Core Temperature (in Celsius): ")
#         core_temperature = float(temperature)
#     except ValueError:
#         print(f'\n[ERROR] Input must be a number. Shutting down system...')
#         return
#
#     if core_temperature > 1670:
#         print(f"\n[WARNING] Temperature {core_temperature:.1f}C is critical!")
#         print("ALERT: Excess heat detected. Purity is compromised. Initiate emergency cooling protocol.")
#
#     elif core_temperature >= 1500:
#         print(f"\n[STATUS] Temperature {core_temperature:.1f}C is normal.")
#         print("Purity Check: 99.5%. Batch approved for production.")
#
#     else:
#         print(f"\n[STATUS] Temperature {core_temperature:.1f}C is too low.")
#         print("Molten is cooling too fast. Incomplete production. Purity Check: [FAILED]")
#
#
# if __name__ == "__main__":
#     run_purity_check()