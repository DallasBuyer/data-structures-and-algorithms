---
title: 机器学习算法岗笔试题整理
time: 2019.07.01
---
---
## **算法和数据结构**：

### 1.霍夫曼树相关知识

- 构建霍夫曼树，求树的深度 $(0.05, 0.29, 0.07, 0.08, 0.14, 0.23, 0.03, 0.11)$: 每次从序列中找两个最小的元素形成一个根节点，然后在序列中去掉两个叶节点，加入这个根节点，根节点的值就是两个叶节点的和。循环上述过程。

- 霍夫曼树的带权路径长度：用每个叶节点的值乘以其路径长度，这里路径长度为此叶节点到根节点的深度。然后将所有叶节点的带权路径长度加起来即为这棵霍夫曼树的带权路径长度。

### 2. 哈希表的平均查找长度

- 开地址法的平均查找长度
- 链地址法的平均查找长度

### 3. 后缀表达式(栈的应用)

- 定义：一个式子默认的形式就叫做它的中缀表达式也是我们最为熟悉的表达式，它对应于二叉树的中序遍历顺序。但是中缀表达式并不能高效地表达所有运算方式。其实还有前缀表达式(波兰式)，其所有运算符都在运算对象之前，它对应于二叉树的前序遍历。后缀表达式(逆波兰式)所有运算对象都在运算对象之后，它对应于二叉树的后序遍历。前缀表达式和后缀表达式不需要引进任何括号或者运算优先级规则，就可以以自然的方式描述任何复杂的表达式的计算顺序。中缀表达式加括号后，几种表达式具有同等的表达能力。
- 一种简单的中缀表达式转化法：给定一种中缀表达式 $a+b*c-(d+e)$,转化成前缀和后缀表达式。第一步：按照运算符的优先级对所有运算单位加括号，式子变成：$((a+(b*c))-(d+e))$。第二步：把运算符号移动到对应的括号前面，则变成 $-(+(a*(bc))+(de))$，去掉括号则形成前缀表达式 $-+a*bc+de$。第三步，把运算符号移动到对应的括号后面，则变成 $((a(bc)*)+(de)+)-$，去掉括号则形成后缀表达式 $abc*+de+-$
- 二叉树转化法：用中缀表达法自下向上按运算顺序构建二叉树，然后前序遍历该二叉树，就得到了前缀表达式，同理后续遍历得到后缀表达式。

### 4. 给定一个序列，以第一个值为标记位置，求快排算法的第一趟排序结果 $(46, 79, 56, 38, 40, 84)$

- 熟练掌握快排的原理，谨记Partition函数的6个步骤，把最左面的索引设置为标记位，先从右面开始扫描，最后令左索引位置为标记值。
- 这道题的答案 $(40, 38, 46, 56, 79, 84)$

### 5. 二叉树的节点计算问题


### 6. 二叉排序树的最优时间复杂度和最坏时间复杂度



### 7. 非递归方法实现二叉树的各种遍历

### 8. 排序算法的各种情况下(最优和最差)时间和空间复杂度，算法是否稳定


---
## **操作系统和计算机组成原理**

### 1. 静态链接库和动态链接库的异同点

### 2. 进程，线程，协程


---
## **计算机网络**

### 1. TCP和UDP，TCP的三次握手


---
## **数据库**

### 使用MySQL
- 选择数据库: USE database_name;
- 显示所有数据库: SHOW DATABASES;
- 显示当前数据库所有表: SHOW TABLES;
- 显示指定数据库所有列: SHOW COLUMNS FROM table_name;

### 检索数据
- 从指定数据库检索单个列: SELECT col_name FROM table_name;
- 从指定数据库检索多个列: SELECT col_name1, col_name2 FROM table_name;
- 从指定数据库检索所有列: SELECT * FROM table_name;
- 检索列的不同行: SELECT DISTINCT col_name FROM table_name;
- 
- 限制返回行数：SELECT col_name FROM table_name LIMIT com_num;
- 限制返回行数及开始行(开始行0)：SELECT col_name FROM table_name LIMIT col_begin, col_num;
  
