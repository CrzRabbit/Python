'''
        Format Characters
x	pad         byte	        no value
c	char	    bytes of length 1	1
b	signed      char integer	1	(1),(3)
B	unsigned    char integer	1	(3)
?	_Bool	    bool	        1	(1)
h	short	    integer	        2	(3)
H	unsigned    short integer	2	(3)
i	int	        integer	        4	(3)
I	unsigned    int	integer	    4	(3)
l	long	    integer	        4	(3)
L	unsigned    long integer	4	(3)
q	long long	integer	        8	(2), (3)
Q	unsigned    l l integer     8	(2), (3)
n	ssize_t	    integer	 	        (4)
N	size_t	    integer	 	        (4)
e	(7)	        float	        2	(5)
f	float	    float	        4	(5)
d	double	    float	        8	(5)
s	char[]	    bytes
p	char[]	    bytes
P	void *	    integer	 	        (6)
>   big-endian
<   small_endian
'''
import struct
from collections import OrderedDict
#获取位图的参数
l = ['位图类型', '位图大小', '保留位', '实际偏移', 'Header字节数', '宽', '高', '保留', '色彩位数']

f = open('1.bmp', 'br')
str = f.read(30)
t = struct.unpack('<ccIIIIIIHH', str)
d = OrderedDict()
d[l[0]] = '{0}{1}'.format(t[0], t[1])
for i in range(1, 9):
    d[l[i]] = t[i + 1]
print(d)