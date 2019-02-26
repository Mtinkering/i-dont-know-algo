//  DP Solution
#include <vector>
using namespace std;
int imax = std::numeric_limits<int>::max();

class Solution
{
public:
  int numSquares(int n)
  {
    vector<int> arr;
    int i = 1;

    while (true)
    {
      int k = i * i;
      if (k <= n)
      {
        arr.push_back(k);
        i += 1;
      }
      else
      {
        break;
      }
    }

    vector<int> dp;
    for (int j = 0; j <= n + 1; j++)
    {
      dp.push_back(imax);
    }

    for (int k = 0; k < arr.size(); k++)
    {
      int key = arr[k];
      for (int i = 1; i <= n; i++)
      {
        if (i > key)
        {
          dp[i] = min(dp[i], 1 + dp[i - key]);
        }
        else if (i == key)
        {
          dp[i] = 1;
        }
      }
    }
    return dp[n];
  }
};

// //  BFS Solution
// #include <vector>
// #include <queue>
//     using namespace std;

// class Solution
// {
// public:
//   int numSquares(int n)
//   {
//     vector<int> keys;
//     int i = 1;

//     for (int i = 1; i * i <= n; ++i)
//     {
//       keys.push_back(i * i);
//     }

//     vector<int> visited;
//     for (int j = 0; j <= n + 1; j++)
//     {
//       visited.push_back(-1);
//     }

//     queue<int> q;
//     q.push(n);
//     visited[n] = 0;

//     while (!q.empty())
//     {
//       int u = q.front();
//       q.pop();

//       int size = keys.size();
//       for (int i = 0; i < size; i++)
//       {
//         int v = u - keys[i];
//         if (v >= 0 && visited[v] == -1)
//         {
//           visited[v] = visited[u] + 1;
//           q.push(v);
//         }
//       }
//     }
//     return visited[0];
//   }
// };