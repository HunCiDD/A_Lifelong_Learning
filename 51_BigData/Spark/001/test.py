from pyspark.conf import SparkConf
from pyspark.context import SparkContext


if __name__ == '__main__':
    conf = SparkConf().setMaster("local").setAppName("WordCount2")
    sc = SparkContext.getOrCreate(conf)
    files = ["0.txt", '1.txt', "2.txt"]
    list_rdd = []
    for file in files:
        r0 = sc.textFile(file).flatMap(lambda x: x.split())
        r1 = r0.map(lambda x: (x, file)).distinct()
        r2 = r0.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x+y)
        r3 = r1.join(r2)
        list_rdd.append(r3)

    r00 = list_rdd[0]
    for i in range(1, len(list_rdd)):
        r00 = r00.union(list_rdd[i])

    r01 = r00.groupByKey().sortByKey()
    rc = r01.collect()
    # z = [(x, tuple(map(list, y))) for x, y in sorted(list())]
    for result in rc:
        print(f"({result[0]}, {result[1].data})")

