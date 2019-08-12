
import shutil # For copy file
import os
import sys

def main():
    if(len(sys.argv) < 4):
        print("Missing arguments! Usage us script log_file 10 5")
        exit(1)

    file_name = str(sys.argv[1])
    limit_size = int(sys.argv[2])
    logs_number = int(sys.argv[3])


    if (os.path.isfile(file_name) == True):
        logfile_size = os.stat(file_name).st_size # Get file size in BYTES
        logfile_size = logfile_size // 1024 #Kilobytes

        if(logfile_size >= limit_size):
            if (logs_number > 0):
                for currentFileNum in range(logs_number, 1, -1):
                    src = file_name + "_" + str(currentFileNum-1)
                    dst = file_name + "_" + str(currentFileNum)
                    if(os.path.isfile(src) == True):
                        shutil.copyfile(src, dst)
                        print("Copied" + src + " to " + dst)

                shutil.copyfile(file_name, file_name + "_1")
                print("Copied " + file_name +" to "+file_name + "_1")
            myfile = open(file_name, 'w')
            myfile.close()


if __name__ == '__main__':
    main()