### 排序检索数据(默认升序)
- 按指定列排序检索: SELECT col_name1 FROM table_name ORDER BY col_name2;
- 按多个指定列排序检索: SELECT col_name1, col_name2 FROM table_name ORDER BY col_name3, col_name4;
- 指定排序方向: SELECT col_name1 FROM table_name ORDER BY col_name2 DESC;
- 混合排序: SELECT col_name1 FROM table_name ORDER BY col_name2 DESC, col_name3;
- 限制排序(严格按照此语法顺序): SELECT col_name1 FROM table_name ORDER BY col_name2 DESC LIMIT 1;

### 过滤数据
- 使用WHERE子句: SELECT col_name1 FROM table_name WHERE col_name2 = val;
- 使用WHERE操作符: SELECT col_name1 FROM table_name WHERE col_name2 <= val; (=,<>,!=,<,<=,>,>=)
- 使用WHERE范围: SELECT col_name1 FROM table_name WHERE col_name2 BETWEEN val1 and val2;
- 检索空值列: SELECT col_name1 FROM table_name WHERE col_name2 IS NULL;

### 数据过滤
- 组合WHERE子句(AND): SELECT col_name1 FROM table_name WHERE col_name2 = val1 AND col_name3 < val2;
- 组合WHERE子句(OR): SELECT col_name1 FROM table_name WHERE col_name2 = val1 OR col_name3 > val2;
- 组合WHERE子句(AND OR): SELECT col_name1 FROM table_name WHERE (col_name2 = val1 OR col_name3 < val2) AND col_name4 != val3;
- WHERE子句(IN): SELECT col_name1 FROM table_name WHERE col_name2 IN (val1, val2) ORDER BY col_name3;
- WHERE子句(NOT): SELECT col_name1 FROM table_name WHERE col_name2 NOT IN (val1, val2);

### 通配符过滤
- LIKE+%通配符(任意字符出现任意次数): SELECT col_name1 FROM table_name WHERE col_name2 LIKE 'Jet%'; (col_name2列以Jet开头的所有记录)
- LIKE+_通配符(只能匹配一个字符): SELECT col_name1 FROM table_name col_name2 LIKE '_ton_anvil'; 

### 正则表达式搜索
- 基本字符匹配REGEXP(包含即可不用完全匹配): SELECT col_name1 FROM table_name WHERE col_name2 REGEXP '1000';
- 进行OR匹配: SELECT col_name1 FROM table_name WHERE col_name2 REGEXP '1000|2000';
- 匹配几个字符之一[]: SELECT col_name1 FROM table_name WHERE col_name2 REGEXP '[123] Ton'; (表示匹配1 Ton,2 Ton, 3 Ton)
- 匹配范围-: SELECT col_name1 FROM table_name WHERE col_name2 REGEXP '[2-4] Ton'; (.匹配任意字符任意长度)
- 匹配特殊字符\\: SELECT col_name1 FROM table_name WHERE col_name2 REGEXP '\\.'; (这里\\相当于转义字符)
- 匹配多个实例: SELECT col_name1 FROM table_name WHERE col_name2 REGEXP '\\([0-9] sticks?\\)'; (?表示0个或1个匹配)
- 定位符: SELECT col_name1 FROM table_name WHERE col_name2 REGEXP '^[0-9\\.]'; (^表示文本的开始，$表示结束)

### 创建计算字段
- 拼接字段: SELECT Concat(col_name1, '(', 'col_name2', ')') FROM table_name;
- 使用别名: SELECT Concat(col_name1, '(', 'col_name2', ')') AS new_name FROM table_name;
- 执行算术计算: SELECT col_name1, col_name2, col_name1*col_name2 AS new_name FROM table_name;

