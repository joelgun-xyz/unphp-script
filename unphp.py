
import glob
import requests
import os
import time

__authors__ = "joelgun"
__copyright__ = ""
__credits__ = ["joelgun"]
__license__ = "MIT"
__date__ = "2020"
__version__ = "0.9"
__maintainer__ = "joelgun"
__email__ = "twitter://@joelgun"
__status__ = "production"
__description__ = "unphp - deobfuscate php code"

logo_string = """
            #                                   
            #    _    _       _____  _    _ _____  
            #   | |  | |     |  __ \| |  | |  __ \ 
            #   | |  | |_ __ | |__) | |__| | |__) |
            #   | |  | | '_ \|  ___/|  __  |  ___/ 
            #   | |__| | | | | |    | |  | | |     
            #    \____/|_| |_|_|    |_|  |_|_|     
            #                                      
            #                                      

        @joelgun - v0.9
    """

print(logo_string)
print('\n')

root_dir = ""
# directory to crawl recursively - root_dir needs a trailing slash (i.e. /root/dir/)
counter = 0
for filename in glob.iglob(root_dir + '**/*.php', recursive=True):
    print("Current file: "+filename)
   
    data = {
#API key from UnPHP     
        'api_key' : '',
    }
    files = {'file' : open(filename, 'rb')}
    r = requests.post('https://www.unphp.net/api/v2/post', files=files, data=data)
    if r.status_code == 200:
        data = r.json()
        print("  -> Deobfuscated file: "+data['output'])

        req = requests.get(data['output'])
        if req.status_code == 200:
            with open(filename,'w'): pass
            with open(filename,'w') as fd:
                fd.write(req.text)
                fd.close()
            print("   ->  File written to disk!")
    counter = counter + 1

print('\n')    
print("<> "+str(counter)+" "+"Files have been deobfuscated!")
print('\n')

print("###################")
print("#### Finished #####")
print("###################")
print('\n')

     
