from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy import Tron, Contract

# client = Tron()  # The default provicder, mainnet
client = Tron()

from tronpy.providers import HTTPProvider
# print(client.get_block())
# print(client.get_latest_block_number())
# print(client.get_latest_block_id())
print(client.get_account_balance(''))
print(client.get_account_asset_balance(''))

priv_key = PrivateKey(bytes.fromhex(""))

cntr = client.get_contract("")
print(dir(cntr.functions))  # prints list of contract functions
for f in cntr.functions:
    print(f) 

precision = cntr.functions.decimals()
print('Balance in yappolaCoins:{} YPC'.format(cntr.functions.balanceOf('')))
print('Balance:', cntr.functions.balanceOf('') / 10 ** precision)
print('TOTAL YPC IN EXISTINCE {}'.format(cntr.functions.totalSupply()))
# print('TOTAL YPC BOUGHT {}'.format(cntr.functions.total_yappolacoins_bought()))
# print('YPC PRICE {:12f}'.format(cntr.functions.equity_in_USD('')//cntr.functions.equity_in_yappolacoins('TBeDPd2zP3piD8zBXfRfXFwhBAHYcUVPgy')))




cntr = client.get_contract("")
print(dir(cntr.functions))  # prints list of contract functions
for f in cntr.functions:
    print(f) 

# print('User Investing: {} '.format(cntr.functions.invest('TBeDPd2zP3piD8zBXfRfXFwhBAHYcUVPgy')))

print('User Stats: {} '.format(cntr.functions.getUserStats('')))
print('percent rate: {:2f}%'.format(cntr.functions.getUserPercentRate(''))) 
print('Contract Balance Rate: {:2f}%'.format(cntr.functions.getContractBalanceRate())) 
print('Contract Balance: {}'.format(cntr.functions.getContractBalance()//1000000)) 
print('User TOTAL WithDrawn {:2f}'.format(cntr.functions.getUserTotalWithdrawn('')//1000000))
print('TOTAL WithDrawn {:2f}'.format(cntr.functions.totalWithdrawn()))
print('current half day {}'.format(cntr.functions.getCurrentHalfDay()))
print('current half day turnover {} \n\n\n\n'.format(cntr.functions.getCurrentHalfDayTurnover()))

# print('withdrawing: {}YPC'.format(cntr.functions.withdraw())) 


# client = Tron()  # The default provicder, mainnet
# client = Tron()

# from tronpy.providers import HTTPProvider
# # print(client.get_block())
# # print(client.get_latest_block_number())
# # print(client.get_latest_block_id()) 
# cntr = client.get_contract("")
# print(dir(cntr.functions))  # prints list of contract functions
# for f in cntr.functions:
#     print(f) 

print('User Investing: {} '.format(cntr.functions.invest('T')))

# print('User Stats: {} '.format(cntr.functions.getUserStats('')))
# print('percent rate: {:2f}%'.format(cntr.functions.getUserPercentRate(''))) 
# print('Contract Balance Rate: {:2f}%'.format(cntr.functions.getContractBalanceRate())) 
# print('Contract Balance: {}'.format(cntr.functions.getContractBalance()//1000000)) 
# print('User TOTAL WithDrawn {:2f}'.format(cntr.functions.getUserTotalWithdrawn('')//1000000))
# print('TOTAL WithDrawn {:2f}'.format(cntr.functions.totalWithdrawn()))
# print('current half day {}'.format(cntr.functions.getCurrentHalfDay()))
# print('current half day turnover {}'.format(cntr.functions.getCurrentHalfDayTurnover()))
# print('\n\n\n\n\n User Stats: {} '.format(cntr.functions.getUserStats('')))
# print('percent rate: {:2f}%'.format(cntr.functions.getUserPercentRate(''))) 
# print('Contract Balance Rate: {:2f}%'.format(cntr.functions.getContractBalanceRate())) 
# print('Contract Balance: {}'.format(cntr.functions.getContractBalance()//1000000)) 
# print('User TOTAL WithDrawn {:2f}'.format(cntr.functions.getUserTotalWithdrawn('')//1000000))
# print('TOTAL WithDrawn {:2f}'.format(cntr.functions.totalWithdrawn()))
# print('current half day {}'.format(cntr.functions.getCurrentHalfDay()))
# print('current half day turnover {}'.format(cntr.functions.getCurrentHalfDayTurnover()))
#  