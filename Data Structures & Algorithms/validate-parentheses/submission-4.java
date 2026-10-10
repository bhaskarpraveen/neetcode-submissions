class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        if (s.length()%2!=0) return false;
        HashMap<Character,Character> hm = new HashMap<Character,Character>();
        hm.put('[',']');
        hm.put('{','}');
        hm.put('(',')');
        boolean flag = true;
        for(char c:s.toCharArray()){
            if(!hm.containsKey(c)){
                if(st.isEmpty()) return false;
                if(hm.get(st.pop())==c){
                    continue;
                }else{
                    flag = false;
                    break;
                }
            }else{
                st.push(c);
            }
        }
        return flag && st.isEmpty();
    }
}
