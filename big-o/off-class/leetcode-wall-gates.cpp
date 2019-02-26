
//  BFS Solution
#include <vector>
#include <queue>
using namespace std;

class Solution
{
public:
  void wallsAndGates(vector<vector<int>> &rooms)
  {

    int m = rooms.size();
    
    if (m == 0) {
      return;
    }
    int n = rooms[0].size();
    if (n == 0)
    {
      return;
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (rooms[i][j] == 0) {
          vector<vector<int>> visited;
          for (int k = 0; k < m; k++)
          {
            vector <int> visit;
            for (int l = 0; l < n; l++)
            {
              visit.push_back(false);
            }
            visited.push_back(visit);
          }

          visited[i][j] = true;
          queue<int> q;
          q.push();

          while (!q.empty())
          {
            int u = q.front();
            q.pop();

            vector<int> options;
            options.push_back(u[0] + 1);
            options.push_back(u - down);
            int size = options.size();
            for (int i = 0; i < size; i++)
            {
              int v = options[i];

              int size = keys.size();
              for (int i = 0; i < size; i++)
              {
                int v = u - keys[i];
                if (v >= 0 && visited[v] == -1)
                {
                  visited[v] = visited[u] + 1;
                  q.push(v);
                }
              }
          }
        }
      }
    }
      vector<int>
          keys;
      int i = 1;

      for (int i = 1; i * i <= n; ++i)
      {
        keys.push_back(i * i);
      }

      vector<int> visited;
      for (int j = 0; j <= n + 1; j++)
      {
        visited.push_back(-1);
      }

      queue<int> q;
      q.push(n);
      visited[n] = 0;

      while (!q.empty())
      {
        int u = q.front();
        q.pop();

        int size = keys.size();
        for (int i = 0; i < size; i++)
        {
          int v = u - keys[i];
          if (v >= 0 && visited[v] == -1)
          {
            visited[v] = visited[u] + 1;
            q.push(v);
          }
        }
      }
      return visited[0];
  }
};