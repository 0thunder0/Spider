import time,datetime,os,random
from leaderShip import leaderShip
from apscheduler.schedulers.blocking import BlockingScheduler
def fun_c():
    #print('定时任务开始...')
    loginMsg={
            'login_url':'http://zz.7oh.net/xmlrpc.php',
            'login_usr':'iyo_cx',
            'login_pw':'$iyo.cx_jax.ye',
            'wp_log':'iyo_cx.log'
            }
    spParse=leaderShip(loginMsg)
    spParse.spiders_collect()

def dojob():
    #创建调度器：BlockingScheduler
    print('定时任务调度,开始')
    sched = BlockingScheduler()
    intc=random.randint(30,59)
    sched.add_job(fun_c,'cron',hour=11, minute=intc)
    sched.start()

if __name__=='__main__':
    dojob()
    #fun_c()
