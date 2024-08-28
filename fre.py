vowel = {'A', 'E', 'I', 'O', 'U'}
consonants = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}

st=[]
def minion_game(s):
    for i in s:
        if i in vowel:
            st.append(i)
            st.count(i)



s = input()
minion_game(s)