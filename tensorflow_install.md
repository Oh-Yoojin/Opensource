# Centos 7 Tensorflow-gpu 설치 순서

## 1. cuda install
### - cuda toolkit 8 & cudnn 5.1 설치
http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html


#### 지포스 그래픽카드가 있나 확인
```
> lspci | grep -i nvidia

```
#### 나는 있다 1080
```
04:00.0 VGA compatible controller: NVIDIA Corporation GP104 [GeForce GTX 1080] (rev a1)
04:00.1 Audio device: NVIDIA Corporation GP104 High Definition Audio Controller (rev a1)
```

#### 커널 확인
```
> uname -r
> sudo yum install kernel-devel-$(uname -r) kernel-headers-$(uname -r)
```

#### Satisfy DKMS dependency
```
> yum install epel-release
> yum install dkms
```
#### nvidia 사이트에서 cuda toolkit 8 (linux, rpm(local)) 다운받아 저장
```
> rpm -i cuda-your-version.rpm
> yum clean expire-cache
> yum install cuda
```

#### PATH 추가
```
export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
```

#### Cudnn 설치
##### nvidia 홈페이지에서 cudnn 다운로드
##### 압축 해제 후 파일들을 cuda 위치로 옮겨줄 것
```
> sudo cp cuda/include/cudnn.h /usr/local/cuda/include
> sudo cp cuda/lib64/cudnn* /usr/local/cuda/lib64
> sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
```

## 2. Install Tensorflow
https://www.tensorflow.org/install/install_linux

##### 가상환경 생성 후
```
> conda install tensorflow-gpu
```
##### 설치 이후 테스트
```
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```

## 3.원격으로 server에서 파이썬 사용
### 3-1. ipython notebook 사용하기
#### Ipython 사용할 포트 열어주기
##### in terminal

```
> jupyter notebook --generate-config

# 포트 오픈(본인이 오픈할 포트 입력)
> sudo firewall-cmd --zone=public --add-port=9200/tcp --permanent
> sudo firewall-cmd --reload
```


##### ipython 실행 후 코드 입력
```
from notebook.auth import passwd
passwd()
#password 입력
#결과값 저장
```
##### 설정하기
```
> vi /home/username/.jupyter/jupyter_notebook_config.py
```
##### 다음 값들을 변경해준다
```
> c.NotebookApp.ip = 아이피 주소
> c.NotebookApp.password = 아까 복사한 비밀번호 변환된 값
> c.NotebookApp.open_browser = False # 자동으로 웹브라우저가 켜질 필요 없음
```
##### 접속 가능
https://ip주소:포트넘버

### 3-2. SSH 연결
##### SSH는 터미널 작업을 하기 위해 필요
##### 포트 오픈 확인 이후 접속
##### windows는 putty 설치 후 사용
##### mac, linux는
```
> ssh -v name@ip -p port
```
### 3-3. Pycharm 연결
##### Pycharm으로 서버 컴퓨터를 사용해 코드 실행 가능
##### Pycharm CE로는 안됨, 학교 이메일 등을 사용해 등록해서 설치
