리스트를 이용하여 기본적인 스택(stack)을 구현하세요. (다음 내용을 고려할 것.) push(x): 정수 x를 스택에 삽입 pop(): 스택에서 가장 위의 값을 제거하고 반환. 만약 스택이 비어 있다면 -1을 반환 top(): 스택의 가장 위에 있는 값을 반환. 만약 스택이 비어 있다면 -1을 반환 is_empty(): 스택이 비어 있으면 True, 아니면 False를 반환

<img width="1110" height="794" alt="image" src="https://github.com/user-attachments/assets/0aa540d4-dfa2-4a52-9fea-07f99aedc62f" />

Stack 이라는 클래스를 선언하고, LIFO(LAST IN FIRST OUT) 규칙 적용
push 메서드를 통해 x를 top에 삽입 
리스트가 비어 있을 때 list.pop을 직접 호출하면 IndexError가 발생하기 때문에, 빈 리스트로 해당 사항 방지


1)push(x)
- 새 원소 x를 스택의 맨 위에 올린다.
- 시간 복잡도: 평균 O(1)
2)POP
