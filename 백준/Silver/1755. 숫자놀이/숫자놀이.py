def ntos(num):
    num = num.replace('0', 'zero')
    num = num.replace('1', 'one')
    num = num.replace('2', 'two')
    num = num.replace('3', 'three')
    num = num.replace('4', 'four')
    num = num.replace('5', 'five')
    num = num.replace('6', 'six')
    num = num.replace('7', 'seven')
    num = num.replace('8', 'eight')
    num = num.replace('9', 'nine')
    return num


def ston(st):
    st = st.replace('zero', '0')
    st = st.replace('one', '1')
    st = st.replace('two', '2')
    st = st.replace('three', '3')
    st = st.replace('four', '4')
    st = st.replace('five', '5')
    st = st.replace('six', '6')
    st = st.replace('seven', '7')
    st = st.replace('eight', '8')
    st = st.replace('nine', '9')
    return int(st)


n, m = map(int, input().split())
n_list = list(range(n, m + 1))
l = m - n + 1
for i in range(0, l):
    num = str(n_list[i])
    n_list[i] = ntos(num)
n_list = sorted(n_list)
for j in range(0, l):
    st = n_list[j]
    n_list[j] = ston(st)
for k in range(0, l):
    if (k % 10 == 9):
        print(n_list[k])
    else:
        print(n_list[k], end=' ')