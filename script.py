# Allows user to enter cost and sale price
cost_price = float(input('Enter cost price: '))
sale_price = float(input('Enter sale price: '))

# Calculates profit and profit percentage
if cost_price < sale_price:
    profit = sale_price - cost_price
    profit_percentage = ((sale_price - cost_price) / cost_price) * 100
    print(f'Your profit is: {profit}')
    print(f'Which is %{int(profit_percentage)}')

# Calculates loss and loss percentage
elif sale_price < cost_price:
    loss = cost_price - sale_price
    loss_percentage = ((cost_price - sale_price) / cost_price) * 100
    print(f'Your loss is: {loss}')
    print(f'Which is %{int(loss_percentage)}')

# If the user has no profit and no loss, they broke even
else:
    print('You broke even')
