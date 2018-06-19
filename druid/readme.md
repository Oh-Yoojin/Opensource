# Druid 실전 가이드

## 1. 설치

### 1.1. Prerequisites
- #### Java 8 or higher
  ##### 자바 미설치시 참고

  ```
  > sudo add-apt-repository ppa:webupd8team/java
  > sudo apt-get update
  > sudo apt-get install oracle-java8-installer
  > sudo apt-get install oracle-java8-set-default
  ```
  ​
  ##### 설치 확인

  ```
  > java -version
  java version "1.8.0_171"
  > javac -version
  javac 1.8.0_171
  ```

- #### Unix-like OS
 ##### 설치 가능 OS
 ##### - Linux
 ##### - OS X
 ##### - windows는 지원하지 않음
 ##### - 본 과제 사용 시스템
 ```
 Distributor ID: Ubuntu
 Description:    Ubuntu 16.04.4 LTS
 Release:        16.04
 Codename:       xenial
 ```


- #### 8G of RAM
##### 64GB ram 사용

- #### 2 vCPUs
##### i7-4930K
- #### Dependency
##### Zookeeper
