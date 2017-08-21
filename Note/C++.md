# 1. sort的compare()的注意点
在对浮点或者double型的一定要用三目运算符。  
因为如果也使用整型那样的想减的话，如果是两个很接近的数则可能返回一个小数（大于-1，小于1），而cmp的返回值是int型，因此会将这个小数返回0，系统认为是相等，失去了本来存在的大小关系。  

For int:
```

int cmp ( const void *a , const void *b )
{
    return *(int *)a - *(int *)b;
}
```
For double (三目运算符)
```
int cmp( const void *a , const void *b )
{
    return *(double *)a > *(double *)b ? 1 : -1;
}
```
# 2. 返回数组中最大/最小元素 max_element()
```
int a[5] = {0, 3, 9, 4, 5};  
int *b;   
b = max_element(a, a+5);  
cout << *b;  
```
# 3. 字符串转换为大/小写
    transform(str1.begin(), str1.end(), str1.begin(), ::toupper);
    transform(str1.begin(), str1.end(), str1.begin(), ::tolower);
# 4 . 字符串中删除重复字符
    str1.erase(remove(str1.begin(), str1.end(), str2[i]), str1.end());
# 5. 生成二维数组
```
int row,col;
cin >> row >> col;
int ** a = new int *[row];
for (int i = 0; i < row; i++)
    a[i] = new int[col];
```
# 6. 格式控制
保留小数 
``` 
cout<<setiosflags(ios::fixed)<<setprecision(2);
```
整数补0
```
cout<<setfill(‘0’)<<setw(4)<<n;
```
# 7. STL库中的正则表达式
	class Solution {
	public:
	    bool isMatch(string s, string p) {
	        return regex_match(s, regex(p));
	    }
	};
# 8. abs()函数时需要注意溢出问题
    INT32_MIN -2147483647-1
    INT32_MAX  2147483647
abs(INT32_MIN)时会产生溢出(二进制转换)
以下两种没有溢出
```
    long long int b = INT32_MIN;
    long long int d = abs(b);	
```
```
    int b = INT32_MIN;
    unsigned int d = abs(b);
```
# 9. 反转数字的简单实现（以前用的是字符串）
    int reverse(int x)
    {
        long long res = 0;
        while(x) {
            res = res*10 + x%10;
            x /= 10;
        }
        return  res;
    }
# 10. 搜索子串
- find( ) 搜索特定字串的第一次出现

- rfind( ) 从尾部开始查第一次出现
- find_first_of( ) 搜索字符的第一次出现
- find_last_of( ) 搜索字符的最后一次出现 
# 11. vector 边界/范围函数
相等
```
//STL库函数之equal_range
vector<int> searchRange(vector<int>& nums, int target) {
    auto bounds = equal_range(nums.begin(), nums.end(), target);
    if (bounds.first == bounds.second)
        return {-1, -1};
    return {bounds.first - nums.begin(), bounds.second - nums.begin() - 1};
}
```
大于/小于
```
//STL库函数之lower_bound , upper_bound
vector<int> searchRange(vector<int>& nums, int target) {
    int lo = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    if (lo == nums.size() || nums[lo] != target)
        return {-1, -1};
    int hi = upper_bound(nums.begin(), nums.end(), target) - nums.begin() - 1;
    return {lo, hi};
}
```
# 12. 浮点数的一些事
==运算：由于浮点数无法精确表示在使用==运算符时很容易报错，所以最好采取减法的方式  
原因：因为当0.1转换成二进制数时会产生无限循环小数导致0.1*1000的值是99.9999046。
```
if(abs(a-b) < 0.00000000001)
    //do
```
四舍五入：浮点数在限制精度后会自动四舍五入
