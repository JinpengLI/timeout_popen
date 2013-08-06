# -*- coding: utf-8 -*-
import sys
import subprocess
import datetime
import os
import time
import signal

from threading  import Thread

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x
ON_POSIX = 'posix' in sys.builtin_module_names


def _enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()


def _read_buf(q):
    out = ""
    is_empty = False
    while not is_empty:
        try:  line = q.get_nowait() # or q.get(timeout=.1)
        except Empty:
            is_empty = True
        else: # got line
            out = out + line
    return out


def timeout_command(command, timeout):
    """call shell-command and either return its output or kill it
    if it doesn't normally exit within  seconds and return None"""

    start = datetime.datetime.now()
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    q = Queue()
    t = Thread(target=_enqueue_output, args=(process.stdout, q))
    t.daemon = True # thread dies with the program
    t.start()
    out = ""
    while process.poll() is None:
        out = out + _read_buf(q)
        ## You can print out here to debug asynchronously
        print out
        time.sleep(1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return None
    out = out + _read_buf(q)
    return out

if __name__ == '__main__':
    file_dir = os.path.dirname(os.path.abspath(__file__))
    path_speaker = os.path.join(file_dir, "speaker.py")
    print path_speaker
    cmd = [];
    cmd.append("unbuffer")
    cmd.append("python")
    cmd.append(path_speaker)
    print timeout_command(cmd, 40)
