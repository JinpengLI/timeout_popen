timeout_popen
=============


Prepartion
----------
You need to install unbuffer in ubuntu.
see http://manpages.ubuntu.com/manpages/lucid/man1/expect_unbuffer.1.html

Main features
-------------

```
1. timeout_command can run subprocess.Popen within limited time.

2. it can read stdout (stardand output) asynchronously
```

An example is shown in the main function of timeout_command.py 

Reference:
http://stackoverflow.com/questions/1191374/subprocess-with-timeout
