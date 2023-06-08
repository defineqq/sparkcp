import org.apache.spark.{SparkConf, SparkContext}

object WordCount {
  def main(args:Array[String]): Unit ={
    val conf=new SparkConf().setAppName("wordcount").setMaster("local[*]")
    val sc=new SparkContext(conf)
    System.setProperty("HADOOP_USER_NAME", "root")

    val lines=sc.textFile("hdfs://master-ubuntu:9000/wordcount/wordcount.txt")

    val flatmaprdd=lines.flatMap(line=>line.split(" "))
    val maprdd=flatmaprdd.map(word=>(word,1))
    val reducerdd=maprdd.reduceByKey{case(x,y)=>x+y}

    reducerdd.saveAsTextFile("hdfs://master-ubuntu:9000/wordcount/output")
  }
}
