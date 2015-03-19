import visa
import time
import math

rm = visa.ResourceManager()
keith = rm.open_resource('GPIB0::22::INSTR')

data = []

def read(start,stop,step,pause,num_runs=1):
    start_volt = start
    stop_volt = stop
    if start > stop:
        volt_step_for = -math.fabs(step)
        volt_step_rev = math.fabs(step)
    elif start < stop:
        volt_step_for = math.fabs(step)
        volt_step_rev = -math.fabs(step)
    else:
        print("Start/Stop voltage cannot be same")
    instr_init()
    for i in range(0,num_runs):
        forward_scan(start_volt,stop_volt,pause,volt_step_for)
        print(i)
        reverse_scan(start_volt,stop_volt,pause,volt_step_rev)
        print(i)
    keith.write("SOUR:VOLT:AMPL 0")
    keith.write("SOUR:VOLT:STAT off")



def instr_init():
    keith.write("*RST")
    keith.write("SYST:ZCH OFF")
    keith.write("SOUR:VOLT:STAT on")

def forward_scan(start,stop,pause,step):
    v = start
    while v  <= stop:
        command = "SOUR:VOLT:AMPL {}".format(v)
        keith.write(command)
        time.sleep(pause)
        print(keith.query("READ?"))
        v += step

def reverse_scan(start,stop,pause,step):
    v = stop
    while v  >= start:
        command = "SOUR:VOLT:AMPL {}".format(v)
        keith.write(command)
        time.sleep(pause)
        print(keith.query("READ?"))
        v += step

read(-1,1,1,1,2)