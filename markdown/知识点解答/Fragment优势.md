## Fragment 基本概念

根据上面的定义可知：

* Fragment是依赖于Activity的，不能独立存在的。
* 一个Activity里可以有多个Fragment。
* 一个Fragment可以被多个Activity重用。
* Fragment有自己的生命周期，并能接收输入事件。
* 我们能在Activity运行时动态地添加或删除Fragment。

## Fragment的优势有以下几点：

* 模块化（Modularity）：我们不必把所有代码全部写在Activity中，而是把代码写在各自的Fragment中。
* 可重用（Reusability）：多个Activity可以重用一个Fragment。
* 可适配（Adaptability）：根据硬件的屏幕尺寸、屏幕方向，能够方便地实现不同的布局，这样用户体验更好。

## Fragment核心的类有：

Fragment：Fragment的基类，任何创建的Fragment都需要继承该类。
FragmentManager：管理和维护Fragment。他是抽象类，具体的实现类是FragmentManagerImpl。
FragmentTransaction：对Fragment的添加、删除等操作都需要通过事务方式进行。他是抽象类，具体的实现类是BackStackRecord。
NestedFragment（Fragment内部嵌套Fragment的能力）是Android 4.2提出的，support-fragment库可以兼容到1.6。通过getChildFragmentManager()能够获得管理子Fragment的FragmentManager，在子Fragment中可以通过getParentFragment()获得父Fragment。
