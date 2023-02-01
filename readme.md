# Tab & Space 一种离奇的编译型,强类型语言

​		**Tab & Space** 是一款只使用'\t', ' ' 和 '\n' 进行编程的语言。采用 *JScript.NET* 语法，编译器器为使用 *python* 调用 *jsc* 编译器进行实现。

### 语法

​		在 **Tab & Space** 中，‘ ’ *(空格)* 代表二进制0，'\t' *(Tab)* 代表二进制1，'\n' *(回车)* 代表一个字符的结束。字符使用ASCII码表示，转换为二进制值，可省略开头的0。

##### 示例

​		原字符串

```python
't&s'
```

​		各个字符的二进制值 (tas编译器也支持该格式的代码)

```
100111
1110100
100110
1110011
100111
```

​		 **tas** 代码

```
	  			
			 	  
	  		 
			  		
	  			
```

​		*对，这里真的存在由 tab 和 space 所构成的代码。*

​		代码的语句使用 *JScript.NET* 语法，可以以 *JScript.NET* 语法编写代码，之后翻译为 tas 代码。可以在 *./sample/* 目录下找到示例的 tas代码与与其等效的  *JScript.NET* 代码。代码文件后缀建议为 **\*.tas** 可以使用tas编译器将脚本文件编译为可执行文件 (*.exe)

​		*(注:若想要使用汉字或其他特殊字符,可在python中使用ord()函数查询字符的值)*

### 编译

```
usage: tas [-h] [--code CODE] [--out OUT] [-t T] [--platform PLATFORM] [--lib LIB] [-r R] [--res RES]
           [--win32res WIN32RES] [--linkres LINKRES] [--debug] [--fast] [--warnaserror] [--print] [--utf8output]

optional arguments:
  -h, --help           show this help message and exit
  --code CODE          代码文件
  --out OUT            指定二进制输出文件的名称
  -t T                 创建控制台应用程序: exe(默认),winexe,library
  --platform PLATFORM  限制可以运行此代码的平台；必须是 x86、Itanium、x64 或 Any CPU(默认平台)
  --lib LIB            指定要在其中搜索引用的附加目录
  -r R                 从指定的程序集文件引用元数据 <file list>: <assembly name>[;<assembly name>...]
  --res RES            嵌入指定的资源 <info>: <filename>[,<name>[,public|private]]
  --win32res WIN32RES  指定 Win32 资源文件(.res)
  --linkres LINKRES    将指定的资源链接到此程序集 <info>: <filename>[,<name>[,public|private]]
  --debug              发出调试信息
  --fast               禁用语言功能以使代码更好地生成
  --warnaserror        将警告视为错误
  --print              提供 print() 函数
  --utf8output         以 UTF-8 字符编码形式发出编译器输出
```

​		使用编译器可以将 tas 脚本进行编译，生成的可执行文件与 tas 脚本同目录。--code 是必须参数，其余的按需求填写即可。
