class MinStack {
    Stack <Integer> st;
    Stack <Integer> min_stack;

    public MinStack() { 
        st = new Stack<>();
        min_stack = new Stack<>();
    }
    
    public void push(int val) {
        st.push(val);
        if(min_stack.isEmpty()||val<=min_stack.peek()){
            min_stack.push(val);
        }
        
    }
    
    public void pop() {
        if(st.isEmpty()) return;
        int top = st.pop();
        if (top == min_stack.peek()) {
            min_stack.pop();
        }
    }
    
    public int top() {
        return st.peek();
    }
    
    public int getMin() {
        return min_stack.peek();
    }
}
