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

from threading import Event
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.can_bar = Event()
        self.can_bar.clear()
        self.can_foo = Event()
        self.can_foo.set()

    def foo(self, print_foo: "Callable[[], None]") -> None:
        for _ in range(self.n):
            self.can_foo.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            print_foo()
            self.can_foo.clear()
            self.can_bar.set()

    def bar(self, print_bar: "Callable[[], None]") -> None:
        for _ in range(self.n):
            self.can_bar.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            print_bar()
            self.can_bar.clear()
            self.can_foo.set()
