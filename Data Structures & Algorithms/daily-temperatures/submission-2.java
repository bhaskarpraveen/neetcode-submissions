class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> st = new Stack<>();
        int[] arr = new int[temperatures.length];
        for(int i=0;i<=temperatures.length-1;i++){
            if(st.isEmpty()){
                st.push(new int[]{temperatures[i],i});
                continue;
            }
            while(!st.isEmpty()&&temperatures[i]>st.peek()[0]){
                arr[st.peek()[1]] = i - st.peek()[1];
                st.pop();
            }
            st.push(new int[]{temperatures[i],i});
        }
        return arr;
    }
}
