from pyspark.sql import SparkSession

#spark session to read file and manipulate it we create spark session
#builder specify the master which need server for spark which is local for us.
# java_home = "ssh k17hawk@localhost"
# spark_session = (SparkSession.builder
#     .master('local[*]')
#     .appName('finance_complaint')
#     .config('spark.executor.instances', '1')
#     .config('spark.executor.memory', '6g')
#     .config('spark.driver.memory', '6g')
#     .config('spark.executor.memoryOverhead', '6g')
#     .config('spark.driver.extraJavaOptions', f'-Djava.home={java_home}')
#     .config('spark.executor.extraJavaOptions', f'-Djava.home={java_home}')
#     .getOrCreate())
import os

# os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'

spark_session = SparkSession.builder.master('local[*]').config("spark.driver.memory", "15g").appName('finance_complaint').getOrCreate()

