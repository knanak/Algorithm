import os, sys


def check_argv():
  if len(sys.argv) == 3:
    return True
  else:
    print('실행파일명 password 7zfile')
    exit()


def crack():
  f = open(sys.argv[1], 'r')
  lines = f.read().splitlines()
  for line in lines:
    x = os.system('7z x {} -p{} -bsp0 -bso0 -bse0 -y'.format(
      sys.argv[2], line))
    if x == 0:
      print("pwd is : " + line)
      exit(1)
  print('not found')


if __name__ == '__main__':
  if check_argv() == True:
    crack()
