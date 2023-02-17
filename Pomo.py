#!/usr/bin/env python
# Adapted from : http://code.activestate.com/recipes/577358-pomodoro-timer/
from __future__ import print_function
from clize import run
from sigtools import modifiers
import sys
import time
import subprocess
from datetime import datetime
import os
import configparser

try:
    from PyQt5.QtWidgets import QMessageBox
    from PyQt5.Qt import QApplication
except ImportError:
    has_qt = False
else:
    has_qt = True


display = print
script_dir = os.path.dirname(__file__)
ALARM_FILE_DIRS = [
    '.',
    script_dir,
    sys.prefix,
    os.path.join(script_dir, "..", ".."),
]
ALARM_FILENAME = 'clock.mp3'
for alarm_file_dir in ALARM_FILE_DIRS:
    ALARM_FILE = os.path.join(alarm_file_dir, ALARM_FILENAME)
    if os.path.exists(ALARM_FILE):
        break
ALARM_CMD_FFPLAY = ["ffplay", "-nodisp", "-autoexit"]
ALARM_CMD_MPG123 = ["mpg123"]
ALARM_CMDS = (ALARM_CMD_MPG123, ALARM_CMD_FFPLAY)
DATA_FILENAME = os.path.expanduser("~/.pomodoro")
CONFIG_FILENAME = os.path.expanduser("~/.pomodoro.conf")
DEV_NULL = open(os.devnull, "w")


# Parsing config file :
config = configparser.ConfigParser()
config.read(CONFIG_FILENAME)
if 'DEFAULTS' not in config : #if the config doesn't exist or is of the wrong format
    #writes the default config to the file
    config['DEFAULTS'] = {'work':'25', 'rest':'5', 'long':'15', 'cycles':'4', 'start':'0', 'repeat':'0', 'alarm':'True', 'notif':'False', 'timer':'False'}
    with open(CONFIG_FILENAME, 'w') as configfile:
        config.write(configfile)
    config.read(CONFIG_FILENAME)
work_default = config['DEFAULTS'].getint('work', fallback='25')
rest_default = config['DEFAULTS'].getint('rest', fallback='5')
long_default = config['DEFAULTS'].getint('long', fallback='15')
cycles_default = config['DEFAULTS'].getint('cycles', fallback='4')
start_default = config['DEFAULTS'].getint('start', fallback='0')
repeat_default = config['DEFAULTS'].getint('repeat', fallback='0')
alarm_default = config['DEFAULTS'].getboolean('alarm', fallback='True')
notif_default = config['DEFAULTS'].getboolean('notif', fallback='False')
timer_default = config['DEFAULTS'].getboolean('timer', fallback='True')


def notify(title, content, more=''):
    if not has_qt:
        return
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(content)
    msg.setWindowTitle(title)
    msg.setDetailedText(more)
    msg.show()
    app.exec_()


def tick(duration, timer):
    try:
        if timer:
            cli_timer(duration)
        else:
            time.sleep(duration)
    except KeyboardInterrupt:
        display("Interrupting")
        interrupt = True
    else:
        interrupt = False
    return interrupt


def play_alarm(filename):
    for alarm_cmd in ALARM_CMDS:
        cmd = alarm_cmd + [filename]
        try:
            p = subprocess.Popen(cmd, stdout=DEV_NULL, stderr=subprocess.PIPE)
            p.wait()
        except OSError:
            # error, try the next alarm cmd
            continue
        else:
            # successful
            return


def write_pomo(start, stop, tag):
    duration = (stop - start).total_seconds() / 60.
    line = "{0},{1},{2},{3}\n".format(tag, start, stop, duration)
    if not os.path.exists(DATA_FILENAME):
        fd = open(DATA_FILENAME, "w")
        fd.write("work,start,end,duration\n")
    else:
        fd = open(DATA_FILENAME, "a")
    fd.write(line)
    fd.close()

def cli_timer(duration):
    for remaining in range(duration, -1, -1):
        sys.stdout.write("\r")
        hours, rem = divmod(remaining, 3600)
        mins, secs = divmod(rem, 60)
        sys.stdout.write("Time remaining: {:0>2}:{:0>2}:{:0>2}".format(hours, mins, secs))
        sys.stdout.flush()
        time.sleep(1)
    print('\n')

@modifiers.kwoargs('long', 'cycles', 'start', 'repeat', 'alarm', 'notif', 'timer')
def main(work=work_default, rest=rest_default, long=long_default, cycles=cycles_default, start=start_default, repeat=repeat_default, alarm=alarm_default, notif=notif_default, timer=timer_default):
    """
    work : int
        nb of minuntes of work
    rest : int
        nb of minutes of rest
    long : int
        nb of minutes of long rest after completion of a set
    cycles : int
        nb of cycles in a set
    start : int
        nb of cycles already completed in the set
    repeat : int
        nb of cycles work-rest to do (use 0 to continue until user interruption)
    alarm : bool
        whether to play an alarm each time a pomodoro is finished or started
    notif : bool
        whether to send a message box each time a pomodoro is finished or
        started
    timer : bool
        whether to have cli timer visible
    """
    cycle = start
    while repeat <= 0 or cycle != repeat:

        # If repeat is >0, continue until cycle == repeat. If repeat <=0, continue until user interrupts.
        display("Work now, cycle {}/{}".format((cycle % cycles) + 1, cycles))

        start = datetime.now()
        interrupted = tick(int(work) * 60, timer)
        if interrupted:
            break
        stop = datetime.now()
        write_pomo(start, stop, "work")
        if alarm:
            play_alarm(ALARM_FILE)

        if (cycle + 1) % cycles == 0:
            # If set complete, long rest
            rest_time = int(long) * 60
            if notif:
                notify('pomodoro', 'Finished set, long rest now.')
            display("Long rest now")
        else:
            # If partial set, normal (short) rest
            rest_time = int(rest) * 60
            if notif:
                notify('pomodoro', 'Finished pomo, rest now.')
            display("Rest now")
        start = datetime.now()
        interrupted = tick(rest_time, timer)
        if interrupted:
            break
        stop = datetime.now()
        write_pomo(start, stop, "rest")

        if alarm:
            play_alarm(ALARM_FILE)
        if notif:
            notify('pomodoro', 'Finished rest, work now.')
        display("Cycle complete")
        cycle += 1


if __name__ == "__main__":
    run(main)