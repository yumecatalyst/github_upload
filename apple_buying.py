apple_price = 200

input_money = input('投入する金額を入力してください：')
input_count = input('購入するりんごの個数を入力してください：')
money = int(input_money)
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払金額は' + str(total_price) + '円です')

if money > total_price:
    print('りんごを' + str(count) + '個買いました')
    print('残金は' + str(money - total_price) + '円です')

elif money == total_price:
    print('りんごを' + str(count) + '個買いました')
    print('財布が空になりました')

else:
    print('お金があと' + str(total_price - money) + '円足りません')
    print('もう一度金額を確認して入れ直してください')
