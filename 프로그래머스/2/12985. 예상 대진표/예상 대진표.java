class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 1;
        a-=1;
        b-=1;
        while(n!=2){
            if((a-b==1 && a/2==b/2) || (b-a==1 && b/2==a/2)) { break; }
            a/=2;
            b/=2;
            n/=2;
            answer+=1;
            
        }
        return answer;
    }
}