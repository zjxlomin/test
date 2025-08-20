import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        List<Integer> list = new ArrayList<>();
        for(int i=0;i<n;i++){
            int x = sc.nextInt();
            list.add(x);
            sc.nextLine();
        }

        Collections.sort(list);
        Iterator<Integer> iterator  = list.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }
    }
}