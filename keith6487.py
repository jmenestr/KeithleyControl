__author__ = 'Justin M'
import visa


class K6487():
    def __init__(self,board = 0,address = 22):
        rm = visa.ResourceManager()
        self.ctrl = rm.open_resource('GPIB{}::{}::INSTR'.format(board,address))

    def reset(self):
        self.ctrl.write("*RST")

    def instr_init(self):
        self.reset()
        self.ctrl.write("SYST:ZCH OFF")
        self.ctrl.write("SOUR:VOLT:STAT on")

    def send(self,command):
        self.ctrl.write(command)

    def set_volt(self,volt):
        command = "SOUR:VOLT:AMPL {}".format(volt)
        self.ctrl.write(command)

    def write_data(self,output):
        pass
        #write data to output
