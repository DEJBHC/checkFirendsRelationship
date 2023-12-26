import time
import random
import uiautomator2 as u2
from getFriends import get_friend_list
"""
查看字符串是否包含括号.
Args:
    strs(str): 必选参数
Returns:
    bool:是否包含括号
"""
def check_bricks(strs):
    for char in strs:
        if char in ['(',')','（','）']:
            return True
    return False
d=u2.connect('设备名称')#连接设备名称
p=get_friend_list()#获取好友列表
def check_f():
    for pe in p:
        d(resourceId="com.tencent.mm:id/meb").click()#点击搜索框
        time.sleep(random.uniform(0.5,1.5))
        d.send_keys(pe)#输入昵称
        time.sleep(random.uniform(0.5,1.5))
        d(resourceId="com.tencent.mm:id/odf").click()#点击昵称
        time.sleep(random.uniform(0.5,1.5))
        d.click(0.931, 0.97)#点击加号
        time.sleep(random.uniform(0.5,1.5))
        d.xpath('//*[@resource-id="com.tencent.mm:id/a1u"]/android.widget.LinearLayout[6]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()#点击转账
        time.sleep(random.uniform(0.5,1.5))
        strs=d(resourceId="com.tencent.mm:id/lwo").get_text()#获取实名信息
        if not check_bricks(strs):#如果名字没有括号，则为异常好友（可能的原因：拉黑，删除，未实名，网络异常）
            print(p[0])
        #当然，我们是可以检测到异常好友弹窗的，如下代码。
        #if d(resourceId="com.tencent.mm:id/jlh").exists:
            print(p[0])
        time.sleep(random.uniform(0.5,1.5))
        for i in range(5):#退回到主页
            d.press("back")
            time.sleep(random.uniform(0.5,1.5))
check_f()
