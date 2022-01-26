import pyspark
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("student analysis")
sc = SparkContext.getOrCreate(conf=conf)

text = sc.textFile("s3://varunetlproject/StudentData.csv")
headers = text.first()
rdd = text.filter(lambda x : x != headers)

#number of students
rdd1 = rdd.map(lambda x : (x.split(",")[4]))
rddDistinct = rdd1.distinct()
numberOfStudents = rddDistinct.count()
print("Number of Students is " + str(numberOfStudents))

#Total marks of female and Male students.
rdd1 = rdd.map(lambda x : (x.split(",")[1],int(x.split(",")[5])))
rdd2 = rdd1.reduceByKey(lambda x,y: x + y)
print("total marks by female and male")
rdd2.collect()

#Total number of students passed or failed.
rdd3 = rdd.map(lambda x : (x.split(",")))
passed = rdd3.filter(lambda x: int(x[5])>50).count()
failed = rdd3.filter(lambda x: int(x[5])<=50).count()
print("passed students and failed students:")
print(passed, failed)

#Total number of enrolments per course.
rdd4 = rdd3.map(lambda x: (x[3],1))
rdd5 = rdd4.reduceByKey(lambda x,y : x + y)
print("Total number of enrolments per course.")
results = rdd5.collect()
rdd5.saveAsTextFile("s3://varunetlproject/output")



