from src.functions import interest_over_time


import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--search_term', type=str, help='Term to be searched for')
args = parser.parse_args()
'''parser.add_argument('--start_time', type=str, help='Start time')
parser.add_argument('--end_time', type=str, help='End time')
parser.add_argument('--export_target', type=str, help='Export results to')




df = interest_over_time(
    search_term=args.search_term,
    start_time=args.start_time,
    end_time=args.end_time
    )

df.to_csv(path_or_buf=args.export_target)
'''

print(args.search_term)
