# 1.char. varchar. nchar. nvarchar的区别
- var：前缀的为**变长**，不带前缀会自动补全以**空格**补全

- n: 前缀的表示Unicode字符，每个字符用两个字节表示，故当能确定只有英文字符时用char 或者varchar能节省空间

- 占有空间：var类型的空间是非var两倍，同时若字段为Null，var类型**不占存储**空间

## 总的来说varchar 和 nvarchar的使用率会高一点，除非需要固定字段长度不然不会考虑char

# 2. 主键长度不宜过长
主键长度过宽，导致表**聚集索引、非聚集索引**空间占用过大  
解释：
Primary Key 字段的长度尽量小，能用 small integer 就不要用 integer  
(如: 若确定此表的数据量不会超过  32000 条记录)。  
例如员工数据表，若能用员工编号当主键，就不要用身份证号码。  
否则会占用过多的 index 和硬盘空间 (数据量越多，爆增越快)，  
index 长度过长，也会影向查找、JOIN 时 index 的搜寻性能。

# 3. SQL的转换类型函数cast( )
    select *
    from table
    where nyear = '2017' and nmonth = '02'
    order by cast(nday as int)

