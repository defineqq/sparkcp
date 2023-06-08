import sys
from pyspark import SparkContext
from pyspark import SparkConf
"""
词频统计
"""
if __name__ == '__main__':
    if len(sys.argv) !=2 :
        print("统计wordcount <input>",file=sys.stderr)
        sys.exit(-1)

    conf = SparkConf().setMaster("local[2]").setAppName("spark03")
    sc = SparkContext(conf=conf)

    def printResult():
        counts = sc.textFile(sys.argv[1]).flatMap(lambda line:line.split("\t")).map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)
        output = counts.collect()

        for(word , count) in output:
            print("%s : %i" % (word,count))

    printResult()
    sc.stop()
