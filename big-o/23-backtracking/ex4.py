def main():
  s = input()

  while s != '#':
    m1 = []
    m2 = []
    letters = s.split()
    m1.append(letters[:4])
    m2.append(letters[4:8])


main()
