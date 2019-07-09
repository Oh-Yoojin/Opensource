## Cassandra 가이드

### 1. Install Cassandra
#### 1.1. Linux single 설치
* http://cassandra.apache.org/download/URL 에서 다운로드
```
> wget http://apache.mirror.cdnetworks.com/cassandra/3.11.4/apache-cassandra-3.11.4-bin.tar.gz
```

* 압축 풀기
```
> tar -xvf apache-cassandra-3.11.4-bin.tar.gz
```

### 2. Start cassandra
#### 2.1. 실행

```
> apache-cassandra-3.10/bin/Cassandra
```

#### 2.2. CQLSH 실행
* In cassandra derectory(~/apache-cassandra-3.10)
```
> bin/CQLSH
```
이후 CQLSH 이용한 cassandra 사용 가능
