from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
# ИИ. Скрипт, который имитирует события DragStart, DragOver, Drop
js_script = """
    var src = arguments[0], tgt = arguments[1];
    var dataTransfer = new DataTransfer();
    
    function createEvent(type) {
        var event = new DragEvent(type, { bubbles: true, cancelable: true, dataTransfer: dataTransfer });
        return event;
    }
    
    src.dispatchEvent(createEvent('dragstart'));
    tgt.dispatchEvent(createEvent('dragover'));
    tgt.dispatchEvent(createEvent('drop'));
    src.dispatchEvent(createEvent('dragend'));
    """


def drag_and_drop(driver: Remote, source: WebElement, target: WebElement):
    driver.execute_script(js_script, source, target)
