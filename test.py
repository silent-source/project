print("success read!")
import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '--name',help='enter the test name')
parser.add_argument('--param',default='test param')
args = parser.parse_args()
print("args:",args)
for i in range(20):
    print(i)