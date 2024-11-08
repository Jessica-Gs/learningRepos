# Get the amount in pesos, soles, and reais
amountPesos = int(input('Enter the amount in pesos: '))
amountSoles = int(input('Enter the amount in soles: '))
amountReais = int(input('Enter the amount in reais: '))

# Set the exchange rate to USD for pesos, soles, and reais
exchangeRatePesos = 0.00025
exchangeRateSoles = 0.28
exchangeRateReais = 0.21

# Calculate the exchange rate and print each amount in USD and the total
pesosInUSD = amountPesos * exchangeRatePesos
print(f'Your money in pesos converted to USD: ${pesosInUSD:.2f}')
solesInUSD = amountSoles * exchangeRateSoles
print(f'Your money in soles converted to USD: ${solesInUSD:.2f}')
reaisInUSD = amountReais * exchangeRateReais
print(f'Your money in reais converted to USD: ${reaisInUSD:.2f}')
totalUSD = pesosInUSD + solesInUSD + reaisInUSD
print(f'The total amount of currency you have after conversion is: ${totalUSD:.2f}')
