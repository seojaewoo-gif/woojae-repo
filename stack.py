class Stack:
    def __init__(self):
        self._data = []

    def push(self, x: int) -> None:
        """정수 x를 스택에 삽입"""
        self._data.append(x)  # list의 맨 뒤를 스택의 top으로 사용

    def pop(self) -> int:
        """가장 위 값을 제거하고 반환. 비어 있으면 -1"""
        return self._data.pop() if self._data else -1

    def top(self) -> int:
        """가장 위 값을 반환(제거 X). 비어 있으면 -1"""
        return self._data[-1] if self._data else -1

    def is_empty(self) -> bool:
        """스택이 비었으면 True, 아니면 False"""
        return len(self._data) == 0

    def __len__(self) -> int:
        """원소 개수 반환(옵션)"""
        return len(self._data)


s = Stack()
print(s.is_empty())  # True
print(s.pop())       # -1 (비었으므로)

s.push(3)
s.push(7)
s.push(5)

print(s.top())       # 5
print(s.pop())       # 5
print(s.top())       # 7
print(s.is_empty())  # False
print(len(s))        # 2
