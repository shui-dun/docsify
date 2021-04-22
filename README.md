# docsify

使用docsify将markdown实时转化为页面

* index.html
	* 支持katex
	* 支持侧边栏
	* 支持侧边栏折叠
	* 支持搜索
* gen-sidebar.py
	
	生成侧标栏
	
* gen-sidebar-win.py
	
	windows下生成侧边栏（linux路径与win不同）
	
* git hooks

	```shell
	#!/bin/bash
	
	git --work-tree=/srv/docsify/notebook --git-dir=/srv/docsify/notebook.git checkout -f 
	python3 /srv/docsify/notebook/gen-sidebar.py

	```