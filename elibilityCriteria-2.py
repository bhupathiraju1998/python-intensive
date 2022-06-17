m = int(input())
p = int(input())
c = int(input())
m_plus_c = m + c 
m_plus_p = m + p
p_plus_c = p +  c 
m_plus_p_c = m+p+c 
if (m_plus_p or m_plus_c or p_plus_c >= 100) and m_plus_p_c >= 180:
    print("True")
else:
    print("False")