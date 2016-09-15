# my_Blog

a simple blog. use flask and mongoDB

用flsk框架写的一个小博客。

+ 前端页面

  使用了bootstrap3和一个下载的博客模板。模板中使用了Google Font的360源，最近貌似不太稳定。后期有时间准备自己写一个。
  现在存在一个Bug，在移动端使用的时候会看不到菜单栏。

+ 后台管理

  用 flask-admin写的管理后台，地址是 `/admin`

+ 部署

  使用前最好先用`manage.py`中的`addUser`和`addPost`添加一个用户和一篇文章，内容随意
    
      python manage.py addUser -u admin -p 123456
      python manage.py addPost
  
  `etc`文件夹中存放了两个配置文件，是为了方便自己部署的，可以删除。

+ 遗留

  现在尚有几个遗留问题我还没处理：

    1. 加载Google Font的不稳定；
    2. 后台文章页面中的修改功能还没处理；
    3. 联系页面中准备增加向作者发邮件的功能（flask-mail）；
    4. 前端展示会将全文展示；
    5. 前端展示的时间问题；
    6. 移动端浏览时效果不理想。

博客地址：[DoubleH & Blog](www.doubleh.cf)
