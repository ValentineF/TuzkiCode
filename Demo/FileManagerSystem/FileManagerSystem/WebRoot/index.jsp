<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ page import="Model.FileResultModel" %>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>网盘搜索</title>
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<link href="./Content/css/bootstrap.css" rel="stylesheet">
	<link href="./Content/css/bootstrap-table.css" rel="stylesheet">
	<script src="./Content/js/jquery-3.2.1.min.js"></script>
	<script src="./Content/js/bootstrap-treeview.js"></script>
	<script src="./Content/js/bootstrap-table.js"></script>
	<script src="./Content/js/bootstrap.min.js"></script>
  </head>
  
  <body>
  	<div class="container">
  		<!-- 搜索栏 -->
	  	<nav class="navbar navbar-default" role="navigation">
			<div class="container-fluid"> 
				<div class="navbar-header">
					<a class="navbar-brand" href="#">网盘搜索</a>
				</div>
				<form class="navbar-form navbar-left" role="search" action="/FileManagerSystem/sys" method="post">
					<div class="form-group">
						<input type="text" class="form-control" style="width: 300px;" placeholder="Search" name="FileName" id="FileName">
					</div>
					<button type="submit" class="btn btn-default" id="search" onclick="Clear()">搜索</button>
					<!-- 进阶搜索 -->
					<button type="button" class="btn btn-primary" data-toggle="collapse" data-target="#demo">选项</button>
					<div id="demo" class="collapse" style="marign-top:3px;">
				    	<select class="form-control" id="FileDisk" name="FileDisk">
				    		<option value="C:/JavaTest"selected="selected">所有磁盘</option>
							<option value="C:/JavaTest/FolderA">FolderA</option>
							<option value="C:/JavaTest/FolderB">FolderB</option>
							<option value="C:/JavaTest/FolderC">FolderC</option>
							<option value="C:/JavaTest/FolderD">FolderD</option>
						</select>
						<select class="form-control" id="FileType" name="FileType">
				    		<option value="" selected="selected">所有文件</option>
							<option value="gif">gif</option>
							<option value="jpg">jpg</option>
							<option value="png">png</option>
							<option value="txt">txt</option>
							<option value="doc">doc</option>
							<option value="docx">docx</option>
						</select>
					</div>
					
				</form>
			</div>
		</nav>
		<!-- 搜索结果 -->
  		<table id="cusTable" class="table table-bordered table-striped table-hover"  data-pagination="true"  data-show-refresh="true"  data-show-toggle="true"  data-showColumns="true">
			<thead>
				<tr>
					<th data-field="fileName">文件名</th>
					<th data-field="filePath">路径</th>
					<th data-field="fileTime">上次修改</th>
				</tr>
			</thead>
			<tbody>
				 <% 				 
				 List<FileResultModel> list = (List<FileResultModel>)session.getAttribute("Result");
				 String htmlCode = "";
				 if(list != null){					 
					 for(FileResultModel model : list){			 		
					 		htmlCode += "<tr>";
					 		htmlCode += "<td>" + model.FileName + "</td>";
					 		htmlCode += "<td>" + model.FilePath + "</td>";
					 		htmlCode += "<td>" + model.FileTime + "</td>";
					 		htmlCode += "</tr>";
					 	} 
				 }				 
				 %>
				 <%= htmlCode %>
				 <% htmlCode = ""; %>
				 <% session.removeAttribute("Result"); %>
			</tbody>
		</table>
  	</div>
  </body>
</html>
