import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ_1707 {
    static int[] visited;
    static ArrayList<Integer>[] adjacent;
    static int v;
    static boolean result;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            result = false;
            v = Integer.parseInt(st.nextToken());
            visited = new int[v + 1];
            adjacent = new ArrayList[v + 1];
            for (int j = 1; j <= v; j++) {
                adjacent[j] = new ArrayList<>();
            }
            int e = Integer.parseInt(st.nextToken());
            for (int j = 0; j < e; j++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                adjacent[a].add(b);
                adjacent[b].add(a);
            }
            for (int j = 1; j <= v; j++) {
                if (visited[j] == 0) {
                    dfs(j, 1);
                }
            }
            if (result) System.out.println("NO");
            else System.out.println("YES");
        }
    }

    static void dfs(int j, int col) {
        visited[j] = col;
        if (result) return;
        for (Integer i : adjacent[j]) {
            if (visited[i] == visited[j]) {
                result = true;
                return;
            }
            if (visited[i] == 0) dfs(i, col * -1);
        }
    }
}