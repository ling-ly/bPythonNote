# 作者：ling-ly
# 开发时间：2023/2/18 14:47

# http协议
# HTTP协议包一条消息分为三大块内容，无论是请求还是响应都是三块内容
#
# 请求：
# 1.请求行 —> 请求方式（get/post) 请求url地址 协议
# 2.请求头 —> 放一些服务器要使用的附加信息※
# 3.请求体 —> 一般放一些请求参数
#
# 响应：
# 1.响应行 —> 协议 状态码 200（ok）404等
# 2.响应头 —> 放一些客服端要使用的一些附加信息※
# 3.响应体 —> 服务器返回的真正客服端要用的内容（HTML，json)等
#
# 写爬虫格外注意请求头与响应头
#
#
# 请求头中常见的一些重要内容（爬虫需要）
# 1.user-agent :请求载体的身份标识（用啥发送的请求
# 2.Referer:防盗链（这次请求是从那个页面来的？反爬会用到）
# 3.cookie：本地字符串数据信息（用户登录信息，反爬的token）
#
# 响应头中常见的一些重要内容：
# 1.cookie：本地字符串数据信息用户登录信息，反爬的token）
# 2.各种神奇的莫名其妙的字符串（这个需要经验了，一般都是token字样，防止各种攻击和反爬）
#
# 请求方式：
#     GET:显示提交
#     POST:隐示提交
