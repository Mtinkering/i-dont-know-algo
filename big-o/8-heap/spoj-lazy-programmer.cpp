#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int t;

int main()
{
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  scanf("%d", &t);
  while (t--)
  {
    vector<vector<int, int, int> > projects;
    int n;
    int currentTime;
    double money;

    scanf("%d", &n);
    for(int i = 0; i < n; i++){
      int x, y, z; scanf("%d %d %d", &x, &y, &z);
      vector<int> project;
      project.push_back(x);
      project.push_back(y);
      project.push_back(z);
      projects.push_back(project);
    }

    // sort
    sort(projects.begin(), projects.end())
    for (int i=0; i< projects.size(); i++) {
      vector<int> project = projects[i];
      int timeNeeded = project[1];
      int deadline = project[2];
      currentTime += timeNeeded;

      if (currentTime <= deadline) continue;
      else {
        // How much time needed more
        int extraTime = currentTime - deadline
        int constant = contract[0]
        money += extraTime/constant

        // Increase time when deadline is higher and time needed is more than deadline
        // # Dont increase when deadline is not higher
        if (deadline <= currentTime - timeNeeded) {
          currentTime = currentTime - timeNeeded
        }
        else {
          currentTime = currentTime - timeNeeded + deadline
        }
      }
    }
  }
  return 0;
}



#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int t;
struct contract {
  int a, b, d;
  bool operator<(const contract& p) const {
    return a < p.a;
  }
};

int main()
{
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  scanf("%d", &t);
  while (t--)
  {
    vector<contract> projects;
    int n;
    int currentTime = 0;
    double money = 0;

    scanf("%d", &n);
    for(int i = 0; i < n; i++){
      int a, b, d; scanf("%d %d %d", &a, &b, &d);
      projects.push_back({a, b, d});
    }

    sort(projects.begin(), projects.end(), [] (const contract& a, const contract& b) {
      return a.d < b.d;
    });
    priority_queue<contract> pq;
    for (int i = 0; i < projects.size(); i++) {
      contract project = projects[i];
      int timeNeeded = project.b;
      int deadline = project.d;
      currentTime += timeNeeded;
      pq.push(project);
      
      // While 
      while (currentTime - deadline > 0) {
        contract top = pq.top();
        pq.pop();
        
        // If can still use this b
        if (currentTime - deadline < top.b) {
          money += 1.0 * (currentTime - deadline) / top.a;
          top.b -= (currentTime - deadline);
          currentTime -= (currentTime - deadline);
          pq.push(top);
        }
        // Else use everything, next time take the next one
        else {
          money += 1.0 * top.b / top.a;
          currentTime -= top.b;
        }
      }
    }
    printf("%.2f\n", money);
  }
  return 0;
}


# Same a:
# 10 100 50
# 20 100 50
# #1-> 2     5 + 5 = 10
# #2 -> 1   2.5 + 10 = 12.5
# => sort by ascending value of a
#
import sys


class Scanner:
  def __init__(self, istream):
    self.tokenizer = Scanner.__tokenizer__(istream)

  def __tokenizer__(istream):
    try:
      for line in istream:  # line = '2'
        for token in line.strip().split():
          yield token
    except EOFError:
      exit()

  def next(self):
    return self.tokenizer.__next__()


sc = Scanner(sys.stdin)

t = int(sc.next())

for _ in range(t):
  money = 0
  n = int(sc.next())
  contracts = []
  currentTime = 0
  for i in range(n):
    a = int(sc.next())
    b = int(sc.next())
    d = int(sc.next())

    contracts.append((a, b, d))

  contracts.sort(key=lambda x: (x[2], x[0], x[1]))
  print(contracts)
  for contract in contracts:
    timeNeeded = contract[1]
    deadline = contract[2]
    currentTime += timeNeeded

    if currentTime <= deadline:
      continue
    else:
      # How much time needed more
      extraTime = currentTime - deadline
      constant = contract[0]
      money += extraTime/constant

      # Increase time when deadline is higher and time needed is more than deadline
      # Dont increase when deadline is not higher
      if deadline <= currentTime - timeNeeded:
        currentTime = currentTime - timeNeeded
      else:
        currentTime = currentTime - timeNeeded + deadline
    print(money)
  print("%.2f" % money)
