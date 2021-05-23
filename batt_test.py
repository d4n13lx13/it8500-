
'''
Open Source Initiative OSI - The MIT License:Licensing
Tue, 2006-10-31 04:56 nelson
The MIT License
Copyright (c) 2009 BK Precision
'''

import pandas as pd
import sys
import dcload
import time
err = sys.stderr.write


def TalkToLoad(load, port, baudrate):
    def test(cmd, results):
        if results:
            print(cmd, "failed:")
            print("  ", results)
            exit(1)
        else:
            print(cmd)
    load.Initialize(port, baudrate)  # Open a serial connection
    print("Time from DC Load =", load.TimeNow())
    test("Set to remote control", load.SetRemoteControl())

    load.SetFunction('battery')
    print("Function =", load.GetFunction())

    load.TurnLoadOn()

    values = load.GetInputValues().split("\t")
    # wait for mode to switch (4th element in value array)

    testtable = pd.read_csv("filename.csv")
    print(testtable)
    # Assuming current points is the column named I,

    amppoints = testtable.loc[:, "A"]  # pandas series

    time.sleep(1)

    for i in amppoints:
        print(load.TimeNow())
        load.SetCCCurrent(i)
        print("batt I =", load.GetCCCurrent())
           # if mode changes back to 0x0 then the test is over
        if values[4] == '0x0':
            # test ended
            break
        i
        time.sleep(10)

    # set back to local
    test("Set to local control", load.SetLocalControl())

if __name__ == '__main__':
    port = '/dev/ttyUSB0'
    baudrate = 4800
    load = dcload.DCLoad()
    TalkToLoad(load, port, baudrate)
