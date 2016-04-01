#!/bin/bash
#ShellName:LazyManage.sh
#Conf:serverlist.conf
#By:peter.li
#2013-05-30
#http://hi.baidu.com/quanzhou722/item/4ccf7e88a877eaccef083d1a


#定义脚本编码为英文utf8
LANG="en_US.UTF-8"

#定义最外层循环,用于菜单返回操作
while true
do

#定义交互式所需变量和自定义操作变量
Set_Variable(){

#配置文件:ip列表，服务器特定信息等
#  #1IP            2平台     3主机类型      4自定义路径           5passwd
#  192.168.1.10    job1      web            /data/apache/www/     8JRcsmw
ServerList=serverlist.conf
#ssh或scp端口号
Port=22
#每次操作超时时间
TimeOut=30

#管理账号:被管理机器上已存在的普通用户，需要统一，不统一请定义在ServerList中匹配截取
RemoteUser="peterli"
RemotePasswd="123456"
#被管理机器上root账号密码,用于su操作，注意此脚本权限保密
RemoteRootPasswd="xuesong"
#管理账号密钥的密码,如果管理账号已有密钥信任关系,并且设置密码请添加此项，其他情况无需管此项
KeyPasswd=""

#每次操作前请修改确认以下变量是否正确,在执行操作
#自定义命令
Cmd="/sbin/ifconfig eth0"
#自定义传送文件或文件夹的本地路径
ScpPath="/root/lazy.txt"
#传送文件到远程目录下
ScpRemotePath="/tmp/"
#自定义脚本路径,请先测试脚本正确性,在批量操作
ScriptPath="Remote.sh"
}

#系统环境检查
System_Check(){

#执行此脚本加kill参数即可结束后台或其它窗口的此脚本. 例: # ./LazyManage.sh kill
if [ "$1" == kill ];then
    ps -eaf |awk '$NF~/.*'${0##*/}'/&&$6~/tty|pts.*/{print $2}' |xargs -t -i kill -9 {}
    exit
fi

#检查配置文件是否存在并且不为空
if [ ! -s serverlist.conf ];then
    echo "error:IP list serverlist.conf file does not exist or is null"
    exit
fi


#检查所需软件是否存在
for i in dialog expect
do
    rpm -q $i >/dev/null
    [ $? -ge 1 ] && echo "$i does not exist,Please root yum -y install $i to install,exit" && exit
done

#检查执行脚本用户
LazyUser=`whoami`

#检查系统参数,可根据需求取相关信息
BitNum=`getconf LONG_BIT`
#SystemNum=`lsb_release -a|grep Release |awk '{print $2}'`

}

#选择操作菜单
Select_Type() {
while true
do
clear
    #判断上层菜单选择,列出相应菜单以供选择
    case $Operate in
    1)
        Type=`dialog --no-shadow --stdout --backtitle "LazyManage" --title "System work content"  --menu "select" 10 60 0 \
        1a "[Common operations]" `
    ;;
    2)
        Type=`dialog --no-shadow --stdout --backtitle "LazyManage" --title "Custom work content"  --menu "select" 10 60 0 \
        1b "[web upgrade]" \
        2b "[db   manage]" `
    ;;
    esac
    #确认选择并执行下一菜单函数Select_Work
    [ $? -eq 0 ] && Select_Work $Type || break
done
}

#选择平台操作菜单
Select_Work() {
while true
do
clear
    case $Type in
    1a)
        Work=`dialog --no-shadow  --stdout --backtitle "LazyManage" --title "Common operations" --menu "select" 20 60 0 \
        1aa "[custom cmd ]" \
        2aa "[scp file   ]" \
        3aa "[exec script]" `
    ;;
    1b)
        Work=`dialog --no-shadow  --stdout --backtitle "LazyManage" --title "web upgrade" --menu "select" 20 60 0 \
        1ba "[job1]" \
        2ba "[job2]" \
        3ba "[job3]" `
    ;;
    2b)
        Work=`dialog --no-shadow  --stdout --backtitle "LazyManage" --title "db   manage" --menu "select" 20 60 0 \
        1bb "[job1]" \
        2bb "[job2]" \
        3bb "[job3]" `
    ;;
    esac
    #确认操作后执行选择IP函数Get_Ip
    [ $? -eq 0 ] && Get_Ip $Work || break
done
}

#选择IP函数
Get_Ip(){
while true
do
clear
#判断以上菜单所有选择,分别截取不同操作和不同平台所对应的IP列表
case $Work in
#Select_Work函数中dialog菜单选择的结果变量 1aa 或 2aa 等皆通过以下命令截取对应IP
[1-9]a[a-z])
    #截取配置文件中 不为#开头 并且 非空行 取出全部IP列表
    List=`awk '$1!~"^#"&&$1!=""{print $1" "$2" on"}' $ServerList |sort -u`
