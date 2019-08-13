import this
zen_of_python='''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
#word_count_1
sub_1 = "better"
count_1 = zen_of_python.count(sub_1)
print("the count is:",count_1)
#word_count_2
sub_2 = "never"
count_2 = zen_of_python.count(sub_2)
print("the count is:",count_2)
#word_count_3
sub_3 = "is"
count_3 = zen_of_python.count(sub_3)
print("the count is:",count_1)

txt_upper = zen_of_python.upper()
print(txt_upper)

txt_change = zen_of_python.replace('i','&')
print(txt_change)
