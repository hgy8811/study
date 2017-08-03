Binder

//实现IApplicationThread接口 提供给 ams、wms用来调用应用程序api
ApplicationThread mAppThread;


## Activity

mToken   对Ams中ActivityRecord的调用Binder



## Ams
在ActivityThread中： ActivityManagerNative.getInstance().activityPaused(...)


## Wms

IWindowSession -> Wms的Binder
ViewRootImpl.W -> Wms中调用窗口的Binder

添加 View
```java
       if (r.window == null && !a.mFinished && willBeVisible) {
                r.window = r.activity.getWindow();
                View decor = r.window.getDecorView();
                decor.setVisibility(View.INVISIBLE);
                ViewManager wm = a.getWindowManager();
                WindowManager.LayoutParams l = r.window.getAttributes();
                a.mDecor = decor;
                l.type = WindowManager.LayoutParams.TYPE_BASE_APPLICATION;
                l.softInputMode |= forwardBit;
                if (a.mVisibleFromClient) {
                    a.mWindowAdded = true;
                    wm.addView(decor, l);
                }
```
windowManager -> WindowManagerImpl -> WindowManagerGlobal  -> ViewRoot -> ViewRootImpl
