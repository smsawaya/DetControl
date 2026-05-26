"""Contains functions used to interface with the bnc boxes"""

import serial
import time

#VARIABLES DEFINITION-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

LASER_COM_PORT = "COM6"
IGNITION_COM_PORT = "COM7"
BAUD = 9600
READ_TIMEOUT_S = 1.0


#FUNCTIONS------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def switch_preset(preset_number, box):
    """Send *RCL <n> to the BNC box; expect a line containing ``ok`` (case-insensitive)."""
    n = int(preset_number) #converts preset number to an integer
    port = LASER_COM_PORT if box == "laser" else IGNITION_COM_PORT
    ser = serial.Serial(port, BAUD, timeout=READ_TIMEOUT_S)
    try:  # send *RCL; raise if response line has no ok
        ser.reset_input_buffer()
        ser.write(b"*RCL %d\r\n" % n)
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept *RCL {n} (expected response containing 'ok'); got {line!r}"
            )
    finally:
        ser.close()

def arm(state, box):
    """Send :PULSE0:STATE ON or OFF to the BNC box; expect a line containing ``ok`` (case-insensitive)."""
    state = str(state).upper()
    port = LASER_COM_PORT if box == "laser" else IGNITION_COM_PORT
    ser = serial.Serial(port, BAUD, timeout=READ_TIMEOUT_S)
    try:
        ser.reset_input_buffer()
        ser.write(f":PULSE0:STATE {state}\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept :PULSE0:STATE {state} (expected response containing 'ok'); got {line!r}"
            )
    finally:
        ser.close()


def set_500(box):
    """Send :PULSE0:STATE ON or OFF to the BNC box; expect a line containing ``ok`` (case-insensitive)."""
    state = str(state).upper()
    port = LASER_COM_PORT if box == "laser" else IGNITION_COM_PORT
    ser = serial.Serial(port, BAUD, timeout=READ_TIMEOUT_S)
    try:
        ser.reset_input_buffer()
        ser.write(f"T1:Wid 3000\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept T1:Wid 3000 (expected response containing 'ok'); got {line!r}"
            )
        ser.reset_input_buffer()
        ser.write(f"T1:Dly 2000000\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept T1:Dly 2000000 (expected response containing 'ok'); got {line!r}"
            )
        ser.reset_input_buffer()
        ser.write(f"T2:Wid 500\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept T2:Wid 500 (expected response containing 'ok'); got {line!r}"
            )
        ser.reset_input_buffer()
        ser.write(f"T2:Dly 0\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept T2:Dly 0 (expected response containing 'ok'); got {line!r}"
            )
        ser.reset_input_buffer()
        ser.write(f"T3:Wid 500\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept T3:Wid 500 (expected response containing 'ok'); got {line!r}"
            )
        ser.reset_input_buffer()
        ser.write(f"T3:Dly 2000\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept T3:Dly 2000 (expected response containing 'ok'); got {line!r}"
            )
        ser.reset_input_buffer()
        ser.write(f"T4:Wid 500\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept T4:Wid 500 (expected response containing 'ok'); got {line!r}"
            )
        ser.reset_input_buffer()
        ser.write(f"T4:Dly 2000\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept T4:Dly 2000 (expected response containing 'ok'); got {line!r}"
            )
        ser.reset_input_buffer()
        ser.write(f"RUN 1\r\n".encode())
        ser.flush()
        ser.readline()  # discard echo
        line = ser.readline()
        if b"ok" not in line.lower():
            raise RuntimeError(
                f"BNC box did not accept RUN 1 (expected response containing 'ok'); got {line!r}"
            )
    finally:
        ser.close()


'Main function used for testing the BNC box. Click run while in this file to test the BNC box.'
def main(): 
    print("Continuous Mode")
    switch_preset(9)
    time.sleep(5)
    print("Arming")
    arm("ON")
    time.sleep(10)
    switch_preset(12)
    print("Single Shot")
    print("Waiting for pulse...")
    time.sleep(5)
    print("Switching to continuous mode")
    switch_preset(9)
    time.sleep(10)
    print("Done")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
