import os
import shutil
import re
import random
# def copy_rename(old_file_name, new_file_name):
#         src_dir= os.curdir
#         dst_dir= os.path.join(os.curdir , "subfolder")
#         src_file = os.path.join(src_dir, old_file_name)
#         shutil.copy(src_file,dst_dir)
        
#         dst_file = os.path.join(dst_dir, old_file_name)
#         new_dst_file_name = os.path.join(dst_dir, new_file_name)
#         os.rename(dst_file, new_dst_file_name)
#         print('done')

# if __name__ == '__main__':
#     old_file_name = '/home/jrivera/Documents/Python_stuff/dataScrubber/BC583-Scrubber/BC583-Scrubbed-P.txt'
#     new_file_name = '/home/jrivera/Documents/Python_stuff/dataScrubber/BC583-Scrubber/BC583-Scrubbed-P-1.txt'
#     copy_rename(old_file_name, new_file_name)


# def page_number(infile, outfile):
#     import re
#     regx = re.compile(r'^DPR#')

#     with open(infile) as fin:
#         with open(outfile, 'w') as fout:
#             for line in fin:
#                 if regx.match(line):
#                     for i in range(0,901):
#                         new_number = i + 1
#                         number_string = str(new_number)
#                         line = line[:159] + number_string + line[161:]
#                         fout.write(line)
#                 else:
#                     fout.write(line)


# if __name__ == '__main__':
#         infile = '/home/jrivera/Documents/Python_stuff/dataScrubber/BC583-Scrubber/BC583-Scrubbed-FAD.txt'
#         outfile = '/home/jrivera/Documents/Python_stuff/dataScrubber/BC583-Scrubber/BC583-Scrubbed-P.txt'
#         page_number(infile, outfile)



def page_number(infile, outfile):
    import re
    regx = re.compile(r'^DPR#')

    with open(infile) as fin:
        with open(outfile, 'w') as fout:
            pagenum = 0
            for line in fin:
                if regx.match(line):
                    pagenum = pagenum + 1
                    print(pagenum)
                    line = f'{line[:159]}{pagenum}\n'
                fout.write(line)



if __name__ == '__main__':
        infile = '/home/jrivera/Documents/Python_stuff/dataScrubber/BC583-Scrubber/BC583-Scrubbed-FAD.txt'
        outfile = '/home/jrivera/Documents/Python_stuff/dataScrubber/BC583-Scrubber/BC583-Scrubbed-P.txt'
        page_number(infile, outfile)