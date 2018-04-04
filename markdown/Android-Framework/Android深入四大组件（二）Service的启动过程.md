# Android深入四大组件（二）Service的启动过程

## ContextImpl到ActivityManageService的调用过程

要启动Service，我们会调用startService方法，它的实现最终在ContextImpl中。

ContextWrapper -> ContextImpl -> ActivityManagerProxy -> ActivityManagerService

## ActivityThread启动Service

ActivityManagerService -> ActivityServices -> ApplicationThread -> ActivityThread -> H -> Service


# Service的绑定过程

## ContextImpl到ActivityManageService的调用过程

要绑定Service，我们会调用bindService方法，它的实现最终在ContextImpl中。

ContextWrapper -> ContextImpl -> ActivityManagerProxy -> ActivityManagerService

## Service的绑定过程

ActivityManagerService -> ActivityServices -> ApplicationThread -> ActivityThread -> H

onServiceConnected方方法执行过程：

AMS -> ActivityServices -> InnerConnection -> ServiceDispatcher -> RunConnection -> ServiceConnection
