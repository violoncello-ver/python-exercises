'''
03-1111-2222という電話番号の文字列があります。
ハイフンを取り除いた電話番号を出力してください。
'''


tel_number = "03-1111-2222"
number_without_hyphen = tel_number.replace("-", "")
print(number_without_hyphen)