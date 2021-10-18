---    
layout:     post    
title:      Linux学习笔记    
subtitle:   Ubuntu学习笔记    
date:       2020-12-02    
author:     AnAn    
header-img: /img/post-bg-article.jpg    
catalog: true    
tags:    
    - Linux    
---    
    
## 目录    
- [环境变量](#环境变量)    
- [标准输出和错误输出](#标准输出和错误输出)    
- [标准输出和错误输出](#常用命令)    
- [定时运行-crontab](#定时运行-crontab)    
- [系统服务工具systemd](#系统服务工具systemd)    
    - [管理命令](#管理命令)    
    - [状态命令](#状态命令)    
    - [服务列表](#服务列表)    
    - [服务状态](#服务状态)    
    - [类型](#类型)    
    - [service-unit](#service-unit)    
    - [laowng.serice](#laowng.serice)    
    - [target-unit](#target-unit)    
    
<a name="环境变量"></a>    
### 环境变量    
- /etc/profile    
  - 此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行.并从/etc/profile.d目录的配置文件中搜集shell的设置.    
  所以如果你有对/etc/profile有修改的话必须得重启你的修改才会生效，此修改对每个用户都生效。    
- /etc/bashrc或/etc/bash.bashrc    
  - :为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取.如果你想对所有的使用bash的用户修改某个配置并    
  在以后打开的bash都生效的话可以修改这个文件，修改这个文件不用重启，重新打开一个bash即可生效。    
- ~/.bash_profile或～/.profile    
  - 每个用户都可使用该文件输入专用于当前用户使用的shell信息,当用户登录时,该文件仅仅执行一次!默认情况下,他设置一些环境变量,执行用户的.bashrc文件.    
- ~/.bashrc    
  - 该文件包含专用于你的bash shell的bash信息,当登录时以及每次打开新的shell时,该文件被读取.    
- set，env，export    
    
  |命令|说明|    
  |:---:|---|    
  |set|用来显示本地变量, 环境变量|    
  |env|用来显示环境变量|    
  |export|用来显示和设置环境变量，声明的变量可以被子shell继承，直接声明的变量则不行|    
    
    
    
<a name="标准输出和错误输出"></a>    
### 标准输出和错误输出    
- command 1 > fielname 把把标准输出重定向到一个文件中    
- command > filename 2>&1 把把标准输出和标准错误一起重定向到一个文件中    
    
<a name="常用命令"></a>    
### 常用命令    
- ctrl-c: ( kill foreground process ) 发送 SIGINT 信号给前台进程组中的所有进程，强制终止程序的执行；    
- ctrl-z: ( suspend foreground process ) 发送 SIGTSTP 信号给前台进程组中的所有进程，常用于挂起一个进程    
- ctrl-d： 一个特殊的二进制值，表示 EOF，作用相当于在终端中输入exit后回车；    
- ctrl-l：清屏幕    
- clear:清除屏幕（与ctrl-l 效果不同）    
- ctrl-s   中断控制台输出    
- ctrl-q   恢复控制台输出    
- jobs：列出后台运行序列号 （ctrl-z 挂起 bg）    
- nohub：不挂断地运行命令    
- &： 后台运行命令    
- fg %num:将挂起的任务放在前台执行    
- bg %num：将挂起的任务放在后台执行    
    
<a name="定时运行-crontab"></a>    
### 定时运行-crontab    
- crontab \[-u username]　　　　//省略用户表表示操作当前用户的crontab      
    -e      (编辑工作表)      
    -l      (列出工作表里的命令)      
    -r      (删除工作作)    
- 格式:    
  
  minute   hour  day   month   week   command      
  \# For details see man 4 crontabs      
  \# Example of job definition:      
  .---------------------------------- minute (0 - 59) 表示分钟      
  |  .------------------------------- hour (0 - 23)   表示小时      
  |  |  .---------------------------- day of month (1 - 31)   表示日期      
  |  |  |  .------------------------- month (1 - 12) OR jan,feb,mar,apr ... 表示月份      
  |  |  |  |  .---------------------- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat  表示星期（0 或 7 表示星期天）      
  |  |  |  |  |  .------------------- username  以哪个用户来执行      
  |  |  |  |  |  |            .------ command  要执行的命令，可以是系统命令，也可以是自己编写的脚本文件      
  |  |  |  |  |  |            |      
  \*  *  *  *  * user-name  command to be executed    
    
- 格式实例：    
    
  |命令|说明|    
  |:---|:---|    
  | */1 * * * * service httpd restart 每一分钟 重启httpd服务 |  每一分钟 重启httpd服务   |    
  |*/1 * * * * service httpd restart|每一分钟 重启httpd服务|    
  |0 */1 * * * service httpd restart|每一小时 重启httpd服务|    
  |30 21 * * * service httpd restart|每天 21：30 分 重启httpd服务|    
  |26 4 1,5,23,28 * * service httpd restart|每月的1号，5号 23 号 28 号 的4点26分，重启httpd服务|    
  |26 4 1-21 * * service httpd restart|每月的1号到21号 的4点26分，重启httpd服务|    
  |*/2 * * * * service httpd restart|每隔两分钟 执行，偶数分钟 重启httpd服务|    
  |1-59/2 * * * * service httpd restart|每隔两分钟 执行，奇数 重启httpd服务|    
  |0 23-7/1 * * * service httpd restart|每天的晚上11点到早上7点 每隔一个小时 重启httpd服务|    
  |0,30 18-23 * * * service httpd restart|每天18点到23点 每隔30分钟 重启httpd服务|    
  |0-59/30 18-23 * * * service httpd restart|每天18点到23点 每隔30分钟 重启httpd服务|    
  |59 1 1-7 4 * test 'date +\\%w' -eq 0 && /root/a.sh|四月的第一个星期日 01:59 分运行脚本 /root/a.sh ，命令中的 test是判断，%w是数字的星期几|    
    
    
<a name="系统服务工具systemd"></a>    
### 系统服务工具systemd    
    
- 说明    
  1. Systemd并不是一个命令，而是一组命令，涉及到系统管理的方方面面。systemctl是Systemd 的主命令，用于管理系统。      
    传统命令init、poweroff、halt、reboot都成为systemctl的软链接    
    切换至紧急救援模式：      
  　　systemctl rescue      
    切换至emergency(紧急)模式：      
  　　systemctl emergency      
    CPU停止工作：    
  　　systemctl halt    
    挂起系统：睡眠模式(也叫挂起suspend)，把信息保存到内存中，断电数据丢失，但是恢复时较快    
  　　systemctl suspend    
    CentOS 7 引导顺序      
      UEFI或BIOS初始化，运行POST开机自检      
      选择启动设备      
      引导装载程序，centos7是grub2      
      加载装载程序的配置文件：/etc/grub.d/ /etc/default/grub /boot/grub2/grub.cfg      
      加载initramfs驱动模块      
      加载内核选项      
      内核初始化，Centos7使用systemd代替init      
      执行initrd.target所有单元，包括挂载/etc/fstab      
      从initramfs根文件系统切换到磁盘根目录      
      systemd执行默认target配置，配置文件/etc/systemd/default.target /etc/systemd/system/      
      systemd执行sysinit.target初始化系统及basic.target准备操作系统      
      systemd启动multi-user.target下的本机与服务器服务      
      systemd执行multi-user.target下的/etc/rc.d/rc.local      
      systemd执行multi-user.target下的getty.target及登入服务      
      systemd执行graphical需要的服务      
  2. 支持systemd的软件配置文件路径一般为“/usr/lib/systemd/system/”    
  3. 开机启动时，systemd只执行/etc/systemd/system/下的配置文件    
    
<a name="管理命令"></a>    
- 管理命令    
  1. sudo systemctl start name.service//启动服务    
  2. sudo systemctl stop name.service//停止服务    
  3. sudo systemctl restart name.service//重启服务    
  4. sudo systemctl status name.service//列出服务状态    
  5. sudo systemctl kill name.service//向服务进程发送kill信号    
  6. sudo systemctl enable name.service//设置服务开机自启动    
     实质是在”/usr/lib/systemd/system/“和“/etc/systemd/system/”两个目录之间建立符号链接关系    
  7. sudo systemctl disable name.service//设置服务取消开机自启动    
  8. sudo systemctl reload name.service//重载服务配置    
  9. sudo systemctl mask name.service//禁止设定为开机自启    
  10. sudo systemctl unmask name.service//取消禁止设定为开机自启    
  11. sudo systemctl daemon-reload //通知systemd更新(扫描)service配置文件    
    
<a name="状态命令"></a>    
- 状态命令    
  1. systemctl is-active name.service    
  2. systemctl is-failed name.service    
  3. systemctl is-enabled name.service    
  4. systemctl list-units -t service//查看已经激活的服务    
  5. systemctl list-units -t service -a//查看所有服务    
  5. systemctl list-units -t service --failed//查看失败的所有服务    
        
    
<a name="服务列表"></a>    
- 服务列表    
  ```sh    
  laowng@laowng-ThinkCentre-M8600t-N000:~$ sudo systemctl list-units -t service --all    
    UNIT                      LOAD      ACTIVE   SUB     DESCRIPTION                 
    accounts-daemon.service   loaded    active   running Accounts Service            
    acpid.service             loaded    active   running ACPI event daemon           
    alsa-restore.service      loaded    active   exited  Save/Restore Sound Card S    
    alsa-state.service        loaded    inactive dead    Manage Sound Card State (    
    anacron.service           loaded    inactive dead    Run anacron jobs            
    apache2.service           loaded    active   running The Apache HTTP Server      
      
  ```    
  - service类型的unit状态：    
  - loaded：Unit配置文件已处理    
  - active(running)：一次或多次持续处理的运行    
  - active(exited)：成功完成一次性的配置    
  - active(waiting)：运行中，等待一个事件    
  - inactive(dead)：不运行    
    
<a name="服务状态"></a>    
- 服务状态    
  ```sh    
  laowng@laowng-ThinkCentre-M8600t-N000:~$ sudo service  mysql status    
  ● mysql.service - MySQL Community Server    
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: en    
     Active: active (running) since Tue 2021-10-12 22:23:37 CST; 3 days ago    
    Process: 2046 ExecStart=/usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/my    
    Process: 1600 ExecStartPre=/usr/share/mysql/mysql-systemd-start pre (code=exit    
   Main PID: 2048 (mysqld)    
      Tasks: 28 (limit: 4915)    
     CGroup: /system.slice/mysql.service    
             └─2048 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid    
      
  10月 12 22:23:17 laowng-ThinkCentre-M8600t-N000 systemd[1]: Starting MySQL Comm    
  10月 12 22:23:37 laowng-ThinkCentre-M8600t-N000 systemd[1]: Started MySQL Commu    
  ```    
  - Loaded行：配置文件的位置，是否设为开机启动    
  - Active行：表示正在运行    
  - Main PID行：主进程ID    
  - Tasks行：由应用本身（这里是 mysql ）提供的软件当前状态    
  - CGroup块：应用的所有子进程    
  - 日志块：应用的日志    
    
<a name="类型"></a>    
- 类型    
  - service：      
　　文件扩展名为.service, 用于定义系统服务    
　　代表一个后台服务进程，比如mysqld。这是最常用的一类。    
  - socket：      
　　文件扩展名为.socket, 用于标识进程间通信用的socket文件，也可在系统启动时，延迟启动服务，实现按需启动    
　　此类配置单元封装系统和互联网中的一个套接字 。当下，systemd支持流式、数据报和连续包的AF_INET、AF_INET6、AF_UNIX socket。每一个套接字配置单元都有一个相应的服务配置单元。相应的服务在第一个"连接"进入套接字时就会启动(例如：nscd.socket 在有新连接后便启动 nscd.service)。    
      
  - device：      
　　文件扩展名为.device, 用于定义内核识别的设备    
　　此类配置单元封装一个存在于 Linux 设备树中的设备。每一个使用 udev 规则标记的设备都将会在 systemd 中作为一个设备配置单元出现。    
      
  - mount：        
　　文件扩展名为.mount, 定义文件系统挂载点    
　　此类配置单元封装文件系统结构层次中的一个挂载点。Systemd 将对这个挂载点进行监控和管理。比如可以在启动时自动将其挂载；可以在某些条件下自动卸载。Systemd 会将/etc/fstab 中的条目都转换为挂载点，并在开机时处理。    
      
  - automount：       
　　文件扩展名为.automount，文件系统的自动挂载点    
　　此类配置单元封装系统结构层次中的一个自挂载点。每一个自挂载配置单元对应一个挂载配置单元 ，当该自动挂载点被访问时，systemd 执行挂载点中定义的挂载行为。    
      
  - swap:        
　　文件扩展名为.swap, 用于标识swap设备    
　　和挂载配置单元类似，交换配置单元用来管理交换分区。用户可以用交换配置单元来定义系统中的交换分区，可以让这些交换分区在启动时被激活。    
      
  - target ：      
　　文件扩展名为.target，用于模拟实现“运行级别”    
　　此类配置单元为其他配置单元进行逻辑分组。它们本身实际上并不做什么，只是引用其他配置单元而已。这样便可以对配置单元做一个统一的控制。这样就可以实现大家都已经非常熟悉的运行级别概念。比如想让系统进入图形化模式，需要运行许多服务和配置命令，这些操作都由一个个配置单元表示，将所有这些配置单元组合为一个目标(target)，就表示需要将这些配置单元全部执行一遍以便进入目标所代表的系统运行状态。 (例如：multi-user.target 相当于在传统使用 SysV 的系统中运行级别 5)    
      
  - timer：      
　　文件扩展名为.timer    
　　定时器配置单元用来定时触发用户定义的操作，这类配置单元取代了 atd、crond 等传统的定时服务。    
      
  - snapshot：      
　　文件扩展名为.snapshot, 管理系统快照    
　  与 target 配置单元相似，快照是一组配置单元。它保存了系统当前的运行状态。    
      
  - path：      
　　文件扩展名为.path，用于定义文件系统中的一个文件或目录使用,常用于当文件系统变化时，延迟激活服务，如：spool 目录    
  　定义了可以被基于路径的触发激活所使用的路径。默认情况下，当路径到了指定的状态(切换到了指定的路径)，一个同名的.service文件将会启用。这里是采用inotify去监控路径的改变    
      
  - slice：      
　　文件扩展名为.slice：与Linux的CGroup相关。其名称反应了其在cgroup树的层次。默认情况下，单元依据其类型的不同被放置在一定的slice里面。    
      
  - scope：      
　　文件扩展名为.scope：Scope单元由systemd接收到总线接口的信息而自动生成。这些Scope单元用于管理由外部创建的系统进程(非Systemd 启动的外部进程)。    
    
<a name="service-unit"></a>    
- service-unit    
  - 这里列举sshd服务的配置文件    
    ```sh    
    laowng@laowng-ThinkCentre-M8600t-N000:~$ sudo systemctl cat sshd    
    # /lib/systemd/system/ssh.service    
    [Unit]    
    Description=OpenBSD Secure Shell server    
    After=network.target auditd.service    
    ConditionPathExists=!/etc/ssh/sshd_not_to_be_run    
        
    [Service]    
    EnvironmentFile=-/etc/default/ssh    
    ExecStartPre=/usr/sbin/sshd -t    
    ExecStart=/usr/sbin/sshd -D $SSHD_OPTS    
    ExecReload=/usr/sbin/sshd -t    
    ExecReload=/bin/kill -HUP $MAINPID    
    KillMode=process    
    Restart=on-failure    
    RestartPreventExitStatus=255    
    Type=notify    
    RuntimeDirectory=sshd    
    RuntimeDirectoryMode=0755    
        
    [Install]    
    WantedBy=multi-user.target    
    Alias=sshd.service    
    ```      
      
  - Unit(定义与Unit类型无关的通用选项；用于提供unit的描述信息、unit行为及依赖关系等)    
    - Description：描述信息    
    - Documentation：文档地址    
    - After：表示当前Unit应该在network.target auditd.service服务之后启动    
    - Before: 表示当前Unit应该在那些Unit之前启动（上述文件无）    
    - Wants：若依赖关系，如果指定Unit没有运行，不应影响当前Unit继续执行    
    - Requires：强依赖关系，如果指定Unit没有运行本Unit会启动失败    
    - BindsTo：与Requires类似，它指定的Unit如果退出，会导致当前Unit停止运行    
    - Conflicts：这里指定的Unit不能与当前Unit同时运行    
    - Condition：当前Unit运行必须满足的条件，否则不会运行    
    - Assert：当前Unit运行必须满足的条件，否则会报启动失败    
    - ConditionPathExists:必须存在指定路径才运行（路径前加!表示不存在）    
    - **Before 和 After只涉及启动顺序，不涉及依赖关系；Wants字段与Requires字段只涉及依赖关系，与启动顺序无关，默认情况下是同时启动的**    
  - Service(与特定类型相关的专用选项；只有Service类型的Unit才有这个区块)    
    - Type：定义启动时的进程行为。它有以下几种值。    
      - Type=simple：默认值，ExecStart字段启动的进程为主进程    
      - Type=forking：ExecStart字段将以fork()方式启动(从父进程创建子进程)，此时父进程将会退出，子进程成为主进程    
      - Type=oneshot：类似于simple，但只执行一次，Systemd 会等它执行完，才启动其他服务    
      - Type=dbus：类似于simple，但会等待 D-Bus信号后启动(通过D-Bus启动)    
      - Type=notify：类似于simple，当前服务启动完毕后会发通知信号给Systemd，然后Systemd再启动其他服务    
      - Type=idle：类似于simple，但是要等到其他任务都执行完，才会启动该服务。一种使用场合是为让该服务的输出，不与其他服务的输出相混合    
    - RemainAfterExit：字段设为yes，表示进程退出以后，服务仍然保持执行（配合Type=oneshot使用）    
    - ExecStart：启动当前服务的命令    
    - ExecStartPre：启动当前服务之前执行的命令    
    - ExecStartPost：启动当前服务之后执行的命令    
    - ExecReload：重启当前服务时执行的命令    
    - ExecStop：停止当前服务时执行的命令    
    - ExecStopPost：停止当其服务之后执行的命令    
    - RestartSec：自动重启当前服务间隔的秒数    
    - Restart：定义何种情况Systemd会自动重启当前服务，可能的值包括always(总是重启)、on-success、on-failure、on-abnormal、on-abort、on-watchdog    
      - no（默认值）：退出后不会重启    
      - on-success：只有正常退出时（退出状态码为0），才会重启    
      - on-failure：非正常退出时（退出状态码非0），包括被信号终止和超时，才会重启    
      - on-abnormal：只有被信号终止和超时，才会重启    
      - on-abort：只有在收到没有捕捉到的信号终止时，才会重启    
      - on-watchdog：超时退出，才会重启    
      - always：不管是什么退出原因，总是重启    
    - RestartPreventExitStatus:当符合某些退出状态时不要进行重启    
    - TimeoutSec：定义Systemd停止当前服务之前等待的秒数    
    - KillMode：systemctl kill时执行的操作：    
      - control-group（默认值）：当前控制组里面的所有子进程，都会被杀掉    
      - process：只杀主进程    
      - mixed：主进程将收到 SIGTERM 信号，子进程收到 SIGKILL 信号    
      - none：没有进程会被杀掉，只是执行服务的 stop 命令    
    - Environment：指定环境变量    
    - EnvironmentFile：指定当前服务的环境参数文件。该文件内部的key=value键值对，可以用$key的形式，在当前配置文件中获取    
    - **所有的启动设置之前，都可以加上一个连词号（-），表示"抑制错误"，即发生错误的时候，不影响其他命令的执行**    
          
  - Install(定义如何启动，以及是否开机启动)      
    - WantedBy：它的值是一个或多个Target，当前Unit激活时(enable)符号链接会放入/etc/systemd/system目录下面以Target名+.wants后缀构成的子目录中    
        Target的含义是服务组，表示一组服务。WantedBy=multi-user.target指的是，sshd 所在的 Target 是multi-user.target。      
        这个设置非常重要，因为执行systemctl enable sshd.service命令时，sshd.service的一个符号链接，就会放在/etc/systemd/system目录下面的multi-user.target.wants子目录之中。      
    - RequiredBy：它的值是一个或多个Target，当前Unit激活时，符号链接会放入/etc/systemd/system目录下面以Target名+.required后缀构成的子目录中      
    - Alias：当前Unit可用于启动的别名    
    - Also：当前Unit激活(enable)时，会被同时激活的其它Unit      
    
<a name="laowng.serice"></a>    
- 这里展示一个测试的laowng.serice    
  - /lib/systemd/system/laowng.service(ubuntu18.04 服务位置在/lib)    
    ```sh    
    [Unit]    
    Description=laowng de test service    
    After=network.target    
        
    [Service]    
    ExecStart=/home/laowng/bin/test.sh    
    ExecReload=/bin/kill -HUP $MAINPID    
    KillMode=control-group    
    Restart=on-failure    
    Type=forking    
        
    [Install]    
    WantedBy=multi-user.target    
    Alias=laowng.service    
    ```    
  - test.sh    
    ```sh    
    #/home/laowng/bin/test.sh    
    #!/bin/bash    
    nohup /home/laowng/bin/test.service >>test.log &    
    ```    
  - test.service    
    ```sh    
    #!/bin/bash    
    date >>/home/wangwen/bin/test.log    
    sleep 5s    
    date >>/home/wangwen/bin/test.log    
    sleep 60s    
    date >>/home/wangwen/bin/test.log    
    sleep 120s    
    date >>/home/wangwen/bin/test.log    
    ```    
    
<a name="target-unit"></a>    
- target-unit    
    
  启动计算机的时候，需要启动大量的Unit。如果每一次启动，都要一一写明本次启动需要哪些Unit，显然非常不方便。Systemd的解决方案就是 Target。简单说，Target就是一个Unit 组，包含许多相关的Unit。启动某个Target的时候，Systemd就会启动里面所有的 Unit。从这个意义上说，Target 这个概念类似于"状态点"，启动某个 Target 就好比启动到某种状态。    
    
  传统的init启动模式里面，有RunLevel的概念，跟Target的作用很类似。不同的是RunLevel 是互斥的，不可能多个 RunLevel 同时启动，但是多个 Target可以同时启动。    
    
  - target类型unit配置文件：/usr/lib/systemd/system/*.target    
    
  - Target与传统RunLevel 的对应关系如下：    
    
    |Traditional runlevel|New target name   Symbolically linked to...|    
    |:---:|---|    
    |Runlevel 0 　　　| runlevel0.target -> poweroff.target  关机|    
    |Runlevel 1 　　　| runlevel1.target -> rescue.target   单用户模式或者救援模式|    
    |Runlevel 2 　　　| runlevel2.target -> multi-user.target|    
    |Runlevel 3 　　　| runlevel3.target -> multi-user.target 正常多用户命令行模式|    
    |Runlevel 4 　　　| runlevel4.target -> multi-user.target|    
    |Runlevel 5 　　　| runlevel5.target -> graphical.target 正常多用户图形模式|    
    |Runlevel 6 　　　| runlevel6.target -> reboot.target   重启|    
  - 配置文件    
    ```sh    
    wangwen@wangwen-ThinkCentre-M8600t-N000:~$ sudo systemctl cat multi-user.target    
    # /lib/systemd/system/multi-user.target    
    #  SPDX-License-Identifier: LGPL-2.1+    
    #    
    #  This file is part of systemd.    
    #    
    #  systemd is free software; you can redistribute it and/or modify it    
    #  under the terms of the GNU Lesser General Public License as published by    
    #  the Free Software Foundation; either version 2.1 of the License, or    
    #  (at your option) any later version.    
        
    [Unit]    
    Description=Multi-User System    
    Documentation=man:systemd.special(7)    
    Requires=basic.target    
    Conflicts=rescue.service rescue.target    
    After=basic.target rescue.service rescue.target    
    AllowIsolate=yes    
    ```    
- 后记    
  **有些程序不建议使用root权限执行，在脚本中可以使用“sudo -u username 命令”的方式执行**            
        
    
    
 