import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();

        String[][] board = new String[n][m];
        for(int i = 0; i < n; i++){
            String s = sc.nextLine();
            board[i]= s.split("");
        }

        int L;
        if(n<m) L=n;
        else L=m;

        while(L>1){
            // n-L
            // m-L
            boolean square = false;
            for(int i=0;i<=n-L;i++){
                for(int j=0;j<=m-L;j++){
                    String a=board[i][j];
                    String b=board[i][j+L-1];
                    String c=board[i+L-1][j];
                    String d=board[i+L-1][j+L-1];
                    if(a.equals(b) && a.equals(c) && a.equals(d)){
                        square=true;
                        break;
                    }
                }
            }
            if(square) break;
            L--;
        }

        System.out.println(L*L);
    }
}