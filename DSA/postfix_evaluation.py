l=input()
st = []
for token in l:
    if token.isdigit():
        st.append(int(token))
    else:
        x2 = st.pop()
        x1 = st.pop()
        if token == "+":
            st.append(x1+x2)
        elif token == "*":
            st.append(x1*x2)
        elif token == "-":
            st.append(x1-x2)
        else:
            st.append(x1//x2)
print(st.pop())
'''
INPUT :
231*+9-

OUTPUT :
-4
'''


