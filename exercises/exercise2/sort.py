from source.datastructures.stack import Stack


def sort(stack1: Stack, stack2: Stack, stack3: Stack) -> None:
    while not stack1.stack_empty():
        stack2.push(stack1.pop())

    src = stack2
    dst = stack3

    while not src.stack_empty():
        element1 = src.pop()

        while not src.stack_empty():
            if (element2 := src.pop()) > element1:
                element1, element2 = element2, element1

            dst.push(element2)

        stack1.push(element1)
        src, dst = dst, src
