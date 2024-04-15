## Баг 1

При выполнении Testcase 5,6,7,8,9 - текст на элементе с энергией накладывается друг на друга.

|TestCase №|Energy|Est.|
|--|--|--|
|Testcase 5|1000000|мВт.|
|Testcase 6|999999999|Млн. мВт.|
|Testcase 7|1000000000|Млн. мВт.|
|Testcase 8|999999999999|Млрд. мВт.|
|Testcase 9|1000000000000|Млрд мВт.|

![b1](https://github.com/k4dms/avitoqa/raw/main/second/output/Testcase5.png)
![T6](https://github.com/k4dms/avitoqa/blob/main/second/output/Testcase6.png)
![T7](https://github.com/k4dms/avitoqa/blob/main/second/output/Testcase7.png)
![T7](https://github.com/k4dms/avitoqa/blob/main/second/output/Testcase8.png)
![T7](https://github.com/k4dms/avitoqa/blob/main/second/output/Testcase9.png)