### 使用数据处理函数
- 文本处理函数: SELECT col_name1, Upper(col_name1) AS new_name FROM table_name;
- 常用本文处理函数: Left(返回串左边的字符), Right(返回串右边的字符), Length(返回串长度), Locate(找出串的子串);
- 常用本文处理函数: Lower(将串转化为小写), LTrim(去掉串左边的空格), RTrim(去掉串右边的空格), Soundex(返回串的SOUNDEX值);
- 日期和时间处理函数: AddDate(), AddTime(), CurDate(), CurTime(), Date(), Day(), Hour(), Time(), Year(), DateDiff();
- 选择日期区间: SELECT col_name1 FROM table_name WHERE Date(col_time) BETWEEN '2005-09-01' AND '2005-09-30';
- 选择年月: SELECT col_name1 FROM table_name WHERE Year(col_time) = 2005 AND Month(col_time) = 9;
- 数值处理函数: Abs(), Cos(), Exp(), Mod(), Pi(), Rand(), Sin(), Sqrt(), Tan();

### 汇总函数
- 返回某列平均值: SELECT AVG(col_price) AS avg_price FROM table_name; (就返回一个单值)
- 返回某几列的平均值: SELECT AVG(col_price) AS avg_price FROM table_name WHERE col_name1 = 1003;
- 返回所有列的行数: SELECT COUNT(*) AS num_rows FROM table_name; (即使某行都是空值也算)
- 返回某列的行数: SELECT COUNT(col_name) AS num_rows FROM table_name; (这列中空值不算一行)
- 返回某列的最大值: SELECT MAX(col_price) AS max_price FROM table_name;
- 返回某列的最小值: SELECT MIN(col_price) AS min_price FROM table_name;
- 返回某列值的和: SELECT SUM(col_price*quantity) AS sum_price FROM table_name;



## **Python知识点**

### 1. Python的可变对象和不可变对象：

- Python的对象分为可变和不可变，主要的核心类型中，不可变对象有 **数字(number)**，**字符串(string)**，**元组(tuple)**；可变对象有 **列表(list)**，**字典(dict)**。对不可变类型的变量重新赋值，实际上是重新创建一个不可变类型的对象，并将原来的变量重新指向新创建的对象。**垃圾回收机制**：**如果没有其他变量引用原有对象的话（即引用计数为0），原有对象就会被回收**。
- 不可变对象：以 int 类型为例，实际上 i=5; i+=1 并不是真的在原有的 int 对象上 +1，而是重新创建一个 value 为 6 的 int 对象，i 引用自这个新的对象两个 i 的内存地址是不一样的。
- 但是 i=5，j=5，对于不可变类型int，无论创建多少个不可变类型，只要值相同，都指向同个内存地址。同样情况的还有比较短的字符串。对于其他类型则不同，以浮点类型为例，从代码运行结果可以看出它是个不可变类型：对i的值进行修改后，指向新的内存地址。这方面涉及Python内存管理机制，Python对int类型和较短的字符串进行了缓存，无论声明多少个值相同的变量，实际上都指向同个内存地址。
- 可变对象：以list为例。list在append之后，还是指向同个内存地址，因为list是可变类型，可以在原处修改。当存在多个值相同的可变类型变量 a=[1,2,3], b=[1,2,3] 时，它们的内存地址是不同的。也可通过 a=b 让它们指向同一个内存地址，这个时候需要注意，因为a、b指向同个内存地址，而a、b的类型都是list可变类型，**对a、b任意一个List进行修改，都会影响另外一个List的值**。

### 2. Python中的值传递和引用传递：
- Python中的变量是没有类型的，我们可以把它看做一个(*void)类型的指针，变量是可以指向任何对象的，而对象才是有类型的。 
- 值传递：被调函数的形式参数作为被调函数的局部变量处理，即在堆栈中开辟了内存空间以存放由主调函数放进来的实参的值，从而成为了实参的一个副本。值传递的特点是被调函数对形式参数的任何操作都是作为局部变量进行，不会影响主调函数的实参变量的值。*被调函数新开辟内存空间存放的是实参的副本值*。
- 引用传递：被调函数的形式参数虽然也作为局部变量在堆栈中开辟了内存空间，但是这时存放的是由主调函数放进来的实参变量的地址。被调函数对形参的任何操作都被处理成间接寻址，即通过堆栈中存放的地址访问主调函数中的实参变量。正因为如此，被调函数对形参做的任何操作都影响了主调函数中的实参变量。*被调函数新开辟内存空间存放的是实参的地址*
- **不可变对象作为函数参数，相当于C语言的值传递**。 
- **可变对象作为函数参数，相当于C语言的引用传递**。因列表是可变数据类型，作为参数传递实则是传递对列表的引用，修改更新列表值后引用依旧不变。

