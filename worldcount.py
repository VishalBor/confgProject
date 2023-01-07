from pyspark.sql import *
import os
import sys

from pyspark import SparkConf
from lib.utils import get_spark_app_config
os.environ['PYSPARK_PYTHON'] = sys.executable

conf01 = get_spark_app_config()



spark007 = SparkSession.builder.config(conf=conf01).getOrCreate()
dada = spark007.sparkContext.parallelize([1,2,2,4,5,6])
conf_out = spark007.sparkContext.getConf()
print(conf_out.toDebugString())
spark007.stop()