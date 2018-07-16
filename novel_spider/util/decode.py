'''
Created on 2018年7月16日

@author: Loong
'''
from idna.core import unicode
import chardet
def decode(src):
    src_charset = chardet.detect(src)
    charset = get_charset(src_charset)
    decode_src= unicode(src, encoding=charset)
    return decode_src

def get_charset(src_charset):
    src_charset['encoding']="gb18030"
    return src_charset['encoding']