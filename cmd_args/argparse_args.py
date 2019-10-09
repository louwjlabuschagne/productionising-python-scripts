import argparse
from datetime import date

parser = argparse.ArgumentParser(prog='Awesome Bananas', 
                                 description='My awesome program that is awesome')
parser.add_argument('-s', '--start_day', 
                    type=str,
                    help='Start day to use in the format 20191008',
                    required=True)
parser.add_argument('-e', '--end_day',
                    type=str,
                    help='End day to use in the format 20191008',
                    default=date.today().strftime('%Y%m%d'))
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='Make the program more talkative ')
args = parser.parse_args()
start_day = args.start_day
end_day = args.end_day
v = args.verbose

print('start_day: %s'%start_day)
print('end_day: %s'%end_day)
print('verbose: %r'%v)