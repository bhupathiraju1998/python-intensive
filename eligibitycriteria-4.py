m = int(input())
p = int(input())
c = int(input())
m_plus_c = m + c 
m_plus_p = m + p
p_plus_c = p +  c 
m_plus_p_c = m+p+c 
if ((m>=60and p>=50 and c>=45) and m_plus_p_c >= 180) or (m_plus_p >= 120 or p_plus_c>=110):
    print("True")
else:
    print("False")