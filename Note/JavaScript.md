# jqury判断Input元素是否为空   
试了很多次的null无效，发现其实是得到的值是""
```
if (itemName == null || itemName == "") {
    $.messageBox5s("提示", "请填写应用名称!");
    return;
}
```
# XMLHttpRequest在IE和Chrome下的兼容性问题
经过多次的实践，Chrome下获取的request.response是Json对象，IE下获取的request.response是Json字符串类型（需要经过序列化）。   
需要对返回的对象进行判断处理，样例：
```
$(function () {
    $("#btnSave").click(function () {
        var logo = document.getElementById("LogoUrl").files[0];
        var title = $("#ColumnTitle").val();
        var isPicture = $("#IsPicture").val();
        //使用formdata保存文件
        var formdata = new FormData();  
        formdata.append("LogoUrl", "temp");
        formdata.append("logo", logo);
        formdata.append("ColumnTitle", title);
        formdata.append("IsPicture", isPicture);

        //创建xmlhttprequest
        var request;
        if (window.XMLHttpRequest) {
            request = new XMLHttpRequest();
        } else {
            request = new ActiveXObject('Microsoft.XMLHTTP');
        }

        //设置状态事件
        request.onreadystatechange = function () {
            if (request.readyState == 4) {//请求完成  
                debugger;
                var data = toJson(request.response);//获取响应实体
                if (request.status == 200) {//成功的请求
                    if (data.type == 1) {
                        window.parent.frameReturnByMes(data.message);
                        window.parent.frameReturnByReload(true);
                        window.parent.frameReturnByClose()
                    } else {
                        window.parent.frameReturnByMes(data.message);
                    }
                } else {
                    window.parent.frameReturnByMes(data.message);
                }
            }
        };
        request.open('POST', '@Url.Action("Create")', true);//初始化请求
        request.responseType = "json"; //设置相应类型为json
        request.send(formdata);

    });
    function toJson(obj) {
        if (typeof obj == 'string') {
            return JSON.parse(obj);
        }
        else {
            return obj;
        }
    }
});
```
# Jquery easyui treegrid 插件使用（树状表格）
```
 $('#List').treegrid({
            url: '@Url.Action("GetList")',
            width: SetGridWidthSub(10),
            methord: 'post',
            height: SetGridHeightSub(35),
            fitColumns: true,
            treeField: "ItemName",
            idField: 'Id',
            pagination: false,
            striped: true, //奇偶行是否区分
            singleSelect: true,//单选模式
            columns: [[
                { field: 'Id', title: 'Id', width: 80, sortable: true },
                { field: 'Available', title: 'Available', width: 80, sortable: true, hidden: true },
				{ field: 'ItemName', title: '模块名称', width: 80, sortable: true },
                {
                    field: 'ItemUrl', title: '链接', width: 80, sortable: true,
                    formatter: function (value, row, index) {
                        return '<a href="' + value + '" target="_blank">' + value + "</a>";
                    }
                },
            ]]
        });
```
前段JS必需配置的treeField: "ItemName",idField: 'Id'这两个字段；   
后台配置增加status字段（用来判断是否需要折叠）-----此前就是这里卡太久了；   
数据库里记得配置顶级菜单这一条记录，不然构不成树
```
if (id == null)
    id = "0";
List<NavigationModel> modelList = NavigationBLL.GetChildNodeById(id);
var json = (from r in modelList
            select new NavigationModel()
            {
                Id = r.Id,
                Available = r.Available,
                ItemName = r.ItemName,
                ItemUrl = r.ItemUrl,
                ItemSort = r.ItemSort,
                IsLast = r.IsLast,
                ParentId = r.ParentId,
                ParentName = r.ParentName,
                state = NavigationBLL.GetChildNodeById(r.Id).Count() > 0 ? "closed" : "open"
            }).ToArray();
return Json(json, JsonRequestBehavior.AllowGet);
```