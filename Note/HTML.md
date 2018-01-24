#   padding-left
设置p元素的左内边距：
```
p
  {
  padding-left:2cm;
  }
```
# i标签设置消息小红点
```
  <i style="
  display: inline-block;
            background: #f00;
            border-radius: 100%;
            width: 5px;
            height: 5px;
            position: inherit;
            bottom: 21px;
            left: 21px;
            z-index: 10;
            margin-bottom: 7px;
  "></i>
```
# 设置兼容性头n
    <meta http-equiv="X-UA-Compatible" content="IE=11">
# 使用H5的时候记得去查看IE对H5的兼容性   
常用的input type="date"  type ="file" 不支持
# 全局CSS不要少写，会影响后续开发
# HTML 5 全局 contenteditable 属性  
[可直接编辑字段，无需其他标签](http://www.w3school.com.cn/html5/att_global_contenteditable.asp) 
# 父窗口操作Iframe元素
```
<iframe src="about:blank" frameborder="0" scrolling="yes" width="100%" height="400" id="test"></iframe>
<script>
$("#test").contents().find("body").html("2312312");
</script>
```
后面的html方法可以自定义，即当作普通元素操作即可
# 用Iframe隔离页面中其他CSS的影响
```
<div id="content" style="display:none;">
    <iframe id="articleIframe" src="about:blank" frameborder="0" scrolling="yes" width="100%" height="400"></iframe>
</div>

<script type="text/javascript">
    var htmlCode = '@Html.Raw(Model.Content)';
    $("#articleIframe").contents().find("body").append(htmlCode);
</script>

<script type="text/javascript">
    $(function () {
        $('#preview').click(function () {
            $("#content").css("display", "inline");
        });
    });
</script>

```