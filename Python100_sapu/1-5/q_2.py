'''
int型の100を文字列型に型変換してxに代入、
文字列型の"100.1"をfloat型に型変換してyに代入、
float型の100.0をint型に型変換してzに代入、
それぞれの値と型をprint関数を使って出力してください。
'''


x = str(100)
y = float('100.1')
z = int(100.0)

print(x, type(x))
print(y, type(y))
print(z, type(z))