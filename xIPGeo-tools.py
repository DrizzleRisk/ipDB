# -*- coding: utf-8 -*-
# code By Drizzle
import socket,struct,sys,string,random,datetime

# 根据现有ipDB生成10进制ip range
def ip2int():
    file_object_read = open('ipDB_0401.txt','r')
    file_object_write = open('ipDB_int_0401.txt','w')

    all_the_text = file_object_read.read()

    # ip2int
    line_arr = all_the_text.split('\n')
    for i in range(len(line_arr)):
        cell = line_arr[i].split(' ')
        cell[0] = str(socket.ntohl(struct.unpack("=I",socket.inet_aton(cell[0]))[0]))
        cell[1] = str(socket.ntohl(struct.unpack("=I",socket.inet_aton(cell[1]))[0]))
        line_arr[i] = ' '.join(cell)
    all_the_text = '\n'.join(line_arr)    

    file_object_write.write(all_the_text)
    file_object_read.close()
    file_object_write.close()

# 创建随机IP
def CreateIPS(num):
    file_object_write = open('random_ips.txt','w')
    for i in range(long(num)):
        file_object_write.write(str(socket.inet_ntoa(struct.pack("=I", random.uniform(16777216,3758096383)))))
        file_object_write.write('\n')
    file_object_write.close()

# 二分查找法效率测试
def finds2():
    file_object_read = open('ipDB_int_0401.txt','r')
    file_object_read2 = open('random_ips.txt','r')

    all_the_text = file_object_read.read()
    all_the_ip = file_object_read2.read()

    l_arr = [[]]
    line_arr = all_the_text.split('\n')
    ip_arr = all_the_ip.split('\n')
    # 二维数组
    for i in range(len(line_arr)):
        l_arr.append(line_arr[i].split(' '))
        l_arr[i+1][0] = long(l_arr[i+1][0])
        l_arr[i+1][1] = long(l_arr[i+1][1])
    find_success = 0
    l_arr_len = len(l_arr)

    start = datetime.datetime.now()
    # 二分查找
    for q in xrange(len(ip_arr)):
        if ip_arr[q] is not '':
            iip = socket.ntohl(struct.unpack("=I",socket.inet_aton(ip_arr[q]))[0])
            low = 0
            high = l_arr_len
            while low <= high:
                mid = (low + high) // 2
                midVal1 = l_arr[mid][0]
                midVal2 = l_arr[mid][1]
                if iip < midVal1:
                    high = mid
                elif iip > midVal2:
                    low = mid
                elif midVal1 <= iip <= midVal2:
                    find_success = find_success + 1
                    break     
                else:
                    print 'error'
    # end
    end = datetime.datetime.now()
    print 'GeoIP DB records: '+str(len(line_arr))
    print 'Random IP Total:  '+str(q)
    print 'Success Found:    '+str(find_success)
    print 'Time Cost:        '+str(end-start)

if __name__ == '__main__':
    #ip2int()
    #CreateIPS(sys.argv[1])
    finds2()
