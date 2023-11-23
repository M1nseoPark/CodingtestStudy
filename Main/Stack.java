interface Stack {
    void push(char item);
    char pop();
    char peek();
    void clear();
}

public class ArrayStack implements Stack {

    private int top;  // 스택 포인터 (현재 top 위치인 인덱스)
    private int stackSize;
    private char stackArr[];

    public ArrayStack(int stackSize) {
        top = -1;  // 스택 포인터 초기화 
        this.stackSize = stackSize;
        stackArr = new char[this.stackSize];  // 스택 배열 생성 
    }

    public void push(char item) {
        if (top == this.stackSize-1)
            System.out.println("Stack is full!");
        else {
            stackArr[++top] = item;
        }
    }

    public char pop() {
        if (top == -1) {
            System.out.println("Stack is empty!");
            return 0;
        }
        else 
            return stackArr[top--];
    }

    public char peek() {
        if (top == -1)
            return 0;
        else
            return stackArr[top];
    }

    public void clear() {
        if (top == -1)
            System.out.println("Stack is empty")!
        else {
            top = -1;
            stackArr = new char[this.stackSize];
        }
    }
}