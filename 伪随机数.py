# 适用于mt_srand(seed)然后后面的mt_rand(这里有一个范围)

str1='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str2='spOkHn1QfZ'
str3 = str1[::-1]
length = len(str2)
res=''
for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            res+=str(j)+' '+str(j)+' '+'0'+' '+str(len(str1)-1)+' '
            break
print(res)

# 求出的结果在kali中输入./php_mt_seed 求得的res即可
# eg: ./php_mt_seed 18 18 0 61 15 15 0 61 50 50 0 61 10 10 0 61 43 43 0 61 13 13 0 61 27 27 0 61 52 52 0 61 5 5 0 61 61 61 0 61



# if(!isset($_SESSION['seed'])){
# $_SESSION['seed']=rand(0,999999999);
# }

# mt_srand($_SESSION['seed']);
# $str_long1 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
# $str='';
# $len1=20;
# for ( $i = 0; $i < $len1; $i++ ){
#     $str.=substr($str_long1, mt_rand(0, strlen($str_long1) - 1), 1);       
# }
# $str_show = substr($str, 0, 10);
# echo "<p id='p1'>".$str_show."</p>"; 