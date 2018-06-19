/*
* Steven June 19 2018
* https://www.spoj.com/problems/ELEVTRBL/
* BFS
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int bfs(int floors, int start, int goal, int up, int down)
{
  if (start == goal)
  {
    return 0;
  }
  vector<int> path(floors, -1);
  queue<int> q;

  path[start] = 0;
  q.push(start);

  // Run BFS
  while (q.size())
  {
    int u = q.front();
    q.pop();

    // There are 2 options to either go up or down. Served as edges
    vector<int> options;
    options.push_back(u + up);
    options.push_back(u - down);

    int size = options.size();
    for (int i = 0; i < size; i++)
    {
      int v = options[i];

      // Return once we found it
      if (options[i] == goal)
      {
        return path[u] + 1;
      }

      // Else just keep track of the current times it takes
      if (v >= 0 && v < floors && path[v] == -1)
      {
        q.push(v);
        path[v] = path[u] + 1;
      }
    }
  };
  return -1;
}

int main()
{
  int floors = 0;
  int start = 0;
  int goal = 0;
  int up = 0;
  int down = 0;
  cin >> floors >> start >> goal >> up >> down;

  // Minus one to go to base 0
  int result = bfs(floors, start - 1, goal - 1, up, down);

  if (result == -1)
  {
    cout << "use the stairs";
  }
  else
  {
    cout << result;
  }
}
