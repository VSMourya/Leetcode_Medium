

def isValid(S):
    st = []
    for i in S:
        if i == "c":
            if st[-2:] != ["a", "b"]:
                return False
            st.pop()
            st.pop()
        else:
            st.append(i)

    return not st


if __name__ == '__main__':
    S = "aabcbc"
    print(isValid(S))


