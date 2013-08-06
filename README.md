timeout popen
=============


Preparation
-----------
You need to install unbuffer in ubuntu.
see http://manpages.ubuntu.com/manpages/lucid/man1/expect_unbuffer.1.html

Main features
-------------

```
1. timeout_command can run subprocess.Popen within limited time.

2. it can read stdout (standard output) asynchronously
```

An example is shown in the main function of timeout_command.py 

Reference
---------

1. http://stackoverflow.com/questions/1191374/subprocess-with-timeout

2. (small bug in below function when there is too many stdout in the buffer) http://howto.pui.ch/post/37471155682/set-timeout-for-a-shell-command-in-python
