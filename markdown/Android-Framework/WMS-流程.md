## WindowManagerService


### addView

#### Activity
ActivityThread -> handleResumeActivity -> (WindowManagerImpl)getWindowManager().addView()
-> WindowManagerGlobal.addView() ->ViewRootImpl.setView() -> IWindowSession.addToDisplay()
->WindowManagerService.addWindow()

IWindowSession -> (Binder)WindowManagerGlobal.getWindowSession()() WindowManagerService 在app里的Binder

IWindow -> (Binder) ViewRootImpl.W 
InputChannel
WindowInputEventReceiver ->接收用户事件（key,touch,trackball...）
ViewPostImeInputState -> 处理用户事件（key,touch,trackball...）
WindowState -> 每一个窗口在WMS里面对应的类,通过app端传递过来的IWindow调用app

#### WindowManager

### 传递事件