;;
1ba)
    #截取IP列表可根据配置文件相关列匹配对应的操作IP
    List=`awk '$1!~"^#"&&$1!=""&&$2=="job1"&&$3=="web"{print $1" "$2"_"$3" on"}' $ServerList`
;;
2ba)
    List=`awk '$1!~"^#"&&$1!=""&&$2=="job2"&&$3=="web"{print $1" "$2"_"$3" on"}' $ServerList`
;;
3ba)
    List=`awk '$1!~"^#"&&$1!=""&&$2=="job3"&&$3=="web"{print $1" "$2"_"$3" on"}' $ServerList`
;;
1bb)
    List=`awk '$1!~"^#"&&$1!=""&&$2=="job1"&&$3=="db"{print $1" "$2"_"$3" on"}' $ServerList`
;;
2bb)
    List=`awk '$1!~"^#"&&$1!=""&&$2=="job2"&&$3=="db"{print $1" "$2"_"$3" on"}' $ServerList`
;;
3bb)
    List=`awk '$1!~"^#"&&$1!=""&&$2=="job3"&&$3=="db"{print $1" "$2"_"$3" on"}' $ServerList`
;;
*)
    echo "Dialog list does not exist"
    break
;;
esac

#选择列出的IP列表菜单
IpList=`dialog --no-shadow  --stdout --backtitle "LazyManage" --title "ip list" --separate-output --checklist "select IP" 0 60 0 $List`
[ $? -eq 0 ]  || break 

Message=`cat <<EOF

Please make sure the information
========================

$IpList

========================
EOF`

#确认IP菜单后执行Perform函数进行操作
dialog --backtitle "LazyManage" --title "Confirm IP" --no-shadow --yesno "$Message" 20 60
[ $? -eq 0 ] && Perform || break

done
}

#判断选择调用执行函数,此脚本中最重要的中枢
Perform(){
    #创建日志目录
    mkdir -p ./lazyresult
    #记录执行失败时间
    echo "============= `date +%Y-%m-%d_%H:%M` =============" >>./lazyresult/lazyerr.log
    #判断最终选择操作分别执行不同函数操作
    case $Work in
    1aa)
        #记录每一次操作
        echo "Custom_Cmd ${Cmd}">>./lazyresult/lazyerr.log
        #创建每次正确操作日志目录
        Result=lazy`date +%m%d%H%M_%N`
        mkdir -p ./lazyresult/$Result
        #执行交互操作函数,将本次操作内容传递给交互函数
        Interactive_Auth Ssh_Cmd
    ;;
    2aa)
        echo "Scp_File ${ScpPath}-${ScpRemotePath}">>./lazyresult/lazyerr.log
        Interactive_Auth Scp_File
    ;;
    3aa)
        echo "Exec_Script ${ScriptPath}">>./lazyresult/lazyerr.log
        Interactive_Auth Ssh_Script
    ;;
    [1-9]ba)
        echo "custom"
    ;;
    [1-9]bb)
        echo "custom"
    ;;

    *)
        #选择不再操作列表中
        echo "Dialog list does not exist"
        break
    ;;
    esac
    
    #本次操作完成
    echo "Operation is complete "
    read
}

#多进程后台控制(暂未启用)
More_Thread(){
#循环所有IP
for Ip in $IpList
do
    echo "$Ip $1"
    #后台执行此函数时传递的函数
    $1 &
    #记录后台执行次数
    ((num++))
    #判断后台操作次数
    if [ $num -eq 6 ];then
    echo "wait..."
    #等待本次后台6个操作完成
    wait
    #从新计数
    num=0
    fi
done
#等待全部后台完成
wait
read
}

