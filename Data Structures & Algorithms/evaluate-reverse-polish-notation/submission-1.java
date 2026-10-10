class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> st = new Stack<>();
        for(String s:tokens){
            if(s.equals("+")||s.equals("-")||s.equals("*")||s.equals("/")){
                if(s.isEmpty()){
                    return 0;
                }else{
                    if(s.equals("+")){
                        int top = Integer.parseInt(st.pop());
                        int next = Integer.parseInt(st.pop());
                        st.push(String.valueOf(top+next));
                    }else if(s.equals("-")){
                        int top = Integer.parseInt(st.pop());
                        int next = Integer.parseInt(st.pop());
                        st.push(String.valueOf(next-top));
                    }else if(s.equals("/")){
                        int top = Integer.parseInt(st.pop());
                        int next = Integer.parseInt(st.pop());
                        st.push(String.valueOf(next/top));
                    }else{
                        int top = Integer.parseInt(st.pop());
                        int next = Integer.parseInt(st.pop());
                        st.push(String.valueOf(top*next));
                    }
                }
            }else{
                st.push(s);
            }
        }
        return Integer.parseInt(st.peek());
    }
}
