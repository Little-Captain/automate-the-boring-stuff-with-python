# 如果需要在一个函数内修改全局变量，就使用 global 语句
# `global 变量名`表示`'变量名'指的是全局变量, 所以不要用这个名字创建一个局部变量`

# 有 4 条法则, 区分一个变量是处于局部作用域还是全局作用域
# 1．如果变量在全局作用域中使用(即在所有函数之外), 它就总是全局变量
# 2．如果在一个函数中, 有针对该变量的 global 语句, 它就是全局变量
# 3．否则, 如果该变量用于函数中的赋值语句, 它就是局部变量
# 4．但是, 如果该变量没有用在赋值语句中, 它就是全局变量

# 在一个函数中, 如果试图在局部变量赋值之前就使用它,
# Python 就会报错(local variable 'xxx' referenced before assignment)

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)