#交互执行操作函数,真正干活的地方
Interactive_Auth(){

#循环所有IP
for Ip in $IpList
do
#如root密码不统一，请在配置文件中对应IP定义，开启下行分别截取IP对应密码
#RemoteRootPasswd=`awk '$1=='$Ip'{print $5}' $ServerList`

#执行交互操作
/usr/bin/expect -c "

#在expect中定义jiaohu函数,已将大部分可能定义了，交互中如遇到个别情况,可自行参考添加交互判断
proc jiaohu {} {
    #判断操作后的显示
    expect {
        #显示password,说明通过用户及密码执行ssh操作
        password {
            #打印本次输入提示
            send_user RemotePasswd
            #输入用户密码回车
            send ${RemotePasswd}\r;
            #再次判断操作后的显示
            expect {
                #下行提示为:root用户不存在
                \"does not exist\" {
                    #打印错误说明
                    send_user \"root user does not exist\n\"
                    #退出并返回错误状态
                    exit 10
                }
                #下行提示为:密码不正确再次输入
                password {
                    send_user \"user passwd error\n\"
                    exit 5
                }
                #下行提示为:输入root密码
                Password {
                    send_user RemoteRootPasswd
                    send ${RemoteRootPasswd}\r;
                    #再次判断密码输入后显示
                    expect {
                        #下行提示为:root密码错误
                        incorrect {
                            send_user \"root passwd error\n\"
                            exit 6
                        }
                        #交互操作成功:普通账号后su操作
                        eof 
                    }
                }
                #交互操作成功:使用root直接操作
                eof
            }
        }
        #密钥并且密钥加密码方式操作
        passphrase {
            send_user KeyPasswd
            send ${KeyPasswd}\r;
            expect {
                \"does not exist\" {
                    send_user \"root user does not exist\n\"
                    exit 10
                }
                passphrase{
                    send_user \"key passwd error\n\"
                    exit 7
                }
                Password {
                    send_user RemoteRootPasswd
                    send ${RemoteRootPasswd}\r;
                    expect {
                        incorrect {
                            send_user \"root passwd error\n\"
                            exit 6
                        }
                        eof
                    }
                }
                eof
            }
        }
        #密钥无密码后su操作
        Password {
            send_user RemoteRootPasswd
            send ${RemoteRootPasswd}\r;
            expect {
                incorrect {
                    send_user \"root passwd error\n\"
                    exit 6
                }
                eof
            }
        }
        #主机不存在
        \"No route to host\" {
            send_user \"host not found\n\"
            exit 4
        }
        #无效参数:IP或端口不合法
        \"Invalid argument\" {
            send_user \"incorrect parameter\n\"
            exit 8
        }
        #拒绝连接:ssh端口号错误
        \"Connection refused\" {
            send_user \"invalid port parameters\n\"
            exit 9
        }
        #root或管理员账号不存在
        \"does not exist\" {
            send_user \"root user does not exist\"
            exit 10
        }
        #交互操作超时
        timeout {
            send_user \"connection timeout \n\"
            exit 3
        }
        eof
    }
}

#设置超时时间
set timeout $TimeOut
#判断此函数参数,执行不同操作,tcl语言流程结构,等同shell中case
switch $1 {
    
    Ssh_Cmd {
        #当参数为Ssh_Cmd时执行以下操作
        spawn ssh -t -p $Port -o StrictHostKeyChecking=no $RemoteUser@$Ip /bin/su - root -c \\\"$Cmd|tee /tmp/Lazy.tmp\\\";
        #调用此expect命令中的jiaohu函数
        jiaohu
        spawn scp -P $Port -o StrictHostKeyChecking=no -r $RemoteUser@$Ip:/tmp/Lazy.tmp ./lazyresult/$Result/${Ip}_result.log;
        jiaohu
    }
    Ssh_Script {
        spawn scp -P $Port -o StrictHostKeyChecking=no $ScriptPath $RemoteUser@$Ip:/tmp/${ScriptPath##*/};
        jiaohu
        spawn ssh -t -p $Port -o StrictHostKeyChecking=no $RemoteUser@$Ip /bin/su - root -c  \\\"/bin/sh /tmp/${ScriptPath##*/}\\\" ;
        jiaohu
    }
    Scp_File {
        spawn scp -P $Port -o StrictHostKeyChecking=no -r $ScpPath $RemoteUser@$Ip:${ScpRemotePath};
        jiaohu
    }
}
#打印IP完成
send_user ${Ip}_Done\n
"
state=`echo $?`
#取上句expect的结束状态,如果错误记录日志
[ $state -ne 0 ] && echo "$Ip $state" >>./lazyresult/lazyerr.log
echo "================================================"
echo ""

done

}

#阻止ctrl+c
trap "" 2 3

#执行系统环境检查
System_Check $1

#定义所有变量
Set_Variable

#Script entrance
#脚本入口
#通过dialog窗口菜单选择结果赋值给变量Operate
Operate=`dialog --no-shadow --stdout --backtitle "LazyManage" --title "manipulation menu"  --menu "select" 10 60 0 \
1 "[system operate]" \
2 "[custom operate]" `
#确认选择后执行函数Select_Type,进入下一步菜单，如果取消则退出脚本
[ $? -eq 0 ] && Select_Type $Operate || exit

done

#End
