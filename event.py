from pywinauto import findwindows, application, ElementNotFoundError
from pywinauto.application import WindowSpecification

from literal.stove import STOVE_CLIENT_TITLE, STOVE_CLIENT_CLASS


def exists_stove_client() -> bool:
    try:
        findwindows.find_element(title=STOVE_CLIENT_TITLE, class_name=STOVE_CLIENT_CLASS)
        return True
    except ElementNotFoundError:
        return False


def get_stove_client_process_id() -> int:
    proc = findwindows.find_element(title=STOVE_CLIENT_TITLE, class_name=STOVE_CLIENT_CLASS)
    return proc.process_id


def focus_stove_client(stove_id: int):
    application.Application(backend="win32").connect(process=stove_id)[STOVE_CLIENT_TITLE].set_focus()


def logout_event(stove_client: WindowSpecification):
    stove_client["CheckBox6"].wrapper_object().click()
    stove_client["로그아웃"].click()
    stove_client["로그아웃 하기"].click()
    
def game_start_event(stove_client: WindowSpecification):
    stove_client["게임 시작"].click()
    
def login_event(stove_client: WindowSpecification, id:str, pw:str):
    pass
    


def main():
    if not(exists_stove_client()):
        print("open stove")

    stove_id = get_stove_client_process_id()

    focus_stove_client(stove_id=stove_id)

    app = application.Application(backend="uia").connect(process=stove_id)
    stove_client = app["STOVE"]

    logout_event(stove_client=stove_client)


if __name__ == "__main__":
    # main()
    
    stove_id = get_stove_client_process_id()
    app = application.Application(backend="uia").connect(process=stove_id)
    stove_client = app["STOVE"]
    print(stove_client.print_control_identifiers())


