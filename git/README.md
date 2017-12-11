# git 사용 팁

  ## git을 사용할 때 생기는 문제점들



### 1. git 가장 기초적인 사용법
###   1.1 id connect
    >git config --global user.mail "honghong@hongmail.com"
    >git config --global user.name "hong hohong"

### 1.2 git clone
#### git clone 을 통해 local 저장소(컴퓨터)에 git repository를 복제.
#### 복제한 이후 로컬에서 작업한 결과물을 git에 commit할 수 있음
    >git clone repository_name


### 1.3 add, commit, push
#### 내가 코드를 이렇게 저렇게 바꾸고 git에 업데이트 하고 싶을 때 사용
#### 변경한 작업을 add 하고 commit하여 변경하고 push를 통해 git 서버(일듯)에 전송
    >git add my_work
    >git commit -m "commit message(암고나)"
    >git push
    
