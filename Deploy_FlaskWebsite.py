import os
import subprocess
import win32service
import win32serviceutil
import win32event



class FlaskWebsiteOnWinService(win32serviceutil.ServiceFramework):
    #Window服务名称（唯一名称）
    _svc_name_ = "FlaskWebsite"
    #在windows的服务管理列表中显示的名称
    _svc_display_name_ = "Flask Website"
    #Windows服务的表述
    _svc_description_="For Selenium Testing."

    #初始化操作
    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)

    #windows服务启动时执行的操作
    def SvcDoRun(self):
        work_dir=os.path.dirname(__file__)
        print("FlaskWebsite.py的目录-------------：",os.path.dirname(__file__))
        #print("FlaskWebsite.py的目录：",work_dir)
        self.child_process = subprocess.Popen("python FlaskWebsite.py",cwd=work_dir)
        win32event.WaitForSingleObject(self.hWaitStop,win32event.INFINITE)

    #windows服务停止时执行的操作
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        os.system("taskkill /t /f /pid %s" % self.child_process.pid)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(FlaskWebsiteOnWinService)




























