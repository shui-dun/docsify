#!/usr/bin/env python3

# Des: 用于生成md格式的文件树

import os
import sys
from urllib.parse import quote

class gen_sidebar:

    def __init__(self):
        self.base_path = '.'
        self.targe_file = '_sidebar.md'
        self.file_allow_ext = [".md"]
        self.file_disallow_start = ["_"]

        self.list_dir = []
        self.set_list_dir()
        self._gen_targe_file()


    def set_list_dir(self):
        
        for parent, dirnames, filenames in os.walk(self.base_path,  followlinks=False):
            for filename in filenames:
                if self._is_allow_file(filename) == False:
                    continue
                file_path = os.path.join(parent, filename)
                dirname = ""
                for _dirname in file_path.split("/"):
                    dirname = os.path.join(dirname, _dirname)
                    if dirname not in self.list_dir:
                        self.list_dir.append(dirname)

    
    def _is_allow_file(self, file):
        for _ext in self.file_disallow_start:
            if file.find(_ext) == 0:
                return False

        ext = os.path.splitext(file)[1]
        if ext in self.file_allow_ext:
            return True
        return False

    def _gen_targe_file(self):
        with open(self.targe_file, 'w', encoding='utf-8') as f:

            _str = []
            for _file in self.list_dir:
                if _file == ".":
                    continue           
                if not self._is_allow_file(_file):
                    _chengji = _file[len(self.base_path)+1:].split('/')
                    _name = _chengji[-1]
                    _url = "#"
                    _str.append("%s- [%s](%s)\n" % ( '    '*(len(_chengji)-1) , _name, _url ) )
                else:
                    _chengji = _file[len(self.base_path)+1:-3].split('/')
                    _name = _chengji[-1]
                    _url = quote(_file[len(self.base_path)+1:-3],'utf-8').replace('%2F', '/')
                    _str.append("%s- [%s](%s)\n" % ( '    '*(len(_chengji)-1) , _name, _url ) )
            
            f.writelines(_str)


if __name__ == "__main__":
    os.chdir(sys.path[0])
    gen_sidebar()