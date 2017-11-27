from fund_list import get_fund_list

def update_list():
    fund_list = get_fund_list()
    print(fund_list)

def main():
    update_list()

main()