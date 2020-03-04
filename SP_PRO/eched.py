import time,datetime,os,random
from leaderShip import leaderShip
from apscheduler.schedulers.blocking import BlockingScheduler
def fun_c():
    print('定时任务开始...')
    loginMsg={
            'login_url':'http://if.fyi:1180/xmlrpc.php',
            'login_usr':'if_fyi',
            'login_pw':'if_fyi',
            'wp_log':'if-fyi.log'
            }
    spParse=leaderShip(loginMsg)
    spParse.spiders_collect()

def dojob():
    #创建调度器：BlockingScheduler
    print('定时任务调度,开始')
    sched = BlockingScheduler()
    intc=random.randint(1,30)
    sched.add_job(fun_c,'cron',hour=6, minute=intc)
    sched.start()

if __name__=='__main__':
    dojob()
    #fun_c()
