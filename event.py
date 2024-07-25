from pywinauto import findwindows, findbestmatch
from pywinauto import application

from typing import Optional

STOVE_CLIENT = "STOVE"
    
def get_stove_client_process_id() -> Optional[int]:
    procs = findwindows.find_elements()
    
    proc_id = None
    for proc in procs:
        if proc.name == STOVE_CLIENT:
            proc_id = proc.process_id
            break
    
    return proc_id

def get_processes() -> Optional[int]:
    procs = findwindows.find_elements()

    for proc in procs:
        print(proc, proc.process_id)

if __name__ == "__main__" :
    app = application.Application(backend='uia')
    stove_id = get_stove_client_process_id()
    
    app.connect(process=stove_id)
    stove = app["STOVE"]
    print(stove.print_control_identifiers())
    

    # app.connect(title_re=STOVE_CLIENT)
    
    # print(app)