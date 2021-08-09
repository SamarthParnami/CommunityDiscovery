import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Stopwatch:
    def __init__(self):
        self._start_time = None
        self._stop_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter_ns()
    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        self._stop_time=time.perf_counter_ns()
        elapsed_time = self._stop_time - self._start_time
        return elapsed_time
    def elapsed(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        if self._stop_time is None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        return self._stop_time-self._stop_time


    def reset(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")
        if self._stop_time is None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")
        self._stop_time = None
        self._start_time = None
