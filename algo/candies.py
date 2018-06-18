N = int(raw_input())

ratings = [int(raw_input()) for x in range(N)]

candies = [1]*N

for i in range(1,N):
	if(ratings[i] > ratings[i-1]):
		candies[i] = candies[i-1] + 1
# print candies
for i in range(N-2,-1,-1):
	if(ratings[i] > ratings[i+1]):
		candies[i] = max(candies[i], candies[i+1] +1)

# print candies
print sum(candies)