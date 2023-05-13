package org.example;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;

import java.io.IOException;

public class WcDriver {
    //psvm
    public static void main(String[] args) throws IOException {
        //创建一个对象
        Configuration conf = new Configuration();
        //core-site.xml是来指定我们操作的文件系统hdfs
        conf.set("fs.defaultFS","hdfs://dsj3master:9000");
        //指定用户名
        System.setProperty("HADOOP_USER_NAME","root");
        /*
        通过FileSystem的静态方法get获得对象
        被static修饰的静态方法，通过类名.出来
        如果不是静态方法该怎么办呢？要实例化才能使用
        什么是实例化？就是创建一个对象 Configuration conf = new Configuration();
        new出来的对象可以调用动态方法
        什么是构造器？方法名为类名，而且方法没有返回值
         */
        FileSystem fs = FileSystem.get(conf);
        //sout
        System.out.println(fs.toString());
    }
}
