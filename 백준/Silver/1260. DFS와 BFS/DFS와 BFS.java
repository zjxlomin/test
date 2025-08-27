import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int v =  sc.nextInt();
        sc.nextLine();

        // 인접 리스트
        List<List> adj = new LinkedList<>();
        for(int i=0;i<n;i++){
            adj.add(i, new LinkedList<>());
        }

        for(int i=0;i<m;i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            adj.get(a-1).add(b);
            adj.get(b-1).add(a);
        }

        List<Integer> bfs = new LinkedList<>();
        List<Integer> dfs = new LinkedList<>();

        // BFS
        for(int i=0;i<n;i++){
            Collections.sort(adj.get(i));
        }

        boolean[] visited = new boolean[n];
        Arrays.fill(visited, false);
        Queue<Integer> deq = new LinkedList<>();
        deq.offer(v);
        visited[v-1] = true;
        bfs.add(v);
        while(!deq.isEmpty()){
            int u=deq.poll();
            for(Object o: adj.get(u-1)){
                int k=(Integer)o;
                if(!visited[k-1]){
                    deq.offer(k);
                    visited[k-1]=true;
                    bfs.add(k);
                }
            }
        }

        // DFS
        for(int i=0;i<n;i++){
            Collections.sort(adj.get(i), Collections.reverseOrder());
        }

        Arrays.fill(visited, false);
        Stack<Integer> stack = new Stack<>();
        stack.push(v);
        while(!stack.isEmpty()){
            int u = stack.pop();
            if(!visited[u-1]){
                visited[u-1]=true;
                dfs.add(u);
            }
            for(Object o: adj.get(u-1)){
                int k =  (Integer)o;
                if(!visited[k-1]){
                    stack.push(k);
                }
            }
        }

        for(int i=0;i<dfs.size();i++){
            System.out.print(dfs.get(i)+" ");
        }
        System.out.println();
        for(int i=0;i<bfs.size();i++){
            System.out.print(bfs.get(i)+" ");
        }
    }
}