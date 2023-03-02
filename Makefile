initialize_git:
	@echo "initialization ..."
	git init

pipe_git:
	@echo "pipe between current folder and github repository setting"
	git add .
	git commit -m "My first commit"
	git remote add origin https://github.com/EDJINEDJA/audiomixer.git

push2git:
	@echo "pushing ..."
	git add .
	git commit -m "My first commit"
	git push -u origin master
	
install:
	@echo "installation"
	pip install -r requirements.txt

setup:initialize_git pipe_git