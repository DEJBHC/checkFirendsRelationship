import time
import uiautomation as auto
wx_window = auto.WindowControl(Name='微信', ClassName='WeChatMainWndForPC')
def get_friend_list(tag: str = None, num: int = 10) -> list:
    """
    获取微好友名称.
    Args:
        tag(str): 可选参数，如不指定，则获取所有好友
        num(int): 可选参数，如不指定，只获取10页好友
    Returns:
        list:好友名单
    """
    def click_tag():
        """点击标签"""
        contacts_window.ButtonControl(Name="标签").Click()

    auto.SendKeys(text='{Alt}{Ctrl}w')  # 快捷键唤醒微信
    # 点击 通讯录管理
    wx_window.ButtonControl(Name="通讯录").Click()
    wx_window.ListControl(Name="联系人").ButtonControl(Name="通讯录管理").Click()
    contacts_window = auto.GetForegroundControl()  # 切换到通讯录管理，相当于切换到弹出来的页面

    if tag:
        click_tag()  # 点击标签
        contacts_window.PaneControl(Name=tag).Click()
        time.sleep(0.3)
        click_tag()  # 关闭标签

    # 获取滑动模式
    scroll = contacts_window.ListControl().GetScrollPattern()
    assert scroll, "没有可滑动对象"
    name_list = list()
    rate: int = int(float(102000 / num))  # 根据输入的num计算滑动的步长
    for pct in range(0, 102000, rate):  # range不支持float，不导入numpy库，采取迂回这的方式
        # 每次滑动一点点，-1代表不用滑动
        scroll.SetScrollPercent(horizontalPercent=-1, verticalPercent=pct / 100000)
        for name_node in contacts_window.ListControl().GetChildren():  # 获取当前页面的 列表 -> 子节点
            nick_name = name_node.TextControl().Name  # 用户名
            remark_name = name_node.ButtonControl(foundIndex=2).Name  # 用户备注名，索引1会错位，索引2是备注名，索引3是标签名
            name_list.append(remark_name if remark_name else nick_name)
    contacts_window.SendKey(auto.SpecialKeyNames['ESC'])  # 结束时候关闭 "通讯录管理" 窗口
    return list(set(name_list))  # 简单去重，但是存在误判（如果存在同名的好友
# print(get_friend_list(tag="无标签", num = 2))
print(get_friend_list(),file=open(".\\friends.txt","w",encoding="utf-8"))
