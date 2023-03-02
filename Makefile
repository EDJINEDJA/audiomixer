initialize_git:
	@echo "initialization ..."
	git init
	touch ./log.txt

pipe_git:
	@echo "pipe between current folder and github repository setting"
	git add . 2>> log.txt
	git commit -m "My first commit" 2>> log.txt
	git remote add origin https://github.com/EDJINEDJA/audiomixer.git 2>> log.txt

push2git:
	@echo "pushing ..."
	git add . 2>> log.txt
	git commit -m "My first commit" 2>> log.txt
	git push -u origin master 2>> log.txt
	

install:
	@echo "installation" 2>> log.txt
	pip install -r requirements.txt 2>> log.txt

setup:initialize_git pipe_git