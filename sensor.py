from serial import Serial, SerialException
import tkinter as tk
import tkinter.ttk as ttk
from serial import Serial
from serial.tools.list_ports import comports
from tkinter.messagebox import showerror

from threading import Thread, Lock # we'll use Lock later ;)

def detached_callback(f):
    return lambda *args, **kwargs: Thread(target=f, args=args, kwargs=kwargs).start()

S_OK: int = 0xaa
S_ERR: int = 0xff
MOTOR_START: int = 0x02
MOTOR_STOP: int = 0x03
MOTOR_SET_SPEED: int = 0x04

with Serial('/dev/cu.usbmodem101', 9600) as ser:
    # ser.write(bytes([0x1]))
    # temp = ser.read()
    print(0)
    # print(bytes([0xaa]))
    # print(temp == bytes([0xaa]))

    # ser.write(bytes([0x0]))
    # print(ser.read() == bytes([0xaa]))

    # ser.write(bytes([0x2]))
    # print(temp)
    # print(bytes([0xaa]))
    # print(ser.read() == bytes([0xaa]))


def detached_callback(f):
    return lambda *args, **kwargs: Thread(target=f, args=args, kwargs=kwargs).start()

class App(tk.Tk):
    ser: Serial
    
    def __init__(self):
        super().__init__()
        
        self.title("Rod lifter")
        
        self.port = tk.StringVar() # add this
        self.led = tk.BooleanVar()
        self.speed = tk.IntVar(value=127) 

        ttk.Button(self, text='Trigger', command=self.update_sensor).pack()


        SerialPortal(self)
        
    def connect(self):
        self.ser = Serial(self.port.get(), 9600)
        # print('hi')
        print(self.ser.is_open)
        
    def disconnect(self):
        self.ser.close()
            
        SerialPortal(self) # display portal to reconnect

    @detached_callback       
    def send_invalid(self):
        self.write(bytes([0x10]))


    @detached_callback
    def update_speed(self, _=None):
        self.write(bytes([self.speed.get()]))
        print(self.speed.get())

    @detached_callback
    def update_sensor(self, _=None):
        self.write(bytes([1]))
        for i in range(13):
            value = (self.ser.read())
            print(value)
            if (value == bytes([0xaa])):
                print("proceed to flash the led light")
                self.write(bytes([2]))
                result = self.ser.read()
                if (result == bytes([0xaa])):
                    print("light flashed with no error")
                else:
                    print("error")

    def write(self, b: bytes):
        # self.ser.write(b)
        try:
            self.ser.write(b)
            if int.from_bytes(self.ser.read(), 'big') == S_ERR:
                showerror('Device Error', 'The device reported an invalid command.')
        except SerialException:
            showerror('Serial Error', 'Write failed.')
            
    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.disconnect()

        
class SerialPortal(tk.Toplevel):
    def __init__(self, parent: App):
        super().__init__(parent)
        
        self.parent = parent
        self.parent.withdraw() # hide App until connected
        
        ttk.OptionMenu(self, parent.port, '', *[d.device for d in comports()]).pack()
        ttk.Button(self, text='Connect', command=self.connect, default='active').pack()
        
    def connect(self):
        self.parent.connect()
        self.destroy()
        self.parent.deiconify() # reveal App\
        
        
class LockedSerial(Serial):
    _lock: Lock = Lock()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def read(self, size=1) -> bytes:
        with self._lock:
            return super().read(size)
        
    def write(self, b: bytes, /) -> int | None:
        with self._lock:
            return super().write(b)
            
    def close(self):
        with self._lock:
            super().close()
        
if __name__ == '__main__':
    with App() as app:
        app.mainloop()
    
        

            





