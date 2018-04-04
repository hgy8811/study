# 理解Window和WindowManager

Window-> PhoneWindow; ViewManager->WindowManager->WindowManagerImpl->;

ApplicationThread/WindowSession


## Window的创建过程
View是Android中的视图的呈现方式，但是View不能单独存在，它必须附着在Window这个概念上。

### Activity的Window创建过程
