/*
* Steven Nguyen 14 June 2018.
*/
#include <iostream>
#include <vector>

using namespace std;
vector<int> graph;

int bfs(int floors, int start, int goal, int up, int down) {
  if (start == goal)
  {
    return 0;
  }
  vector<int> path;
  vector<int> levels;
  for (int i = 0; i < floors; i++) {
    path.push_back(-1);
    levels.push_back(-1);
  };

  int l = 0;
  int r = 0;
  path[start] = 0;
  levels[l] = start;

  while (l <= r) {
    int u = levels[l];
    vector<int> options;
    options.push_back(u + up);
    options.push_back(u - down);
    int size = options.size();
    for (int i = 0; i < size; i++)
    {
      int v = options[i];
      if (options[i] == goal)
      {
        return path[u] + 1;
      }
      if (v >= 0 && v < floors && path[v] == -1)
      {
        r += 1;
        levels[r] = v;
        path[v] = path[u] + 1;
      }
    }
    l += 1;
  };
  return -1;
}

int main() {
  int floors = 0;
  int start = 0;
  int goal = 0;
  int up = 0;
  int down = 0;
  cin >>floors>>start>>goal>>up>>down;
  
  int result = bfs(floors, start - 1, goal - 1, up, down);

  if (result == -1) {
    cout << "use the stairs";
  } else {
    cout << result;
  }
}
