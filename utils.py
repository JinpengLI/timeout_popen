# -*- coding: utf-8 -*-

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x
ON_POSIX = 'posix' in sys.builtin_module_names


def enqueue_output(out, queue):
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
    import subprocess, datetime, os, time, signal
    start = datetime.datetime.now()
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    q = Queue()
    t = Thread(target=enqueue_output, args=(process.stdout, q))
    t.daemon = True # thread dies with the program
    t.start()
    out = ""
    while process.poll() is None:
        out = out + _read_buf(q)
        time.sleep(1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return None
    out = out + _read_buf(q)
    return out
