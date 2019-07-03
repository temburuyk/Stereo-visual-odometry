from pynq import Overlay
from pynq import Xlnk
import numpy as np


overlay = Overlay('/home/xilinx/SVO/Stereo-visual-odometry/design_1.bit')

overlay

mul_ip = overlay.mat_multiply_0

mul_ip

mul_ip.register_map

print(overlay.ip_dict.keys())

mul_ip.read(0x0c)

xlnk = Xlnk()

A_buffer = xlnk.cma_array(shape=(9,), dtype=np.ubyte)
B_buffer = xlnk.cma_array(shape=(9,), dtype=np.ubyte)
C_buffer = xlnk.cma_array(shape=(9,), dtype=np.ubyte)

A_dram_addr = A_buffer.physical_address
B_dram_addr = B_buffer.physical_address
C_dram_addr = C_buffer.physical_address

print(hex(A_dram_addr)) 

A_reg_offset = mul_ip.register_map.A.address
B_reg_offset = mul_ip.register_map.B.address
C_reg_offset = mul_ip.register_map.C.address
CTRL_reg_offset = mul_ip.register_map.CTRL.address

for i in range(9):
	A_buffer[i]=i
	B_buffer[i]=8-i

mul_ip.write(A_reg_offset,A_dram_addr)
mul_ip.write(B_reg_offset,B_dram_addr)
mul_ip.write(C_reg_offset,C_dram_addr)

mul_ip.write(CTRL_reg_offset,1)
cycles = 0
#print(mul_ip.register_map.CTRL)
#print(mul_ip.register_map.CTRL.AP_START)
#print(mul_ip.register_map.CTRL.AP_DONE)
while(not(mul_ip.register_map.CTRL.AP_DONE)):
	print(cycles)
	cycles = cycles+1

print(A_buffer)
print(B_buffer)
print(C_buffer)

