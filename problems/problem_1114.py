# 1114. Print in Order
#
# Suppose we have a class:
#
# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
#
# The same instance of Foo will be passed to three different threads. Thread A
# will call first(), thread B will call second(), and thread C will call
# third(). Design a mechanism and modify the program to ensure that second() is
# executed after first(), and third() is executed after second().
#
# Note:
#
# We do not know how the threads will be scheduled in the operating system, even
# though the numbers in the input seem to imply the ordering. The input format
# you see is mainly to ensure our tests' comprehensiveness.
#
# Constraints:
#
# - nums is a permutation of [1, 2, 3].


from threading import Lock
from typing import Callable


class Foo:
    def __init__(self):
        self.first_job_done = Lock()
        self.second_job_done = Lock()
        self.first_job_done.acquire()
        self.second_job_done.acquire()

    def first(self, print_first: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print_first()
        self.first_job_done.release()

    def second(self, print_second: "Callable[[], None]") -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.first_job_done:
            print_second()
            self.second_job_done.release()

    def third(self, print_third: "Callable[[], None]") -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.second_job_done:
            print_third()
