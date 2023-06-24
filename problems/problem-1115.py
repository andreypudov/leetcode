# Suppose you are given the following code:
#
# class FooBar {
#   public void foo() {
#     for (int i = 0; i < n; i++) {
#       print("foo");
#     }
#   }
#
#   public void bar() {
#     for (int i = 0; i < n; i++) {
#       print("bar");
#     }
#   }
# }
#
# The same instance of FooBar will be passed to two different threads:
#
#     thread A will call foo(), while
#     thread B will call bar().
#
# Modify the given program to output "foobar" n times.

from threading import Barrier, Event
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.canBar = Event()
        self.canBar.clear()
        self.canFoo = Event()
        self.canFoo.set()

    def foo(self, printFoo: "Callable[[], None]") -> None:
        for i in range(self.n):
            self.canFoo.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.canFoo.clear()
            self.canBar.set()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for i in range(self.n):
            self.canBar.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.canBar.clear()
            self.canFoo.set()