### 3. Python的线程和进程，全局解释锁：

 
### 4. Python中的运算符：
| 运算符 |         描述         | 运算符 |          描述          |
| :----: | :------------------: | :----: | :--------------------: |
|   &    |        按位与        |   //   |     整除 向下取整      |
|   I    |        按位或        |   **   |         幂a**b         |
|   ^    |       按位异或       |   !=   |         不等于         |
|   ~    |       按位取反       |   <>   |      不等于类似!=      |
|   <<   | 左移 高位丢弃低位补0 |   in   |       a in list        |
|   >>   | 右移 低位丢弃高位补0 | not in |     a not in list      |
|   /    |          除          |   is   | 两变量是否引用同一对象 |
|   %    |    取模 返回余数     | is not |    是否引用不同对象    |

### 5. 容器类collections：deque, Counter, OrderDict

### 6. List: 可变对象

|                     方法                     |                       描述                       |
| :------------------------------------------: | :----------------------------------------------: |
|            lists = [3, 5, 6, 'a']            |              初始化一个list用方括号              |
|               list.append(obj)               |                列表末尾添加新对象                |
|               list.extend(seq)               |                用seq序列扩展列表                 |
|               list.count(obj)                | 统计某元素在列表中出现次数，相当于哈希表或者字典 |
|               list.index(obj)                |        从列表中找出obj第一个匹配项的索引         |
|           list.insert(index, obj)            |              将obj插入某个位置index              |
|              list.pop(index=-1)              |           移除列表中某个元素并返回该值           |
| list.sort(cmp=None, key=None, reverse=False) |                       排序                       |
|                  list[a:b]                   |                  切片索引a到b-1                  |
|                   list[a:]                   |                 切片索引a到末尾                  |
|                   list[:b]                   |                切片索引开头到b-1                 |
|                   list[::]                   |                     全部索引                     |
|              cmp(list1, list2)               |                比较两个列表的元素                |
|                  min(list)                   |                   取列表最小值                   |
|                  max(list)                   |                   取列表最大值                   |

### 7. Tuple: 不可变对象

|                 方法                  |                          描述                          |
| :-----------------------------------: | :----------------------------------------------------: |
| aTuple = (123, 'abc', 4.56, [2, 5.5]) | 构建元组用的是圆括号，另外只有一个元素的时候需要加逗号 |
| aTuple[1:4], aTuple[:2], aTuple[3,1]  |           访问元组中的值和列表的切片操作一致           |
|           和字符,串数字一样           |        元组是不可更新的，必须再构造一个新的元组        |
|          删除一个元组的元素           |         是不可能的，就和数字56一样你无法删除5          |
|              aTuple * 2               |                重复一个元组，和列表一样                |
|       aTuple + ('free', 'easy')       |                连接两个元组，和列表一样                |
|             list(aTuple)              |                    将元组转化成列表                    |
|   str(), len(), max(), min(), cmp()   |                 这些方法和list一样使用                 |
|          aTuple[3][0] = 'a'           |        虽然元组不可变，但里面的可变元素是可变的        |
|  return (obj1,obj2) return obj1,obj2  |         这两个返回式等价，默认返回的是一个元组         |
|         4, 2 < 3, 5 --> False         |        所有多对象的，逗号分割的默认类型都是元组        |
|      ('xyz',)元组 ('xyz')字符串       |                     创建单元素元组                     |
|           tuple() 和 list()           |               元组和列表之间可以轻松转换               |



### 8. 拷贝Python对象，浅拷贝和深拷贝