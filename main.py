import file
import Hill_Climbing as hc

# The main program is complete. Do not change this file.
data = file.read_dataset()
hc_instance = hc.Hill_Climbing(data)
hc_instance.run_hc(100)
