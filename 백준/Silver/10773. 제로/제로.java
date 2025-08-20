import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        Stack<Integer> stack = new Stack<>();
        for(int i=0;i<n;i++){
            int x = sc.nextInt();
            if(x==0){
                stack.pop();
            }
            else{
                stack.push(x);
            }
        }

        int sum = 0;
        while(!stack.isEmpty()){
            sum+=stack.pop();
        }
        System.out.println(sum);
    }
}
