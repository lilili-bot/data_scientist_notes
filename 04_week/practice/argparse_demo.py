""" import argparse
parser = argparse.ArgumentParser(description= '命令中传入一个数字')
parser.add_argument('integers', type=int, nargs='+', help = '传入数字')
args = parser.parse_args()
print(sum(args.integers)) """

""" import argparse
parser = argparse.ArgumentParser(description='name')
parser.add_argument('param2', type=str, help = 'first name')
parser.add_argument('param1', type=str, help = 'last name')
args = parser.parse_args()
# print name
print(args.param1+args.param2) """

# import argparse
# parser = argparse.ArgumentParser(description='whole name')
# parser.add_argument('--family', type = str, help = '姓氏')
# parser.add_argument('--name', type = str, help = '名字')
# args = parser.parse_args()

# print(args.family+args.name)

import argparse
parser = argparse.ArgumentParser(description='姓名')
parser.add_argument('--family', type = str, default = 'plitschka', help ='请输入姓氏')
parser.add_argument('--name', type=str, default = '', required= False, help='请输入名字')
args = parser.parse_args()
# print name
print(args.family+'_'+args.name)
