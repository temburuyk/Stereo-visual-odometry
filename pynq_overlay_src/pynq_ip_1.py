from pynq import Overlay

overlay = Overlay('/home/xilinx/SVO/Stereo-visual-odometry/design_1.bit')

overlay

mul_ip = overlay.mat_multiply_0

mul_ip

#mul_ip.register_map

mul_ip.read(0x0c)