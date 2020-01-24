TimeoutThreadPoolExecutor
============================

This library tries to solve my issue with 1000+ idle threads in Python 3.7 by using a backported
ThreadPoolExecutor (with thread reuse) and giving threads a TTL.

There is probably no reason to use this for short-lived threads.


Usage
-----

There are two ways to use this library, overwrite the default TheadPoolExecutor or use it directly.

To overwrite the default, do this as the first thing before any other thing your project does.

    from timeoutthreadpoolexecutor import TimeoutThreadPoolExecutor
    from concurrent.futures import thread
    thread.ThreadPoolExecutor = TimeoutThreadPoolExecutor

or

    from timeoutthreadpoolexecutor import TimeoutThreadPoolExecutor as ThreadPoolExecutor



License
-------

Same as Python, I guess.