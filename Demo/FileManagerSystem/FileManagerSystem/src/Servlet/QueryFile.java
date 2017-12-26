package Servlet;
import java.util.*;
import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;
import java.text.SimpleDateFormat;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import Model.FileResultModel; 

/**
 * Servlet implementation class QueryFile
 */
@WebServlet("/QueryFile")
public class QueryFile extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public QueryFile() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		request.setCharacterEncoding("UTF-8");
		//获取参数
		String fileName = request.getParameter("FileName");
		String fileType = request.getParameter("FileType");	
		String fileDisk = request.getParameter("FileDisk");
		//参数处理
		if(fileDisk == null){
			fileDisk = "C:/JavaTest";
		}
		if(fileType == null){
			fileType = "";
		}
		//查询
		List<FileResultModel> list = queryFile(fileName,fileType,fileDisk);
		//存session
		HttpSession result=request.getSession();
		result.setAttribute("Result", list);
		response.sendRedirect("/FileManagerSystem/index.jsp");
		
	}
	
	//搜索结果
	public static List<File> queryResult = new ArrayList<File>();	
	
	/**
	 * 遍历搜索
	 * @param file
	 * @param filter
	 * @return
	 */
	public static void searchFile(File file, FilenameFilter filter){
	     if(file.isDirectory()){
	    	 queryResult.addAll(Arrays.asList(file.listFiles(filter)));
	           for(File e : file.listFiles()){
	                 searchFile(e, filter);
	           }
	     }
   }
	/**
	 * 根据参数查询文件
	 * @param fileName 
	 * @param fileType
	 * @param fileDisk
	 * @return
	 */
	public List<FileResultModel> queryFile(final String fileName,final String fileType,String fileDisk){		
				//根据名称和类型过滤				
				FilenameFilter filter = new FilenameFilter() {
			         public boolean accept(File dir, String name) {
			            return name.contains(fileName) && name.endsWith(fileType);
			        }
			      };
			      
			    File dir = new File(fileDisk);
			    searchFile(dir,filter); 
			    								
				//填充结果
				List<FileResultModel> list = new ArrayList<FileResultModel>();				
				for(File e : queryResult){
					FileResultModel model = new FileResultModel();
					model.FileName = e.getName();
					model.FilePath = e.getAbsolutePath();
					Date time = new Date(e.lastModified());
			        SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd HH:mm:ss");
					model.FileTime = ft.format(time);
					list.add(model);
				}
				queryResult = new ArrayList<File>();
				return list;				
	}
	

}
