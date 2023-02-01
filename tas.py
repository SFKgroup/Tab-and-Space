import argparse
import os
import sys
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--code', type=str, default=None, help='代码文件')
parser.add_argument('--out', type=str, default=None, help='指定二进制输出文件的名称')
parser.add_argument('-t', type=str, default='exe', help='创建控制台应用程序: exe(默认),winexe,library')
parser.add_argument('--platform', type=str, default='anycpu', help='限制可以运行此代码的平台；必须是 x86、Itanium、x64 或 Any CPU(默认平台)')
parser.add_argument('--lib', type=str, default=None, help='指定要在其中搜索引用的附加目录')
parser.add_argument('-r', type=str, default=None, help='从指定的程序集文件引用元数据\n<file list>: <assembly name>[;<assembly name>...]')
parser.add_argument('--res', type=str, default=None, help='嵌入指定的资源\n<info>: <filename>[,<name>[,public|private]]')
parser.add_argument('--win32res', type=str, default=None, help='指定 Win32 资源文件(.res)')
parser.add_argument('--linkres', type=str, default=None, help='将指定的资源链接到此程序集\n<info>: <filename>[,<name>[,public|private]]')
parser.add_argument('--debug', action='store_true', help='发出调试信息')
parser.add_argument('--fast', action='store_true', help='禁用语言功能以使代码更好地生成')
parser.add_argument('--warnaserror', action='store_true', help='将警告视为错误')
parser.add_argument('--print', action='store_true', help='提供 print() 函数')
parser.add_argument('--utf8output', action='store_true', help='以 UTF-8 字符编码形式发出编译器输出')
opt = parser.parse_args()

if not opt.code:
    print('[404] 文件未找到,请使用 --code 参数指定代码文件.')
    sys.exit()
file_name = opt.code
if opt.out:out_path = os.path.splitext(opt.out)[0]+'.temp'
else:out_path = os.path.splitext(file_name)[0]+'.temp'

try:
    out = open(out_path,'w',encoding='utf-8')
    grand = open(file_name,'r',encoding='utf-8')
    for i in grand.readlines():
        data = i[:-1].replace(' ','0').replace('\t','1')
        data = chr(int(data,2))
        out.write(data)
    out.close()
    grand.close()
except:
    print('[503] 临时文件生成失败')
    sys.exit()

print('[200] 临时文件生成成功\n[200] 开始编译')

other = ''
if opt.lib        :other += '/lib:"'     + opt.lib      +'" '
if opt.r          :other += '/r:"'       + opt.r        +'" '
if opt.res        :other += '/res:"'     + opt.res      +'" '
if opt.win32res   :other += '/win32res:"'+ opt.win32res +'" '
if opt.linkres    :other += '/linkres:"' + opt.linkres  +'" '
if opt.debug      :other += '/debug '
if opt.fast       :other += '/fast '
if opt.warnaserror:other += '/warnaserror '
if opt.print      :other += '/print '
if opt.utf8output :other += '/utf8output '

p = subprocess.Popen('jsc.exe /nologo /t:'+opt.t+' /platform:'+opt.platform+' '+other+'"'+out_path+'"')
p.wait() 
os.remove(out_path)
os.rename('./'+os.path.split(out_path[:-4]+'exe')[-1],out_path[:-4]+'exe')

print('[200] '+out_path[:-4]+'exe 编译成功')