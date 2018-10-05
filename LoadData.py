

## csv파일 mysql 데이터베이스에 저장하기

import csv
import pymysql
import socket

#csv파일 읽어오기
data2018 = open('./csv_dir/lostAnimal_2018.csv','r')
csvReader = csv.reader(data2018)

#데이터베이스 연결


