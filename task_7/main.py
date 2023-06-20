from cw_seven import new_text as one
from cw_seven import new_name as two
from cw_seven import task_three as three
from cw_seven import new_bin_files as nbf
from cw_seven import rename as rn
if __name__ == '__main__':
    # one.feel_num(5, 'file3.txt')
    # two.fail_name(3, 'file_2.txt')
    # three.new('file_1.txt', 'file_2.txt', 'result.txt')
    # nbf.gen_files('bin', 3, 10, num=3)
    rn.group_rename(new_name='pineapple', num=2, extention_old='.txt', extention_new='.jpg',
                    catalog='/Users/Mokonajen/PycharmProjects/pythonProject1/practical_task_1/task_7', name_range=[1, 5])