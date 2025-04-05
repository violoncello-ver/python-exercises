'''
変数xに10、変数yに2を代入し、
「xかけるyの結果」と「x割るyの結果」の合計を出力してください。
また、「xのy乗」から「xをyで割った余り」を引いた数を出力してください。
'''


x = 10
y = 2

result_1 = (x * y) + (x / y)
result_2 = (x ** y) - (x % y)

print(result_1)
print(result_2)